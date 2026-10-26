# 2024-10-29, Uppgift 6(a-b): window-spectrum notes

**PASS: both parts saved in the existing subject folder `signal calc/6`. Question number 6 and folder number 6 match.**

All work remains local. No output folder was created and no GitHub upload was performed.

## Source audit and provenance

- Original: [2024-10 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/2024-10 exam.pdf>), PDF page 4 / printed page 3, Question 6(a-b).
- Personal references inspected first: [6 58a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/6/6 58a.jpg>) and [6 58b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/6/6 58b.jpg>). These are typed explanations, not handwritten answers.
- Personal handwriting: [6 58.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-08/6 58.png>), dated 2025-08-20. It contains an unfinished time-resolution reminder and sketches; neither target part has a completed handwritten solution.
- Other folder-6 notes concern camera capture or Bayer reconstruction, so their solving content is excluded.
- Verified answer source: [included example-solutions sheet](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/graded references/Z6EHWWR50000_Grade-B.pdf>), PDF page 3, Q6, using the previously authorized graded-reference fallback. Images identify the reference origin rather than presenting it as personal handwriting.

## Critical question change

The 2025 personal typed references ask about best **time resolution** in part (a), selecting iv. The target 2024 part (a) asks about best **frequency separation**, selecting iii. The complete target wording was checked before adapting the notes.

- Part (a): **Window iii** has the narrowest main lobe, allowing nearby frequency components to be separated more clearly.
- Part (b): **Window iv** has the smallest visible side lobes, giving the least spectral leakage.
- Preserve the personal typed notes' comparison method: main-lobe width for separation, side-lobe level for leakage.
- Do not generalize the reference's exact-zero-outside-the-main-lobe claim; the output uses the visually supported smallest-visible-side-lobes wording.

The original plot right endpoints are printed -pi, as are the left endpoints; the crops preserve this printing error. The choice of windows does not depend on that label. The original page also repeats the inconsistent DT056A Visualization running header already recorded for Q3-Q5; the dated DT081A exam and actual Q6 reference entry agree.

## Final images

| Part | Image | Dimensions | Bytes |
|---|---|---|---|
| a | [6 410a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/6/6 410a-l.png>) | 384 x 767 | 70690 |
| b | [6 410b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/6/6 410b-l.png>) | 384 x 783 | 71146 |

## Verification

- Entire original multipart question, point allocations and all four original plots repeated above each solution.
- All four crops checked pixel-for-pixel against the original PDF.
- Both PNGs exactly 384 pixels wide and visually reviewed at native size; no cropped text, graph labels or answers.
- PDF text, figures, margins, geometry and missing-glyph checks passed.
- All 46 pre-existing calculator files unchanged; Q1-Q5 definitions preserved exactly.
- Existing folder list unchanged; the original 6 68 LaTeX images and all references remain untouched.
- Both subparts complete; personal handwritten answers remain missing/incomplete and the fallback is identified explicitly.

## Source and repeat command

- Authoritative source: [2024-10-29_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2024-10-29_compiled_notes.tex>).
- Existing exporter and shared layout reused without changes.

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2024-10-29 --question 6
```

Temporary PDFs, build files, preservation snapshot and detailed validation are under `tmp/pdfs/signal-export/2024-10-29/Q06/`.

## Final PNG checksums

- 6 410a-l.png: `3c3fe5e45134f08f8013cbcc1136e29a675d994c1abdf43164fc5f757592d7a8`
- 6 410b-l.png: `28a4b62d9b6e888684a6a7ccef24fddddcf1a53459b61204e2ee1ef1c9ac25f8`
