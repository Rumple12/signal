"""Rebuild the first 384-pixel Signal calculator note from its exam and TeX.

Run with a Python installation providing Pillow and pypdf. MiKTeX and Poppler
are located locally; no packages are installed and no source scans are changed.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess

from PIL import Image
from pypdf import PdfReader


SOURCE_DIR = Path(__file__).resolve().parent
EXAM_DIR = SOURCE_DIR.parent
WORKSPACE = EXAM_DIR.parent.parent
BUILD_DIR = WORKSPACE / "tmp" / "pdfs" / "signal-calc-68b"
EXAM = EXAM_DIR / (
    "c2360b75-8986-11f0-817c-81fdb65741b1 - Omtentamen - Sundsvall.pdf"
)
TEX = SOURCE_DIR / "2026-08_compiled_notes.tex"
QUESTION = SOURCE_DIR / "assets" / "68-q2-question.png"
OUTPUT = (
    EXAM_DIR / "signal calc" / "1 - random question"
    / "68b-difference-equation.png"
)


def executable(name: str, candidates: list[Path]) -> str:
    found = shutil.which(name)
    if found:
        return found
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    raise FileNotFoundError(f"Required local tool is missing: {name}")


def run(args: list[str], cwd: Path) -> str:
    result = subprocess.run(
        args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, encoding="utf-8", errors="replace", check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stdout[-6000:])
    return result.stdout


def main() -> None:
    user_profile = Path(os.environ.get("USERPROFILE", str(Path.home())))
    runtime = (
        user_profile / ".cache" / "codex-runtimes"
        / "codex-primary-runtime" / "dependencies"
    )
    latex = executable("pdflatex", [
        user_profile / "AppData" / "Local" / "Programs" / "MiKTeX"
        / "miktex" / "bin" / "x64" / "pdflatex.exe",
    ])
    poppler = executable("pdftoppm", [
        runtime / "native" / "poppler" / "Library" / "bin" / "pdftoppm.exe",
    ])
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    QUESTION.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    # Preserve the original question's wording, diagram, and relative layout.
    page = PdfReader(EXAM).pages[1]
    scan = page.images[0].image
    if scan.size != (2491, 3505):
        raise ValueError(f"Unexpected source scan dimensions: {scan.size}")
    scan.crop((325, 2180, 2260, 3230)).save(QUESTION, optimize=True)

    run([
        latex, "-interaction=nonstopmode", "-halt-on-error",
        "-file-line-error", f"-output-directory={BUILD_DIR}", TEX.name,
    ], SOURCE_DIR)
    log = (BUILD_DIR / f"{TEX.stem}.log").read_text(errors="replace")
    if "Overfull" in log:
        raise ValueError("The TeX layout has an overflowing box; inspect its log.")
    pdf = BUILD_DIR / f"{TEX.stem}.pdf"
    if len(PdfReader(pdf).pages) != 1:
        raise ValueError("The first note must render to one continuous page.")

    rendered = BUILD_DIR / "rendered"
    run([
        poppler, "-r", "216", "-gray", "-png", "-singlefile",
        str(pdf), str(rendered),
    ], BUILD_DIR)
    with Image.open(rendered.with_suffix(".png")) as rendered_image:
        image = rendered_image.convert("L")
    ink = image.point(lambda value: 255 if value < 240 else 0)
    bounds = ink.getbbox()
    if not bounds:
        raise ValueError("The rendered note is empty.")
    if bounds[0] < 12 or bounds[2] > image.width - 12:
        raise ValueError("The note has insufficient side margins.")
    image = image.crop((0, 0, image.width, min(image.height, bounds[3] + 24)))
    height = round(image.height * 384 / image.width)
    image = image.resize((384, height), Image.Resampling.LANCZOS)
    image.save(OUTPUT, format="PNG", optimize=True, compress_level=9)

    with Image.open(OUTPUT) as final:
        final.verify()
    with Image.open(OUTPUT) as final:
        if final.width != 384 or final.format != "PNG":
            raise ValueError("Invalid final format or width.")
        metadata = {
            "exam_date": "2026-08-18",
            "question": "2(b)",
            "output": str(OUTPUT),
            "width": final.width,
            "height": final.height,
            "bytes": OUTPUT.stat().st_size,
            "mode": final.mode,
            "source_pdf_page": 2,
            "question_crop": [325, 2180, 2260, 3230],
            "handwritten_sources": [
                "IMG_20261024_154041.jpg",
                "IMG_20261024_154103.jpg",
                "IMG_20261024_154120.jpg",
            ],
        }
    (BUILD_DIR / "export.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8",
    )
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
