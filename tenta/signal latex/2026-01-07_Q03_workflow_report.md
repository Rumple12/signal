# 2026-01-07 Uppgift 3 - simple response and frequency sketch

PASS. Complete Q3(a-c), in the existing subject folder
`signal calc/3 y(n) x(n) (electro map func)`. Question/folder numbers match.
The full original three-part question and all its equations/point values appear
above every solution. There are no original figures in Q3.

## Sources and authorization

No personal January Q3 handwriting found in the existing subject folder or raw
January notes. The user explicitly authorized: "Adapt my August handwritten
method for (a-b); solve (c) simply."

- (a): own `3 68a.jpg` composite in the existing folder, handwriting only.
  Raw pages `tenta/signal tenta/2026-08/3 68.jpg` and `3 68a.jpg` inspected in full.
  Generated text appended to the composite is not a solution source.
- (b): own `3 68b.jpg` composite; raw `3 68b.jpg` and `3 68b-2.jpg` inspected.
  These handwritten notes are dated2026-08-18. Preserve recurrence, initial rest,
  needed input values, then successive output substitutions.
- (c): raw `3 68c.png` is unfinished: a different frequency function and sketch
  prompt only. Typed content in the composite was distinguished from handwriting
  and excluded. Fresh simple solution from the verified January target function.
  No graded, typed, or previous generated solution copied.

## Target-specific results

(a) The target input equals1 for every n>=0: a unit step. Therefore the answer
is step response. The August impulse-response answer is not copied. This is a
change in the target question, not an error in the handwritten August answer.

(b) Shift the January equation down one index:
`y[n]=x[n-1]-y[n-1]+0.8y[n-2]-0.2x[n-2]`.
Assume initial rest explicitly, as in the notes, because no initial conditions
are given. Use radians and retain unrounded values internally.
`y[0]=0`, `y[1]=0.9092974268256817`, `y[2]=-0.9782609057429242`.
Only x[0] andx[1] are needed owing to the target input delay.

(c) This is a separate system. Take reciprocal denominator magnitude, calculate
three simple complex-denominator rows covering0,pi/2,pi,3pi/2,2pi, then sketch.
Key gains:2,0.5547001962,0.6666666667,0.5547001962,2. Dips are slightly after
pi/2 and before3pi/2. No derivative/extrema derivation or long trigonometric
expansion in the calculator answer. Curve directly evaluates the given function.

## Outputs and validation

Authoritative TeX: `tenta/signal latex/2026-01-07_compiled_notes.tex`.

| Part | Filename | Pixels |
|---|---|---|
| a | 3 61a-l.png | 384 x 457 |
| b | 3 61b-l.png | 384 x 819 |
| c | 3 61c-l.png | 384 x 871 |

All three latest PNGs visually inspected at native384px width: PASS. All original
question text/math, every calculation, full table and curve, axes and labels are
readable and unclipped. Text, geometry, margins, overflow and glyph checks passed.
Curve uses480 small native-LaTeX segments, with five key points marked.

Independent checks:71 original-equation residuals agree with the shifted
recurrence;1441 frequency-grid evaluations agree with the complex-magnitude
function and symmetry. These internal checks are not added to the solutions.

All99 prior calculator files,94 other source/workflow files,105 original and
reference inputs, existing folders, AGENTS.md, shared exporter/layout preserved.
Questions1-2 source definitions, registries and images are unchanged. Exactly
three new calculator PNGs; no new output folder. No previous images regenerated.

All work local. No GitHub upload, commit, push or publication.
Evidence: `tmp/pdfs/signal-export/2026-01-07/Q03/validation.json` and
`equation-verification.json`.
