# 2024-10-29, Uppgift 9: recover a 3x3 point spread function

**PASS: complete unlettered Question 9 saved in existing subject folder 7, with the image-filter kernel notes.**

**Question/folder mismatch: actual exam question 9, subject folder 7. Filename remains `9 410-l.png`.** No folder 9 was created.

All work remains local. No GitHub upload.

## Source and method

- Original: [2024-10 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/2024-10 exam.pdf>), PDF page 6 / printed page 5, Question 9 (6p).
- Personal folder-7 kernel notes and available dated raw notes were checked first. They cover kernel interpretation and coefficient sums, not a matching PSF-recovery solution. An exact handwritten example was not found.
- Verified source: [included example-solutions sheet](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/graded references/Z6EHWWR50000_Grade-B.pdf>), PDF page 3, Q9, using the previously authorized reference fallback.
- Preserve that source's direct method: each nonzero input produces a scaled, shifted impulse response; subtract overlapping copies and divide by the input amplitude. The output identifies the reference origin.
- Use x(1,1)=112. Its isolated top row gives (0,1/8,0). Center 56/112=1/2; direct neighbors 14/112=1/8. The known zero top corners rule out the diagonal overlaps at the side-weight cells.
- Lower-left weight: (10-80/8)/112=0. Lower-right weight: (36-224/8-64/8)/112=0.
- Check the overlapping output y(3,3)=224/8+64/8+176/8=58.

## Verified kernel

```text
0    1/8   0
1/8  1/2   1/8
0    1/8   0
```

The center and direct neighbors form a cross-shaped averaging filter. Coefficients sum to 1.

All 36 equations for the shown 6x6 output window were solved using exact rational arithmetic with zero-padded input. The coefficient matrix has rank 9, giving a unique 3x3 kernel; applying that kernel reproduces every given output exactly. The full matrices and verification are recorded in `tmp/pdfs/signal-export/2024-10-29/Q09/matrix-verification.json`.

The original page repeats the DT056A Visualization running-header typo recorded for Q3-Q8. The dated DT081A exam and Q9 reference agree; the unrelated header is excluded.

## Final image

- [9 410-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7/9 410-l.png>): 384 x 1374 pixels, 105206 bytes.
- SHA256: `ef14f97f7731f4c78a93c39466730a8292d14090d326419cf1b06d7fb27a892f`.
- Full original question and both original matrices appear above the complete solution. Matrix crops are stacked so values and row/column indices remain readable.

## Validation

- Both matrix crops verified pixel-for-pixel against the original PDF.
- Latest final PNG visually checked at native width, including all matrix numbers, formulas, final kernel and page join.
- PDF text, figures, margins, page geometry and missing-glyph checks passed.
- All 50 pre-existing calculator files and Q1-Q8 definitions preserved exactly; existing folder list unchanged.
- No missing subparts or unresolved calculations. The missing matching handwritten example and use of the reference are recorded explicitly.

Authoritative source: [2024-10-29_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2024-10-29_compiled_notes.tex>). Existing exporter and shared layout reused unchanged.

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2024-10-29 --question 9
```

Temporary PDFs, build files, preservation snapshot and detailed validation are under `tmp/pdfs/signal-export/2024-10-29/Q09/`.
