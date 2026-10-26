# 2024-10-29, Uppgift 5(a-b): LTI spectra notes

**PASS: both parts saved in existing subject folder `signal calc/5`. Question number 5 and folder number 5 match.**

All work remains local. No new output folder and no GitHub upload.

## Source mapping

- Original: [2024-10 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/2024-10 exam.pdf>), PDF page 4 / printed page 3, Question 5(a-b).
- Part (a): [own handwritten 5 68a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/5/5 68a.jpg>), 2026-08-18 Question 5(a).
- Part (b): [own handwritten 5 68b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/5/5 68b.jpg>), 2026-08-18 Question 5(b).
- Primary method retained: Y=XH; multiply amplitude heights and add signed phases; evaluate f=0,10,20,30; draw amplitude and phase spectra.
- Other personal notes in folder 5 were inspected. January 2026 and October 2025 use related sinusoidal-output variants; the August 2026 spectrum-plot variant is the direct match.
- Secondary verification only: [included example-solutions sheet](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/graded references/Z6EHWWR50000_Grade-B.pdf>), PDF page 3, Q5.

## Target adaptation

| f | Input magnitude | System magnitude | Output magnitude |
|---|---|---|---|
| 0 | 0 | 20 | 0 |
| 10 | 4 | 20 | 80 |
| 20 | 4 | 10 | 40 |
| 30 | 0 | 10 | 0 |

The source note values (40,40,15,0) are not copied into the target. The target magnitude is 8f on [0,10], 120-4f on [10,30], and zero above 30. These are exact straight segments because one multiplicand is constant on each interval. Only the plotted nonnegative frequency range is claimed; an unspecified negative-frequency extension is not invented.

The target phase graphs are exact negatives on the nonzero signal support, so output phase is zero for 0<f<30. A labeled English clarification states that phase is undefined where output magnitude is zero, including f=0 and f=30. This refines the source note and example sheet's all-frequency zero-phase shorthand.

The original page repeats the inconsistent DT056A Visualization running header already recorded for Q3/Q4. The dated DT081A exam, actual Q5 content and reference entry agree. The unrelated header is excluded.

## Final images

| Part | Image | Dimensions | Bytes |
|---|---|---|---|
| a | [5 410a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/5/5 410a-l.png>) | 384 x 821 | 56446 |
| b | [5 410b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/5/5 410b-l.png>) | 384 x 1265 | 78249 |

## Verification

- Entire original multipart question and all four original graphs repeated above each solution.
- Four source crops verified pixel-for-pixel against the original PDF.
- Both final PNGs inspected at native 384-pixel width; no clipped text, formulas or graphs.
- Output magnitude formulas and phase cancellation verified with exact rational arithmetic across all intervals and boundaries.
- PDF text, figures, margins, geometry and missing-glyph checks passed.
- All 44 pre-existing calculator files unchanged; Q1-Q4 definitions preserved exactly.
- No missing subparts or unresolved calculations.

## Source and repeat command

- Authoritative source: [2024-10-29_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2024-10-29_compiled_notes.tex>).
- Existing exporter and shared layout reused without changes.

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2024-10-29 --question 5
```

Temporary PDFs, build files, preservation snapshot and detailed validation are under `tmp/pdfs/signal-export/2024-10-29/Q05/`.

## Final PNG checksums

- 5 410a-l.png: `a78bb35721a187e0a4d7010a4169b3a946d0d6f31d46fed63d10c84e4661a832`
- 5 410b-l.png: `b484d5628be79805194e4774088962fea5e1d50a69dbf9f2297f61d0d563bd81`
