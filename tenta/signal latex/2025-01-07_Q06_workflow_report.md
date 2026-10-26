# 2025-01-07, Uppgift 6(a-b): window functions

**PASS: both parts saved in the existing subject folder `signal calc/6 long theory rgb`. Question and folder numbers match.**

All work remains local. No calculator folder was created and no GitHub upload was performed.

## Sources and fidelity

- Original: [2025-01 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/2025-01 exam.pdf>), PDF page 4 / printed page 3, Question 6(a-b).
- Personal notes inspected first: existing folder 6 window notes, typed `6 58a.jpg` and `6 58b.jpg`, and raw [6 58.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-08/6 58.png>). The raw handwritten answer is unfinished; the typed references are not described as personal handwriting.
- Primary verified fallback: [January graded reference](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/DT081A-2025-01-07 (1)/F6PACQ9N0000_Grade-C.pdf>), PDF page 9 / handwritten page 8. Both parts received 2/2. Reference use was authorized earlier in this workflow; provenance is visible in both PNGs.
- Compact main-lobe/side-lobe reasoning follows the established October window notes. January part (a) asks frequency separation, whereas the August personal reference asks time resolution. The distinction is explicitly flagged in the new part (a).

## Verified answers

- (a) Window (iii): narrowest main lobe, hence best frequency separation among the four plots.
- (b) Window (iv): smallest visible side lobes, hence least spectral leakage among the four plots.

All four original plot crops are repeated above each solution and verified pixel-for-pixel against the exam. The source plots print `-pi` at both endpoints; the original labels are preserved rather than silently redrawn. This printing issue does not affect the main-lobe/side-lobe comparison.

## Final images

| Part | Image | Dimensions | Bytes | SHA256 |
|---|---|---|---|---|
| a | [6 51a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/6 long theory rgb/6 51a-l.png>) | 384 x 757 | 72784 | `39caf3f08271229cd77d55f9d9b0aeb997b949fb39939b94f3e232ceb922eb73` |
| b | [6 51b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/6 long theory rgb/6 51b-l.png>) | 384 x 773 | 72768 | `72208c8d44e2cfa94fb84073d5465a83d8e3f54aa098eeb022fe6c1769cabe03` |

## Validation

- Full original multipart question and both point allocations repeated on each image.
- Both final PNGs visually inspected at actual 384-pixel width; all four plot labels/curves and complete explanations fit without clipping.
- PDF text, figures, margin geometry, missing-glyph and original crop checks passed.
- All 65 previous calculator files, 47 other existing source/workflow files and 3 original inputs preserved by SHA256.
- Q1-Q5 definitions and all 19 earlier registry entries preserved. Existing eight calculator folders preserved. Shared exporter/layout unchanged.
- No incomplete subparts. Personal handwriting limitation and time/frequency distinction disclosed.

Authoritative source: [2025-01-07_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-01-07_compiled_notes.tex>).

Reproduce from the course root:

```powershell
& 'C:/Users/Jake_/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B 'tenta/signal latex/export_notes.py' --exam 2025-01-07 --question 6
```

Build intermediates and detailed validation: `tmp/pdfs/signal-export/2025-01-07/Q06/`.
