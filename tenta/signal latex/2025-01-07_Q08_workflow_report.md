# 2025-01-07, Uppgift 8: image-filter kernel matching

**PASS: complete Question 8 saved in existing `signal calc/7 kernels`, with matching handwritten kernel notes.**

**Question/folder mismatch: actual question 8, subject folder 7. Filename stays `8 51-l.png`.** Folder 8 contains histogram/CDF contrast notes, a different subject.

All work remains local. No calculator folder was created and no GitHub upload was performed.

## Sources and fidelity

- Original: [2025-01 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/2025-01 exam.pdf>), PDF page 5 / printed page 4, Q8 (5p). Full original wording, five matrices, input image and five result images retained.
- Primary own handwriting: [7 68.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7 kernels/7 68.jpg>), 2026-08-18 Question 7. Raw pages [7 68.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2026-08/7 68.jpg>), [7 68-2.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2026-08/7 68-2.jpg>) and [7 68-3.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2026-08/7 68-3.jpg>) were read as well.
- Own method/order retained: center-only scaling, averaging, vertical edges, remaining edge kernel, sharpening; inspect the pattern, then coefficient sum, then match the result. Reuse the established October Q8 solution structure and wording where the same method applies.
- Target adaptations: kernel 1 has center 2 instead of 0.5, so it brightens rather than dims. January kernel 3 uses opposite top/bottom rows, yielding horizontal-edge detection rather than the August Laplacian's multidirectional edges. The same directional-difference reasoning from own kernel 2 applies after transposing. The PNG explicitly flags the January kernel-3 change.
- The handwritten averaging block labelled 2 actually describes target kernel 4; retained explicit English clarification. Zero-sum behavior is stated as cancellation of flat regions, avoiding the inaccurate suggestion that the entire image becomes black.
- Verification: [January graded reference](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/DT081A-2025-01-07 (1)/F6PACQ9N0000_Grade-C.pdf>), PDF page 11 / handwritten page 10, received 5/5. All five matches and the horizontal-edge interpretation agree. Own handwriting supplies the method; the graded answer verifies the January mapping.

## Verified matches

| Kernel | Result | Reason |
|---|---|---|
| 1 | iv | Center 2 doubles pixel values; neighbors ignored |
| 2 | v | Left-right differences reveal vertical edges; sum 0 |
| 3 | ii | Top-bottom differences reveal horizontal edges; sum 0 |
| 4 | i | Nine weights 1/9 average neighbors; blur, sum 1 |
| 5 | iii | Identity plus Laplacian sharpens; sum 1 |

The original says four filters but shows five kernels/results. Original wording is preserved, all five are answered, and the discrepancy is flagged in the PNG. Pixel doubling describes the linear operation before display clipping. Edge polarity can reverse with convolution versus correlation; the edge direction and matching are unchanged.

## Final image and validation

- [8 51-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7 kernels/8 51-l.png>): 384 x 1413 pixels; 123497 bytes.
- SHA256: `d0d48a28f5bde121dd25a32cd2ac210d65897533ef6d5111ad492f7afaf613a7`.
- One complete unlettered question, no fabricated part letter. The original input and all five outputs appear above the solution; result crops are rearranged for readability while preserving their labels.
- All six image crops verified pixel-for-pixel against PDF page 5. Matrices checked against the original image. Input crop adjusted to exclude stray text from the line above.
- Final native-width PNG visually inspected, including the two-page join. Complete solution, matrix coefficients, picture labels and final mapping fit without clipping. PDF text, figure count, geometry, margin and missing-glyph checks passed.
- Exact rational checks passed for sums [2,0,0,1,1], flat-patch response, horizontal/vertical ramps, transpose relationship of kernels 2/3, and kernel 5 = identity + Laplacian. These verify the interpretation; no new exporter tests or converter were introduced.
- All 68 previous calculator files, 54 other source/workflow files and 6 original/reference inputs preserved by SHA256. Q1-Q7 definitions and 24 existing registry entries preserved; all eight existing folders unchanged. Exactly one new calculator image.
- No missing subparts or unresolved matches. Cross-year differences and source-label correction disclosed.

Authoritative source: [2025-01-07_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-01-07_compiled_notes.tex>). Existing exporter and layout reused unchanged.

Reproduce from the course root:

```powershell
& 'C:/Users/Jake_/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B 'tenta/signal latex/export_notes.py' --exam 2025-01-07 --question 8
```

Build intermediates and detailed validation: `tmp/pdfs/signal-export/2025-01-07/Q08/`.
