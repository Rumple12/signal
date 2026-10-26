# 2026-01-07 Uppgift 2 - own handwritten block-diagram method

PASS. Complete Q2(a-b), saved in existing `signal calc/2 electro map`.
Question/folder numbers match. Full original question, both parts and all point
values, plus the original diagram, appear above each solution.

## Own sources actually used

- (a): `tenta/signal tenta/signal calc/2 electro map/2 61a.jpg`.
- (b): `tenta/signal tenta/signal calc/2 electro map/2 61b.jpg`.
- Raw originals also inspected in full: `tenta/signal tenta/2026-01/2 61a.jpg`
  and `2 61b.jpg`. Both dated2026-01-07.
- (a) retains the user's present/past versus future-input causality test. The
  handwritten FIR/IIR conclusion is missing; only the short necessary explanation
  that delayed feedback gives an infinite impulse response is completed from
  the original target diagram. This completion is not claimed as handwriting.
- (b) faithfully keeps the backward route: undo0.5 -> lower delay and0.9 ->
  backward across upper delay -> add -> shift all indices down1 -> divide2 and
  collect output terms. Repeated routes merged. No new method or example added.
- No graded answer or cross-year solution used. No derivation error found.

## Result

Causal and IIR.

`y[n] - 0.9y[n-2] = 0.5x[n-1]`.

Own intermediate equations preserved, including
`x[n] + 1.8y[n-1] = 2y[n+1]` and its one-sample shift.
No transfer function, extra theory or numerical example added to the solution.

## Files and verification

Authoritative TeX: `tenta/signal latex/2026-01-07_compiled_notes.tex`.

| Part | Filename | Pixels |
|---|---|---|
| a | 2 61a-l.png | 384 x 422 |
| b | 2 61b-l.png | 384 x 730 |

Both final images inspected at native384px width: PASS. Complete question,
original diagram, all calculation steps and final answers readable; no clipping.
PDF text, geometry, margins, overflow and glyph checks passed. Diagram crop
matches PDF page2/image0 at[875,2435,1690,2695], native page2481x3519.
Original wording preserved; text validation splits around the typographic
apostrophe in "system's" to avoid an extraction-only punctuation mismatch.

Internal exact-rational verification independently simulates the two delay
blocks and both gains:72 input samples agree with the handwritten equation,
71 backward summing equations agree, and80 impulse samples confirm the loop.
These checks are not added as examples to the calculator notes.

Question1 TeX definitions, registry and images unchanged. All97 prior calculator
files,92 other source/workflow files and105 original/reference inputs preserved.
All existing folder names, AGENTS.md, shared exporter and layout unchanged.
Exactly two new calculator images. No new output folder.

All work local. No GitHub upload, commit, push or publication.
Build evidence: `tmp/pdfs/signal-export/2026-01-07/Q02/validation.json` and
`equation-verification.json`.
