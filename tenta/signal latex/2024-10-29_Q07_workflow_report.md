# 2024-10-29, Uppgift 7: 2D frequency-selective properties

**PASS: the complete unlettered question is saved in existing subject folder `signal calc/7`. Question and folder numbers match.**

All work remains local. No output folder was created and no GitHub upload was performed.

## Sources and subject choice

- Original: [2024-10 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/2024-10 exam.pdf>), PDF page 5 / printed page 4, Question 7 (3p).
- Personal notes inspected first: [7 68.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7/7 68.jpg>) and its raw 2026-08 source pages. These cover kernel filtering, preservation of brightness and sharpening. Their terminology supports the image-effect explanation, but they are not an exact handwritten solution of the target response-surface question.
- Folder 7 groups image filtering and sharpening. Folder 8 contains histogram/CDF contrast enhancement; the target is a linear spatial-filter response, so folder 7 is the appropriate subject group.
- Target-specific verification: [included example-solutions sheet](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/graded references/Z6EHWWR50000_Grade-B.pdf>), PDF page 3, Q7, using the previously authorized reference fallback. The image clearly identifies this as reference-checked content.

## Verified interpretation

- At zero spatial frequency the gain is 1, retaining the average image level.
- Higher spatial frequencies have stronger gain, so edges and fine details are emphasized.
- Classification: high-frequency emphasis / high-boost, giving sharpening and edge enhancement. DC is retained.
- No exact kernel, cutoff, directional symmetry, phase response or maximum gain is inferred from this partial magnitude plot.
- The original page repeats the DT056A Visualization running-header typo already recorded for Q3-Q6. The dated DT081A cover, actual Q7 and reference agree; the unrelated header is excluded.

## Final image

- [7 410-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7/7 410-l.png>): 384 x 671 pixels, 59278 bytes.
- Exactly 384 pixels wide, visually inspected at native size, with the full original question and original surface plot above the compact solution.
- SHA256: `f0d0b6587a73988e5d1d9d259d0eeede4811b8ea2ecd28438f26be8a5d24ba40`.

## Workflow and preservation

- One image because the original question has no lettered parts. The registry uses an empty part; the filename and headings omit a fabricated letter.
- Existing exporter and layout were extended minimally for unlettered questions. A prior lettered question, Q6(a), was compiled only in a temporary directory; complete text/figure checks passed and all extracted character positions matched its previous PDF exactly.
- All 48 pre-existing calculator files unchanged. Previous Q1-Q6 definitions preserved exactly. Existing folder list unchanged.
- Original plot crop verified pixel-for-pixel against the exam; text, figure count, geometry, margins and missing-glyph checks passed.
- No missing subparts or unresolved interpretation. Exact personal handwritten match is unavailable and was not claimed.

Authoritative source: [2024-10-29_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2024-10-29_compiled_notes.tex>).

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2024-10-29 --question 7
```

Build files, preservation snapshot, regression PDF and detailed validation are under `tmp/pdfs/signal-export/2024-10-29/Q07/`.
