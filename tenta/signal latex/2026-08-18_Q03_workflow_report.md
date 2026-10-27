# 2026-08-18 Uppgift 3 - impulse response, samples and amplitude sketch

PASS. Complete Question3(a-c), in existing
`signal calc/3 y(n) x(n) (electro map func)/latex`.
Question and subject-folder numbers match. Every image repeats the full original
three-part question, both separate systems and all1p/2p/3p allocations.

## Original and actual solution sources

- Original exam: `tenta/signal tenta/2026-08/2026-08 exam.pdf`, PDF page3,
  printed page2; exact date August18,2026 verified previously on cover and first
  exam page. Its unchanged SHA256 is
  `f0a44d790df6c154ef9165ac0467ddb8210c23b567860b64c8790bc2cc4c90c8`.
- (a) Own handwriting in `signal calc/3 y(n) x(n) (electro map func)/3 68a.jpg`;
  inspect raw `2026-08/3 68.jpg` and `3 68a.jpg`. Exclude appended generated quote.
- (b) Own handwriting in `signal calc/3 y(n) x(n) (electro map func)/3 68b.jpg`;
  inspect raw `2026-08/3 68b.jpg` and `3 68b-2.jpg`.
- (c) Raw handwritten `2026-08/3 68c.png` and the handwritten region of
  `signal calc/3 y(n) x(n) (electro map func)/3 68c.jpg` repeat the given function
  and frequency interval but have no worked calculations or sketch. The typed
  explanation appended to the composite was identified and excluded as a
  solution source. Missing working completed with a newly authored simple
  solution under the permanent missing-handwriting rule; labelled in the image
  and registered as `independently-solved`.
- No cross-year solution or graded answer used. No completed handwritten
  calculation replaced by a different method.

## Faithful method and necessary steps

(a) Identify the unit impulse, name its output h[n] as the impulse response,
then retain the own observation that this particular system has an infinite
response because of feedback. Distinguish the response name from its IIR
classification instead of treating impulse response and IIR as synonyms.

(b) Keep own order: initial rest, input samples, then successive y[0],y[1],y[2].
Initial rest y[-1]=y[-2]=0 is an explicit assumption because the exam supplies
no initial conditions. Cosines use radians. Show every required substitution,
multiplication and sign before the final result, retaining internal calculator
precision to avoid cumulative rounding. Own final answers verified:
`y[0]=1`, `y[1]=-0.445970`, `y[2]=0.718823` to six decimal places.
No error found in the used handwritten calculations.

(c) Treat the frequency function as the separate system explicitly stated in
the exam. Take reciprocal denominator magnitude. Explain imaginary j and the
complex magnitude calculation, then substitute the required frequencies:
0 gives3.333, pi/2 gives0.535, pi gives1.429,3pi/2 gives0.535 and2pi gives3.333.
Show the necessary denominator arithmetic. Draw the smooth direct-function
curve, with dips close to pi/2 and3pi/2, a smaller peak at pi and high endpoints.
No expanded trigonometric formula, extremum calculus, invented numerical example
or extra method included.

## Outputs and verification

Authoritative source: `tenta/signal latex/2026-08-18_compiled_notes.tex`.

| Part | Filename in existing subject/latex folder | Size | SHA256 |
|---|---|---|---|
| a | `3 68a-l.png` | 384 x456 | `0628d978f1fb1b49bf36cfa8cd4415647a74b54f22dfd748c6012eca5cd3b3f4` |
| b | `3 68b-l.png` | 384 x1024 | `3b67ac6c3ac954751db54ca71c4485aba4734a2b6f6232d5db7819cdffd6f013` |
| c | `3 68c-l.png` | 384 x1081 | `15e77e5b978386ce8c05705cee42b240a185c1e0139e31fe970e0c5a1a0f0e2e` |

All three final images inspected at native384px: PASS. Complete original wording,
piecewise inputs, both frequency-function forms, all marks, substitutions,
initial-rest assumption, final answers and curve axes/labels readable and
unclipped. Question3 has no original figure; adjacent Q4 spectrum excluded.
Part(a) compiles on one narrow page; parts(b,c) on two joined pages each.
Exporter checks pass for complete-question coverage/order, geometry, margins,
overflow, glyphs, source integrity and valid PNGs.

Numerical verification reproduces all handwritten samples in radians.600 plotted
curve values match independent real/imaginary denominator calculations to less
than1e-12; symmetry about pi and all five key values verified. The native LaTeX
curve uses dense quadratic segments through actual function midpoints, rather
than straight lines between only the five marked points.

All prior Question1,2,6 definitions, registries, solutions and render calls are
unchanged.367 other files remain byte-identical at their original paths;
9 folder5 files were externally renamed/moved into `5 eq and 2graphs - dc, cos, sin`
during this task, and identical copies were verified by SHA256 and left
untouched. Together all376 prior files other than the dated source are accounted
for, including126 prior calculator-folder files. No unresolved external changes.
Shared exporter/layout, AGENTS.md and original/reference images unchanged.
Three new calculator images; no output folder created.

All work local. No commit, push or upload.
Evidence: `tmp/pdfs/signal-export/2026-08-18/Q03/validation.json`,
`content-verification.json`, `curve-samples.json`, `preservation-before.json`.
