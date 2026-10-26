# 2024-10-29, Uppgift 8: image-filter kernel matching

**PASS: complete Question 8 saved in existing subject folder 7 alongside the matching handwritten kernel notes.**

**Question/folder mismatch: actual exam question 8, subject folder 7. Filename remains `8 410-l.png`.** Folder 8 contains histogram/CDF contrast enhancement, which is a different family.

All work remains local. No new output folder and no GitHub upload.

## Sources and fidelity

- Original: [2024-10 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/2024-10 exam.pdf>), PDF page 5 / printed page 4, Question 8 (5p).
- Primary own handwritten source: [7 68.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7/7 68.jpg>), 2026-08-18 Question 7, with the same five kernels and filtered images. Raw 2026-08/7 68.jpg, 7 68-2.jpg and 7 68-3.jpg were also inspected during the source comparison.
- Preserve the handwritten reasoning and order: center-only dimming, averaging, vertical edges, Laplacian zero-sum edges, sum-one sharpening.
- Secondary reference check only: [included example-solutions sheet](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/graded references/Z6EHWWR50000_Grade-B.pdf>), PDF page 3, Q8; all five matches agree.

## Explicit clarification

The handwritten averaging block is labelled 2 but discusses an equal-weight fractional averaging matrix. That is target kernel 4. A later own-note block correctly identifies kernel 2 as vertical-edge detection. The image labels this correction as an English clarification.

The handwritten idea that a zero column makes the image black is explained precisely using the coefficient sum: constant regions cancel for kernel 2, while left-to-right changes remain. For kernel 3, a zero sum cancels flat regions while edges remain; the complete image does not become zero. These clarifications retain the original pattern/sum method.

## Verified matches

| Kernel | Result | Reason |
|---|---|---|
| 1 | ii | Center coefficient 0.5 halves each pixel; neighbors ignored |
| 2 | iv | Left-right difference emphasizes vertical edges; sum 0 |
| 3 | v | Laplacian emphasizes edges in all directions; sum 0 |
| 4 | iii | Nine coefficients 1/9 average neighbors; blur with sum 1 |
| 5 | i | Identity plus Laplacian sharpens; sum 1 |

Coefficient sums, constant-patch response, horizontal/vertical ramp response of kernel 2, and kernel 5 = identity + kernel 3 were checked with exact arithmetic.

The original question says four filters but displays five kernels/results. Its wording is preserved and all five are answered. The unrelated DT056A running-header typo on the same page is excluded as in prior questions.

## Final image

- [8 410-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7/8 410-l.png>): 384 x 1364 pixels, 107750 bytes.
- SHA256: `be106405002319eeb089d89c55b5ffa9e00783bd42308f6f9079bb28142112b4`.
- The full original question, five matrices, original eye image and all five result images appear above the single complete solution. Result crops are rearranged for narrow-screen readability while their original labels and content are retained.

## Validation

- All six source image crops checked pixel-for-pixel against the original PDF.
- Latest final PNG visually inspected at native width after removing a stray heading underline from the result crops.
- PDF text, figure count, geometry, margins and missing-glyph checks passed.
- All 49 pre-existing calculator files and Q1-Q7 definitions unchanged; folder list unchanged.
- No missing parts or unresolved calculations.

Authoritative source: [2024-10-29_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2024-10-29_compiled_notes.tex>). Existing exporter and shared layout reused unchanged.

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2024-10-29 --question 8
```

Temporary PDFs, build files, preservation snapshot and detailed validation are under `tmp/pdfs/signal-export/2024-10-29/Q08/`.
