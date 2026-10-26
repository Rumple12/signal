# 2025-01-07, Uppgift 2(a-b): block diagram and difference equation

**PASS: both parts saved in the existing subject folder `signal calc/2`, matching the handwritten block-diagram notes. Question and folder numbers match.**

All work remains local. No output folder was created and no GitHub upload was performed.

## Source and method

- Original: [2025-01 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/2025-01 exam.pdf>), PDF page 2 / printed page 1, Question 2(a-b). Exact date verified in the exam cover and first question page during Question 1.
- Primary own sources: [2 68a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2/2 68a.jpg>) and [2 68b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2/2 68b.jpg>), 2026-08-18 Question 2. Same topology and actual task.
- Keep the same wording and sequence as the previous matching notes: delays, feedback, FIR/IIR; then input group, feedback group, combine, collect output terms.
- Secondary check only: [January graded answer](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/DT081A-2025-01-07 (1)/F6PACQ9N0000_Grade-C.pdf>), PDF page 4. Its recursive equation matches the original target diagram. No grade assumption is needed.

## Target adaptation

| Branch | Delays | Own-note gains | Target gains |
|---|---|---|---|
| Input | 0, 1, 3 | 1, 2, 1 | 1, 4, 2 |
| Feedback | 1, 3 | +0.3, -0.1 | +0.4, -0.2 |

There is no tap after the second delay in either chain, so no x(n-2) or y(n-2) term is added. All gains and delay positions were read from the original target diagram.

## Verified result

- (a) **IIR**, since the delayed previous outputs feed back into the system.
- Input group: x(n) + 4x(n-1) + 2x(n-3).
- Feedback group: +0.4y(n-1) - 0.2y(n-3).
- Recursive equation: y(n) = x(n) + 4x(n-1) + 2x(n-3) + 0.4y(n-1) - 0.2y(n-3).
- Collected answer: **y(n) - 0.4y(n-1) + 0.2y(n-3) = x(n) + 4x(n-1) + 2x(n-3)**.

Exact arithmetic verifies the sign change on collection and agreement of recursive/collected forms for the impulse response. The transfer numerator 1+4D+2D^3 and denominator 1-(2/5)D+(1/5)D^3 have equal degree and are not proportional; their ratio cannot be a finite polynomial. This independently verifies IIR without relying on a universal feedback rule. No stability claim is added.

## Final images

| Part | Image | Dimensions | Bytes |
|---|---|---|---|
| a | [2 51a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2/2 51a-l.png>) | 384 x 635 | 56043 |
| b | [2 51b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2/2 51b-l.png>) | 384 x 1015 | 74478 |

## Validation

- Entire original question and both point allocations repeated above each solution.
- Original diagram crop checked pixel-for-pixel against the target PDF.
- Both final PNGs inspected at native width; complete diagram, symbols, formulas and page join checked.
- PDF text, figure, margins, geometry, clipping and missing-glyph checks passed.
- All 56 prior calculator files and all 37 other pre-existing source/workflow files unchanged.
- January Question 1 definitions and registry preserved exactly; prior dated sources and output folders untouched.
- No missing subparts or unresolved values.

Authoritative source: [2025-01-07_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-01-07_compiled_notes.tex>). Existing exporter and shared layout reused unchanged.

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2025-01-07 --question 2
```

Temporary PDFs, exact-arithmetic checks, preservation snapshot and detailed validation are under `tmp/pdfs/signal-export/2025-01-07/Q02/`.

## Final PNG checksums

- 2 51a-l.png: `149de85ea8edcd37d071bb02630ada74d753a7416e959f9f1d818346a5cd2e99`
- 2 51b-l.png: `f2d695b88743843236426f6a770c9303fd2dfc18c4d6546dc18f39c976eec6c0`
