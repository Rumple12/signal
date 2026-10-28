"""Export every completed part of one question from its authoritative exam TeX.

The source's SIGNAL_* JSON comment records are the export registry. A complete
part must have a visually verified source, a source hash, and explicit provenance.
This exporter does not invent solutions or perform automatic handwriting OCR.
"""

from __future__ import annotations

import argparse
from datetime import date
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
import unicodedata

from PIL import Image, ImageChops
import pdfplumber
from pypdf import PdfReader, PdfWriter


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
    if exam['id'] == 'example':
        folder = CALCULATOR_ROOT / 'exempl tenta'
        if not folder.is_dir():
            raise ValueError('The explicitly requested example output folder must exist.')
        suffix = '_' + part['part'] if part['part'] else ''
        return folder / f"example_Q{int(question['number']):02d}{suffix}-l.png"
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
    if question.get('output_directory') == 'exempl tenta':
        return {'folder_number': None, 'folder_name': 'exempl tenta',
                'question_folder_mismatch': False,
                'routing_notice': 'User explicitly requested one example-exam output folder.'}
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


def render_region(original: Path, crop: dict) -> Image.Image:
    """Preserve vector PDF figures and annotations as a verified original crop."""
    profile = Path(os.environ.get('USERPROFILE', str(Path.home())))
    poppler = local_tool('pdftoppm', [profile / '.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe'])
    dpi = crop.get('dpi', 180)
    x0, y0, x1, y1 = [round(v * dpi / 72) for v in crop['pdf_region']]
    page = str(crop['pdf_page'])
    data = subprocess.run([poppler, '-r', str(dpi), '-png', '-singlefile',
        '-f', page, '-l', page, '-x', str(x0), '-y', str(y0),
        '-W', str(x1-x0), '-H', str(y1-y0), str(original)],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout
    return Image.open(io.BytesIO(data)).convert('RGB')


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


def compile_question(source: Path, question: dict, parts: list[dict], latex: str) -> dict:
    """Compile only changed parts together, once; split without changing page layout."""
    build = BUILD_ROOT / source.stem.removesuffix('_compiled_notes') / f"Q{question['number']:02d}"
    build.mkdir(parents=True, exist_ok=True)
    body = []
    for part in parts:
        tag = part['part'] or 'whole'
        body.extend([f"\\typeout{{SIGNALSTART-{tag}:\\thepage}}",
                     f"\\SignalSavedRender{{{question['number']}}}{{{part['part']}}}\\clearpage",
                     f"\\typeout{{SIGNALEND-{tag}:\\thepage}}"])
    wrapper = build / 'batch.tex'
    wrapper.write_text(
        f"\\def\\SignalSelectedQuestion{{{question['number']}}}\n"
        "\\def\\SignalSelectedPart{}\n"
        "\\AtBeginDocument{\\let\\SignalSavedRender\\SignalRender\n"
        "\\renewcommand{\\SignalRender}[2]{\n" + '\n'.join(body) + "\n}}\n"
        f"\\input{{\\detokenize{{{source.as_posix()}}}}}\n", encoding='utf-8')
    environment = os.environ.copy()
    environment['MIKTEX_ENABLE_INSTALLER'] = '0'
    run([latex, '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
         f'-output-directory={build}', str(wrapper)], SOURCE_DIR, environment)
    log = build / 'batch.log'
    diagnostics = log.read_text(errors='replace')
    reader = PdfReader(build / 'batch.pdf')
    result = {}
    for part in parts:
        tag = part['part'] or 'whole'
        start = int(re.search(rf'SIGNALSTART-{tag}:(\d+)', diagnostics)[1]) - 1
        stop = int(re.search(rf'SIGNALEND-{tag}:(\d+)', diagnostics)[1]) - 1
        assert stop > start
        target = build / (part['part'] or 'whole')
        target.mkdir(exist_ok=True)
        pdf = target / 'selected.pdf'
        writer = PdfWriter()
        for page in reader.pages[start:stop]:
            writer.add_page(page)
        with pdf.open('wb') as stream:
            writer.write(stream)
        result[part['part']] = (pdf, log)
    return result


def macro_text(text: str, prefix: str) -> str:
    """Extract one balanced TeX definition for a question-local cache key."""
    start = text.find(prefix)
    if start < 0:
        return ''
    depth = 1
    for pos in range(start + len(prefix), len(text)):
        if text[pos] in '{}':
            slashes = 0
            at = pos - 1
            while at >= 0 and text[at] == '\\':
                slashes += 1
                at -= 1
            if slashes % 2:
                continue
            depth += 1 if text[pos] == '{' else -1
            if depth == 0:
                return text[start:pos + 1]
    raise ValueError('Unbalanced question or solution definition.')


def update_index(exam: dict, question: dict, parts: list[dict], source: Path) -> None:
    path = SOURCE_DIR / 'source_index.json'
    if path.exists():
        index = json.loads(path.read_text(encoding='utf-8'))
    else:
        index = {'version': 1, 'exams': {}}
        # Bootstrap only existing dated registries, never a repository-wide search.
        for candidate in SOURCE_DIR.glob('*_compiled_notes.tex'):
            if not re.match(r'\d{4}-\d{2}-\d{2}_', candidate.name):
                continue
            saved = records(candidate)
            for q in saved['QUESTION']:
                entry = index['exams'].setdefault(saved['EXAM'][0]['id'],
                    {'pdf': saved['EXAM'][0]['pdf'], 'tex': candidate.relative_to(REPO).as_posix(), 'questions': {}})
                entry['questions'][str(q['number'])] = {
                    'pdf_page': q.get('pdf_page'), 'folder_number': q.get('folder_number'),
                    'output_subfolder': q.get('output_subfolder', ''),
                    'parts': [p for p in saved['PART'] if p['question'] == q['number']]}
    entry = index['exams'].setdefault(exam['id'],
        {'pdf': exam['pdf'], 'tex': source.relative_to(REPO).as_posix(), 'questions': {}})
    entry['questions'][str(question['number'])] = {
        'pdf_page': question.get('pdf_page'), 'folder_number': question['folder_number'],
        'folder_name': question.get('output_directory') or question_folder(int(question['folder_number'])).name,
        'output_subfolder': question.get('output_subfolder', ''), 'parts': parts}
    encoded = json.dumps(index, indent=2, ensure_ascii=False) + '\n'
    if not path.exists() or path.read_text(encoding='utf-8') != encoded:
        path.write_text(encoded, encoding='utf-8')


def export_part(source: Path, exam: dict, question: dict, part: dict,
                compiled: tuple[Path, Path], poppler: str) -> dict:
    verify_started = time.perf_counter()
    source_path = resolve_source_path(part["source"])
    if not part.get("content_verified"):
        raise ValueError("Part lacks recorded visual source verification.")
    if part["source_kind"] not in ("handwritten", "user-approved-typed", "independently-solved"):
        raise ValueError("Part has no approved solution provenance.")
    if sha256(source_path) != part["source_sha256"]:
        raise ValueError("The solution source changed; recheck the transcription first.")
    question_number = int(question["number"])
    letter = part["part"]
    if not re.fullmatch(r"(?:[a-z]|ii|iii|iv|vi)?", letter):
        raise ValueError("Use a letter, i-vi, or an empty part for an unlettered question.")
    output = output_path(exam, question, part)
    build = BUILD_ROOT / exam["id"] / f"Q{question_number:02d}" / letter
    build.mkdir(parents=True, exist_ok=True)
    pdf, log = compiled
    checked = verify_pdf(pdf, log, question, part)
    verification_seconds = time.perf_counter() - verify_started
    render_started = time.perf_counter()
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
            "sha256": sha256(output), **checked, "visual_review": "NEEDS REVIEW",
            "verification_seconds": verification_seconds,
            "render_seconds": time.perf_counter() - render_started}


def main() -> int:
    started = time.perf_counter()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exam", required=True, help="Exact exam date, YYYY-MM-DD")
    parser.add_argument("--question", required=True, type=int)
    parser.add_argument("--list", action="store_true", help="List completed/missing parts without rendering")
    args = parser.parse_args()
    if not re.fullmatch(r"(?:\d{4}-\d{2}-\d{2}|example)", args.exam) or args.question < 1:
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
    identity_verified = exam.get('identity_verified') if exam['id'] == 'example' else exam.get('date_verified')
    if not identity_verified or sha256(original) != exam["pdf_sha256"]:
        raise ValueError("The original exam is unverified or changed.")
    all_sources = {original, source, SOURCE_DIR / "signal_layout.tex"}
    for crop in question.get("figure_crops", []):
        asset = SOURCE_DIR / crop["asset"]
        if 'pdf_region' in crop:
            expected = render_region(original, crop)
        else:
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
    update_index(exam, question, selected, source)
    report_path = BUILD_ROOT / args.exam / f"Q{args.question:02d}" / "validation.json"
    prior = json.loads(report_path.read_text(encoding='utf-8')) if report_path.exists() else {}
    old_outputs = {p['part']: p for p in prior.get('outputs', [])}
    tex = source.read_text(encoding='utf-8')
    common = {'question': question, 'layout': sha256(SOURCE_DIR / 'signal_layout.tex'),
              'exporter': sha256(Path(__file__)),
              'definition': macro_text(tex, f"\\SignalQuestion{{{args.question}}}{{"),
              'inputs': {p: digest for p, digest in before.items() if p != str(source)}}
    fingerprints = {}
    changed = []
    cached = {}
    for part in completed:
        payload = {**common, 'part': part,
            'solution': macro_text(tex, f"\\SignalSolution{{{args.question}}}{{{part['part']}}}{{"),
            'legacy': macro_text(tex, f"\\SignalLegacy{{{args.question}}}{{{part['part']}}}{{")}
        key = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
        fingerprints[part['part']] = key
        old = old_outputs.get(part['part'], {})
        output = output_path(exam, question, part)
        if (old.get('fingerprint') == key and old.get('output') == str(output)
                and output.is_file() and sha256(output) == old.get('sha256')):
            cached[part['part']] = {**old, 'skipped_unchanged': True}
        else:
            changed.append(part)
    source_seconds = time.perf_counter() - started
    compile_started = time.perf_counter()
    compiled = compile_question(source, question, changed, latex) if changed else {}
    compile_seconds = time.perf_counter() - compile_started
    outputs = []
    for part in completed:
        if part['part'] in cached:
            outputs.append(cached[part['part']])
        else:
            outputs.append({**export_part(source, exam, question, part, compiled[part['part']], poppler),
                'fingerprint': fingerprints[part['part']], 'skipped_unchanged': False})
    if before != {str(path): sha256(path) for path in all_sources}:
        raise ValueError("A source file changed during export.")
    report = {**listing, "status": "PASS" if not missing else "NEEDS REVIEW",
              "original_sources_unchanged": True, "source_hashes": before,
              "canonical_source": str(source), "outputs": outputs,
              "visual_review": ('PASS' if outputs and all(p.get('visual_review') == 'PASS' for p in outputs) else 'NEEDS REVIEW'),
              'timings': {'source_validation_seconds': source_seconds,
                  'compile_seconds': compile_seconds, 'compile_count': int(bool(changed)),
                  'render_seconds': sum(p.get('render_seconds', 0) for p in outputs if not p.get('skipped_unchanged')),
                  'verification_seconds': sum(p.get('verification_seconds', 0) for p in outputs if not p.get('skipped_unchanged')),
                  'total_seconds': time.perf_counter() - started}}
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
