"""Export every completed part of one question from its authoritative exam TeX.

The source's SIGNAL_* JSON comment records are the export registry. A complete
part must have a visually verified source, a source hash, and explicit provenance.
This exporter does not invent solutions or perform automatic handwriting OCR.
"""

from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import unicodedata

from PIL import Image, ImageChops
import pdfplumber
from pypdf import PdfReader


SOURCE_DIR = Path(__file__).resolve().parent
REPO = SOURCE_DIR.parent.parent
BUILD_ROOT = REPO / "tmp" / "pdfs" / "signal-export"
CALCULATOR_ROOT = REPO / "tenta" / "signal tenta" / "signal calc"


def question_folder(folder_number: int) -> Path:
    """Resolve a chosen subject folder without creating or renaming folders."""
    candidates = sorted(
        path for path in CALCULATOR_ROOT.iterdir()
        if path.is_dir() and re.match(rf"^{folder_number}(?!\.\d)(?:$|[ ._-])", path.name)
    )
    if len(candidates) != 1:
        found = ", ".join(path.name for path in candidates) or "none"
        raise ValueError(
            f"Subject folder {folder_number} needs one existing output folder; found {found}. "
            "Clarify the destination. No output folder was created."
        )
    return candidates[0]


def output_path(exam: dict, question: dict, part: dict) -> Path:
    """Route by subject; keep the original exam question number in the title."""
    exam_date = date.fromisoformat(exam["id"])
    question_number = int(question["number"])
    date_code = f"{exam_date.year % 10}{exam_date.month}"
    image_title = f"{question_number} {date_code}{part['part']}"
    folder = question_folder(int(question["folder_number"]))
    subfolder = question.get("output_subfolder")
    if subfolder is not None:
        if not isinstance(subfolder, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 _-]*", subfolder):
            raise ValueError("Use one existing child folder name for output_subfolder.")
        folder = folder / subfolder
        if not folder.is_dir():
            raise ValueError("The chosen output subfolder must already exist; no folder was created.")
    return folder / f"{image_title}-l.png"


def routing_info(question: dict) -> dict:
    """Expose question/folder mismatches in listings and export reports."""
    question_number = int(question["number"])
    folder_number = int(question["folder_number"])
    folder = question_folder(folder_number)
    mismatch = question_number != folder_number
    return {"folder_number": folder_number, "folder_name": folder.name,
            "output_subfolder": question.get("output_subfolder", ""),
            "question_folder_mismatch": mismatch,
            "routing_notice": (
                f"Question {question_number} is saved in folder {folder.name} by subject; "
                f"filenames keep question number {question_number}."
                if mismatch else "Question and subject folder numbers match.")}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_source_path(relative: str) -> Path:
    """Keep source links usable when a premade numbered folder is renamed."""
    path = REPO / relative
    if path.is_file():
        return path
    try:
        parts = path.relative_to(CALCULATOR_ROOT).parts
    except ValueError:
        return path
    if len(parts) == 2:
        match = re.match(r"^(\d+)(?:$|[ ._-])", parts[0])
        if match:
            return question_folder(int(match[1])) / parts[1]
    return path


def records(path: Path) -> dict:
    result = {"EXAM": [], "QUESTION": [], "PART": []}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = re.match(r"^% SIGNAL_(EXAM|QUESTION|PART) (\{.*\})$", line)
        if match:
            try:
                result[match[1]].append(json.loads(match[2]))
            except json.JSONDecodeError as error:
                raise ValueError(f"Invalid registry JSON at {path.name}:{line_number}") from error
    if len(result["EXAM"]) != 1:
        raise ValueError("The dated source must contain exactly one SIGNAL_EXAM record.")
    return result


def local_tool(name: str, candidates: list[Path]) -> str:
    located = shutil.which(name)
    if located:
        return located
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    raise FileNotFoundError(f"Missing {name}. Install/configure it before exporting.")


def run(command: list[str], cwd: Path, environment: dict | None = None) -> None:
    result = subprocess.run(command, cwd=cwd, env=environment,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            text=True, encoding="utf-8", errors="replace", check=False)
    if result.returncode:
        raise RuntimeError(result.stdout[-7000:])


def normalized(text: str) -> str:
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", text))


def verify_pdf(pdf: Path, log: Path, question: dict, part: dict) -> dict:
    diagnostics = log.read_text(errors="replace")
    if "Overfull" in diagnostics or "Missing character:" in diagnostics:
        raise ValueError("Layout overflow or missing glyph; inspect the build log.")
    if "LaTeX Warning: File" in diagnostics or "undefined references" in diagnostics:
        raise ValueError("Missing source image or reference; inspect the build log.")
    text = ""
    figures = 0
    with pdfplumber.open(pdf) as document:
        for page in document.pages:
            expected_width = 384 * 72 / 72.27
            expected_height = 900 * 72 / 72.27
            if abs(page.width - expected_width) > 0.1 or abs(page.height - expected_height) > 0.1:
                raise ValueError("The PDF does not use 384pt x 900pt paper.")
            margin = 10 * 72 / 72.27 - 1.1
            for item in [*page.chars, *page.images]:
                if (item["x0"] < margin or item["x1"] > page.width - margin
                        or item["top"] < margin or item["bottom"] > page.height - margin):
                    raise ValueError(f"Text/math/figure outside the page margins: {item.get('text', 'figure')}")
            figures += len(page.images)
            text += "\n" + (page.extract_text(x_tolerance=2) or "")
    flattened = normalized(text)
    for required in [*question.get("required_question_text", []), *part.get("required_solution_text", [])]:
        if normalized(required) not in flattened:
            raise ValueError(f"Required original question or solution text is missing: {required}")
    if question.get("required_question_text"):
        heading = f"Solution for part ({part['part']})" if part["part"] else "Solution"
        solution_start = flattened.find(normalized(heading))
        if solution_start < 0 or any(
            flattened.find(normalized(required)) + len(normalized(required)) > solution_start
            for required in question["required_question_text"]
        ):
            raise ValueError("The entire original question must appear before the solution.")
    if figures < question.get("required_figures", 0):
        raise ValueError("An original question figure is missing.")
    return {"pages": len(PdfReader(pdf).pages), "embedded_figures": figures,
            "complete_question_repeated": True, "solution_text_present": True,
            "pdf_geometry_verified": True, "no_clipping_verified": True,
            "no_missing_glyphs": True}


def export_part(source: Path, exam: dict, question: dict, part: dict,
                latex: str, poppler: str) -> dict:
    source_path = resolve_source_path(part["source"])
    if not part.get("content_verified"):
        raise ValueError("Part lacks recorded visual source verification.")
    if part["source_kind"] not in ("handwritten", "user-approved-typed", "independently-solved"):
        raise ValueError("Part has no approved solution provenance.")
    if sha256(source_path) != part["source_sha256"]:
        raise ValueError("The solution source changed; recheck the transcription first.")
    question_number = int(question["number"])
    letter = part["part"]
    if not re.fullmatch(r"[a-z]?", letter):
        raise ValueError("Use a-z for a subquestion, or an empty part for an unlettered question.")
    output = output_path(exam, question, part)
    build = BUILD_ROOT / exam["id"] / f"Q{question_number:02d}" / letter
    build.mkdir(parents=True, exist_ok=True)
    wrapper = build / "selected.tex"
    wrapper.write_text(
        f"\\def\\SignalSelectedQuestion{{{question_number}}}\n"
        f"\\def\\SignalSelectedPart{{{letter}}}\n"
        f"\\input{{\\detokenize{{{source.as_posix()}}}}}\n", encoding="utf-8")
    environment = os.environ.copy()
    # Disable automatic MiKTeX package installation; failures stay explicit.
    environment["MIKTEX_ENABLE_INSTALLER"] = "0"
    run([latex, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
         f"-output-directory={build}", str(wrapper)], SOURCE_DIR, environment)
    pdf = build / "selected.pdf"
    checked = verify_pdf(pdf, build / "selected.log", question, part)
    page_bands = []
    for page_number in range(1, checked["pages"] + 1):
        prefix = build / f"page-{page_number:03d}"
        run([poppler, "-r", "216", "-png", "-f", str(page_number), "-l",
             str(page_number), "-singlefile", str(pdf), str(prefix)], build)
        with Image.open(prefix.with_suffix(".png")) as raster:
            image = raster.convert("RGB")
        dark = image.convert("L").point(lambda value: 255 if value < 242 else 0)
        bounds = dark.getbbox()
        if not bounds:
            continue
        if bounds[0] < 18 or bounds[2] > image.width - 18:
            raise ValueError("The rasterized note has insufficient horizontal margins.")
        image = image.crop((0, max(0, bounds[1] - 24), image.width,
                            min(image.height, bounds[3] + 24)))
        page_bands.append(image.resize((384, round(image.height * 384 / image.width)),
                                        Image.Resampling.LANCZOS))
    if not page_bands:
        raise ValueError("The selected solution rendered no content.")
    height = sum(band.height for band in page_bands) + 8 * (len(page_bands) - 1)
    final = Image.new("RGB", (384, height), "white")
    cursor = 0
    for band in page_bands:
        final.paste(band, (0, cursor))
        cursor += band.height + 8
    # A palette preserves the colored Bayer diagram while keeping CG50 files small.
    palette = final.quantize(colors=256, method=Image.Quantize.MEDIANCUT,
                             dither=Image.Dither.NONE)
    palette.save(output, format="PNG", optimize=True, compress_level=9)
    with Image.open(output) as reopened:
        reopened.verify()
    if final.width != 384:
        raise ValueError("The final PNG width is incorrect.")
    return {"part": letter, "status": "PASS", "source_kind": part["source_kind"],
            "source": str(source_path), "output": str(output), "width": 384,
            "height": height, "bytes": output.stat().st_size, "mode": "P",
            "sha256": sha256(output), **checked, "visual_review": "NEEDS REVIEW"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exam", required=True, help="Exact exam date, YYYY-MM-DD")
    parser.add_argument("--question", required=True, type=int)
    parser.add_argument("--list", action="store_true", help="List completed/missing parts without rendering")
    args = parser.parse_args()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.exam) or args.question < 1:
        parser.error("Supply an exact exam date and a positive question number.")
    source = SOURCE_DIR / f"{args.exam}_compiled_notes.tex"
    registry = records(source)
    exam = registry["EXAM"][0]
    if exam["id"] != args.exam:
        raise ValueError("The requested date does not match the exam registry.")
    questions = [entry for entry in registry["QUESTION"] if entry["number"] == args.question]
    if len(questions) != 1:
        raise ValueError("The question is absent or declared more than once.")
    question = questions[0]
    selected = [entry for entry in registry["PART"] if entry["question"] == args.question]
    if len({entry["part"] for entry in selected}) != len(selected):
        raise ValueError("A solution part is declared more than once.")
    completed = [entry for entry in selected if entry["status"] == "complete"]
    missing = [letter for letter in question["parts"]
               if not any(entry["part"] == letter and entry["status"] == "complete" for entry in selected)]
    listing = {"exam": args.exam, "question": args.question, **routing_info(question),
               "completed_parts": [entry["part"] or "whole question" for entry in completed],
               "incomplete_parts": [letter or "whole question" for letter in missing]}
    if args.list:
        print(json.dumps(listing, indent=2))
        return 0
    if not completed:
        print(json.dumps({**listing, "status": "FAIL", "reason": "No completed source-backed solutions."}, indent=2))
        return 2
    original = REPO / exam["pdf"]
    if not exam.get("date_verified") or sha256(original) != exam["pdf_sha256"]:
        raise ValueError("The original exam is unverified or changed.")
    all_sources = {original, source, SOURCE_DIR / "signal_layout.tex"}
    for crop in question.get("figure_crops", []):
        asset = SOURCE_DIR / crop["asset"]
        scan = PdfReader(original).pages[crop["pdf_page"] - 1].images[crop.get("image_index", 0)].image
        expected = scan.convert("RGB").crop(tuple(crop["box"]))
        with Image.open(asset) as supplied:
            supplied = supplied.convert("RGB")
            if supplied.size != expected.size or ImageChops.difference(expected, supplied).getbbox():
                raise ValueError("A question figure no longer matches its original exam crop.")
        all_sources.add(asset)
    all_sources.update(resolve_source_path(entry["source"]) for entry in selected if "source" in entry)
    before = {str(path): sha256(path) for path in all_sources}
    profile = Path(os.environ.get("USERPROFILE", str(Path.home())))
    runtime = profile / ".cache/codex-runtimes/codex-primary-runtime/dependencies"
    latex = local_tool("pdflatex", [profile / "AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdflatex.exe"])
    poppler = local_tool("pdftoppm", [runtime / "native/poppler/Library/bin/pdftoppm.exe"])
    outputs = [export_part(source, exam, question, part, latex, poppler) for part in completed]
    if before != {str(path): sha256(path) for path in all_sources}:
        raise ValueError("A source file changed during export.")
    report = {**listing, "status": "PASS" if not missing else "NEEDS REVIEW",
              "original_sources_unchanged": True, "source_hashes": before,
              "canonical_source": str(source), "outputs": outputs,
              "visual_review": "NEEDS REVIEW"}
    report_path = BUILD_ROOT / args.exam / f"Q{args.question:02d}" / "validation.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
