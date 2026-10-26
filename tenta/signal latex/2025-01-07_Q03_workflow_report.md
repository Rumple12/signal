# 2025-01-07, Uppgift 3(a-c): impulse response, samples and magnitude

**PASS: all three parts saved in existing subject folder `signal calc/3 y(n) x(n)`. Question and folder numbers match.**

All work remains local. No output folder was created by this task and no GitHub upload was performed.

## Sources and method

- Original: [2025-01 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/2025-01 exam.pdf>), PDF page 3 / printed page 2, Q3(a-c).
- Part (a): [3 68a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n)/3 68a.jpg>), own 2026-08-18 Q3(a) unit-impulse -> impulse response -> feedback explanation.
- Part (b): [3 68b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n)/3 68b.jpg>), own 2026-08-18 Q3(b) initial rest -> input values -> successive outputs method. Use target feedback +1,+1, impulse input and five samples; source -0.5/+0.5, 0.1^n cos(n) input and output numbers are excluded.
- Part (c): [3 68c.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n)/3 68c.jpg>) has unfinished handwriting and a completed typed magnitude-first reference. Raw [3 68c.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2026-08/3 68c.png>) confirms no completed handwritten evaluation. The PNG identifies the typed reference. Adapt its magnitude method to the target expression and requested single frequency; source coefficients 0.5/0.8 and curve values are excluded.
- January graded reference p5 confirms the impulse-response classification, but b is unevaluated with expansion errors and c is absent. It is not the solving source.

## Results and original-question issue

- (a) The unit impulse produces h(n); this recurrence is IIR.
- (b) Assume initial rest y(-1)=y(-2)=0. First five outputs: **1,1,2,3,5**.
- (c) At Omega=pi/2, the exponentials are -j and -1. Denominator 2+j gives H=(2-j)/5 and formal magnitude **1/sqrt(5) = 0.4472135955...**.

For the causal initial-rest interpretation in b, the impulse response grows and does not tend to zero; its ordinary DTFT does not converge. The pole (1+sqrt(5))/2 exceeds 1 and the causal region of convergence excludes the unit circle. The exam nevertheless supplies H and asks for evaluation. Part c explicitly labels its answer as a formal algebraic evaluation of that supplied expression. No convergent causal DTFT or stable steady-state gain is claimed. This issue is specific to the initial-rest interpretation, rather than excluding every possible noncausal region of convergence.

## Folder renames observed during work

The existing subject folders were renamed externally during this task: `2` to `2 electro map`; `3` to `3 y(n) x(n)`; `4` to `4 sketching symmetry`; `5` to `5 dc, cos, sin`; `6` to `6 long theory rgb`; `7` to `7 kernels`; `8` to `8 castle`. All original file contents remain identical; their paths changed. The task adopted those names and did not recreate the old folders. Current Q3 source paths and final output links use the new name.

The shared exporter now resolves an older calculator-note source path through the unique existing numeric subject-folder prefix when the original path is missing. Hash checks are retained. Every registered January primary source, including older folder-2 records, was resolved and verified. This avoids altering previous source records just for the folder rename.

## Final images

| Part | Image | Dimensions | Bytes |
|---|---|---|---|
| a | [3 51a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n)/3 51a-l.png>) | 384 x 673 | 42225 |
| b | [3 51b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n)/3 51b-l.png>) | 384 x 998 | 47237 |
| c | [3 51c-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n)/3 51c-l.png>) | 384 x 850 | 47920 |

## Validation

- Entire original multipart question, recurrence, input, supplied frequency equations and point allocations repeated.
- All three PNGs exactly 384 pixels wide and inspected in full; latest rendered bytes match those inspected.
- PDF text, margins, geometry and missing-glyph checks passed.
- First 20 impulse samples, exact complex components and squared magnitude, and independent numerical exponentials verified.
- All 58 prior calculator contents preserved; 47 prior paths changed with the external folder renames. Q1-Q2 definitions and registry preserved exactly.
- All other pre-existing source/workflow files unchanged apart from the documented exporter rename support.
- All subparts complete; incomplete personal handwriting for c, initial-rest assumption and DTFT issue identified explicitly.

Authoritative source: [2025-01-07_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-01-07_compiled_notes.tex>).

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2025-01-07 --question 3
```

Temporary PDFs, math verification, preservation snapshot and detailed validation are under `tmp/pdfs/signal-export/2025-01-07/Q03/`.

## Final PNG checksums

- 3 51a-l.png: `61b3f8834b34e52270bcb42a3065a9fccf94855d9ca8d30d7594a6b0075d3f2d`
- 3 51b-l.png: `c6949c278853e3ad41f2abf2bcece70d7957ac51e5e8dcfccff639eb2e9311cb`
- 3 51c-l.png: `bdd424d82b63cf1c2e591a08c9c0ab75d466ba2f9b175e61bd839fad8091f4f2`
