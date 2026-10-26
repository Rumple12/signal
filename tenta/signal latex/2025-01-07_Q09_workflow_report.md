# 2025-01-07, Uppgift 9: recover a 3x3 point spread function

**PASS: complete unlettered Question 9 saved in existing `signal calc/7 kernels`.**

**Question/folder mismatch: actual question 9, subject folder 7. Filename remains `9 51-l.png`.** No calculator folder was created. All work remains local; no GitHub upload.

## Sources and method

- Original: [2025-01 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/2025-01 exam.pdf>), PDF page 6 / printed page 5, Q9 (6p). Full original wording and both original matrix images retained.
- Own source inspected first: [7 68.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7 kernels/7 68.jpg>) and the available dated raw-note inventory. Own notes cover kernel interpretation, averaging and coefficient sums, rather than a matching PSF-recovery derivation. No exact own handwritten solution was found; this is disclosed rather than presented as personal handwriting.
- Verified fallback: [January graded paper](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/DT081A-2025-01-07 (1)/F6PACQ9N0000_Grade-C.pdf>), PDF page 12 / handwritten page 11, Q9, 6/6. Use follows the already authorized reference fallback.
- January input/output matrices match October 2024 Q9 cell-for-cell. The established October solution is reused verbatim: each input impulse produces a scaled copy of the kernel; subtract overlapping contributions and divide by the input value. Existing reference provenance remains visible in the PNG.
- Start from x(1,1)=112. Its isolated top output row (0,14,0) gives top weights (0,1/8,0). Center 56/112=1/2; direct neighbors 14/112=1/8. Known zero upper corners eliminate diagonal overlaps at the neighboring cells.
- Lower-left corner: (10-80/8)/112=0. Lower-right: (36-224/8-64/8)/112=0.
- Overlap check at (3,3): 224/8+64/8+176/8=28+8+22=58, matching the target.

## Verified kernel

```text
0    1/8   0
1/8  1/2   1/8
0    1/8   0
```

Cross-shaped averaging kernel: center 1/2, four direct neighbors 1/8, zero corners; sum 1.

All 36 equations for the shown 6x6 output window were solved independently with exact Fraction arithmetic and Gaussian elimination. Rank 9 gives a unique 3x3 kernel. Applying it reproduces every shown output. Both matrices, reconstruction and kernel are recorded in `tmp/pdfs/signal-export/2025-01-07/Q09/matrix-verification.json`. Input is zero outside the given 6x6 image; comparison uses the shown output window.

## Final image and validation

- [9 51-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7 kernels/9 51-l.png>): 384 x 1374 pixels; 105412 bytes.
- SHA256: `ee9270609ee49b8cd6be7054b7139226912078235c3710607ab4bc15ecd136ed`.
- One complete unlettered question, no invented part letter. Both original matrices are stacked above the solution so all values and row/column indices remain readable.
- Both crops verified pixel-for-pixel against original PDF page 6, image 0: input box [370,650,1110,1250], output box [1270,650,2020,1250].
- Final PNG visually inspected at native 384-pixel width, including page join, matrix values, calculations and final kernel. Text, figure count, margins, geometry and missing-glyph checks passed.
- All 69 previous calculator files, 61 other source/workflow files and 3 original/reference inputs preserved by SHA256. Q1-Q8 definitions and 26 earlier registry entries preserved exactly. Existing eight calculator folders and shared exporter/layout unchanged. Exactly one new calculator image.
- No incomplete parts or unresolved calculations. Missing own handwritten match and reference fallback recorded.

## January exam completion

Question 9 is the last question. PDF pages 7-8 were visually checked and contain formula sheets. All nine question records are complete, with 19 calculator PNGs present at width 384. Earlier images were verified as preserved; they were not regenerated.

Authoritative source: [2025-01-07_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-01-07_compiled_notes.tex>).

Reproduce from the course root:

```powershell
& 'C:/Users/Jake_/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B 'tenta/signal latex/export_notes.py' --exam 2025-01-07 --question 9
```

Detailed validation and build intermediates: `tmp/pdfs/signal-export/2025-01-07/Q09/`.
