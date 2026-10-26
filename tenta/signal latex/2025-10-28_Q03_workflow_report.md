# 2025-10-28, Uppgift 3(a-c): impulse response, samples and magnitude sketch

**PASS: all three parts saved in existing `signal calc/3 y(n) x(n)`. Question and folder numbers match.**

All work remains local. No calculator folder was created and no GitHub upload was performed. Question 4 was not processed.

## Original and source priority

- Original: [2025-10.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/2025-10.pdf>), PDF page 3 / printed page 2, Q3(a-c), dated 2025-10-28. Full original recurrence, both piecewise inputs, both equivalent supplied frequency-function expressions and point allocations repeated above each answer. Long equations are split vertically without changing them.
- Part (a): [3 68a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n)/3 68a.jpg>), own 2026-08-18 Q3(a), unit impulse -> impulse response -> feedback. Exact previously verified January Q3(a) solution wording retained. The target's feedforward delayed-input term and new feedback coefficients occur in the original question.
- Part (b): [3 68b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n)/3 68b.jpg>), own 2026-08-18 Q3(b), initial rest -> input values -> successive outputs. Target input is 0.6^n cos(n), not the source 0.1^n. Preserve the method and compute the new recurrence, including -0.3x(n-1).
- Part (c): [3 68c.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n)/3 68c.jpg>) includes unfinished handwriting and a completed typed magnitude/sketch reference. Raw [3 68c.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2026-08/3 68c.png>) confirms handwriting is unfinished. Typed reference is identified honestly. Preserve magnitude -> simplify denominator -> key points -> sketch, but use target coefficients 1 and 0.5 rather than the reference 0.5 and 0.8. Compute actual minima rather than copying approximate quarter-period minima.
- October [graded reference](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/VWCHCLKL0000_Grade-B.pdf>): handwritten PDF pages 7-8 were inspected. It uses x(0)=0.6 in b, gives the wrong gain 2 at pi and claims pi-periodicity in c. Those results are rejected. The included typed example sheet on PDF page 2 agrees with the independently computed target samples and corrected curve. Own notes remain the source for a/b.

## Verified results

### Part a

A unit impulse produces the system's impulse response h(n), assuming initial rest. The target recurrence is IIR. Its transfer relation has numerator z(z-0.3) and denominator z^2+z-0.5; neither numerator root cancels a denominator root, so the response is not finite. First exact impulse samples are 1,-13/10,9/5,... . The calculator explanation retains the user's simpler impulse/feedback reasoning.

### Part b

Rearrange to y(n)=x(n)-0.3x(n-1)-y(n-1)+0.5y(n-2). Assume y(-1)=y(-2)=0; x(-1)=0 follows from the input definition. Use radians and retain full precision.

- x(0)=1; x(1)=0.6cos(1)=0.3241813835208838; x(2)=0.36cos(2)=-0.14981286115697126.
- y(0)=1.
- y(1)=0.6cos(1)-1.3=-0.9758186164791162.
- y(2)=0.36cos(2)-0.78cos(1)+1.8=1.2287513402658798.

The PNG explicitly checks 0.6^0=1. Rounding is applied only to displayed final outputs.

### Part c

This is explicitly ANOTHER system. Evaluate its supplied H independently of a/b. No causal region of convergence, stability or DTFT convergence for the a/b recurrence is inferred for it.

For D=1-exp(-jOmega)-0.5exp(-2jOmega):

```text
Re D = 1-cos(Omega)-0.5cos(2Omega)
Im D = sin(Omega)+0.5sin(2Omega)
|D|^2 = 2.25-cos(Omega)-cos(2Omega)
      = 27/8-2*(cos(Omega)+1/4)^2
|H| = 1/sqrt(2.25-cos(Omega)-cos(2Omega))
```

| Omega | Magnitude |
|---|---|
| 0 | 2 |
| pi/2 | 2/sqrt(13) = 0.5547001962 |
| pi | 2/3 = 0.6666666667 |
| 3pi/2 | 2/sqrt(13) |
| 2pi | 2 |

Minima occur at acos(-1/4)=1.8234765819 and 2pi-acos(-1/4)=4.4597087252 rad, with magnitude sqrt(8/27)=0.544331054. Thus the curve dips slightly after pi/2 and before 3pi/2. It has high endpoints and a smaller central peak. Period is 2pi, not pi. The PNG explicitly corrects the erroneous reference value at pi and states the period.

The plot is drawn directly in LaTeX from 720 calculated segments, with the exact formula used at every vertex. Complex-exponential, equivalent rational and real-cosine forms agree at 1,441 frequencies. The maximum magnitude error at segment midpoints is 0.000190189, below 0.0002, or about 0.012 display pixels vertically. A rendering overflow in automatic Bezier sampling was repaired with four explicit samples per short segment; no shared layout/exporter change was needed. Final curve is smooth and visually checked.

## Final images

| Part | Image | Dimensions | Bytes |
|---|---|---|---|
| a | [3 510a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n)/3 510a-l.png>) | 384 x 692 | 40832 |
| b | [3 510b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n)/3 510b-l.png>) | 384 x 1034 | 54030 |
| c | [3 510c-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n)/3 510c-l.png>) | 384 x 1216 | 63144 |

## Verification and preservation

- All latest images inspected at native width 384. All original question text/math and the correct corresponding solution present. Multi-page joins, part-c plot, axes, values, minima and final answer checked.
- PDF text, margins, geometry and missing-glyph checks passed. Original question contains no figures; the solution plot uses native vector drawing.
- Output samples independently agree with the unrolled closed forms. Twenty-four exact impulse samples and non-cancellation check support IIR. Magnitude algebra, extrema, periodicity and curve data verified.
- All 78 previous calculator files, 68 other source/workflow files and 6 original/reference inputs unchanged by SHA256. Q1-Q2 definitions and 10 earlier registry entries preserved. Shared layout/exporter and existing eight calculator folders unchanged. Exactly three new calculator PNGs.
- All parts complete. Initial-rest/radians assumptions, unfinished personal handwriting for c and reference corrections disclosed.

Authoritative source updated: [2025-10-28_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-10-28_compiled_notes.tex>).

Reproduce from the course root:

```powershell
& 'C:/Users/Jake_/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B 'tenta/signal latex/export_notes.py' --exam 2025-10-28 --question 3
```

Detailed validation, numeric results and build intermediates: `tmp/pdfs/signal-export/2025-10-28/Q03/`.

## Final PNG checksums

- 3 510a-l.png: `9db0c955f317024d976052d17edc3013820c54300cb9a553b3760e42448c87b7`
- 3 510b-l.png: `3ce9d4070c406a9a9082742d2aa7042ff02621683e16224e854463f3c5de7783`
- 3 510c-l.png: `481784b08f40c181f0e5d68e2ed9d9ea7c4a9ecb7c868c67b3b28ec32a90d062`
