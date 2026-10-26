# 2026-01-07 Uppgift 4 - own sampling and spectrum notes

PASS. Complete Q4(a-c), in the existing `signal calc/4 sketching symmetry` folder.
Question/folder numbers match. Every image repeats the full original question,
all three parts and point values, and the original reconstruction block diagram.

## Handwritten sources used

- `tenta/signal tenta/signal calc/4 sketching symmetry/4 61a.jpg`
- `tenta/signal tenta/signal calc/4 sketching symmetry/4 61b.jpg`
- `tenta/signal tenta/signal calc/4 sketching symmetry/4 61c.jpg`

All correspond to2026-01-07. Raw originals exist under `tenta/signal tenta/2026-01/`.
The raw(c) was read to verify the final horizontal-axis label is30Hz and the
roll-off runs from25to30Hz. Only own handwriting supplies the solutions; no
lecture, graded, typed or cross-year answer used.

## Faithful method and necessary clarifications

(a) Keep omega=2pi*f ->25Hz and10Hz ->double25 ->50Hz. Retain the boxed50Hz as
the ideal Nyquist sampling limit. Briefly clarify that a real filter needs a
higher sampling rate to provide space for roll-off.

(b) Keep the handwritten order:30<50, folding limit30/2=15Hz,10Hz unchanged,
abs(25-30)=5Hz, both5and10Hz pass the30Hz LP filter. Explicitly flag the note's
cut-off wording:25Hz aliases during sampling; it is not removed by the LP filter.
15Hz is the folding limit, not sampling frequency.

The5/10Hz result is explicitly conditional on the own answer's low-frequency
(baseband) reconstruction interpretation. The original reconstruction block
does not specify whether additional sampling images have already been removed;
this uncertainty is not silently resolved by importing another solution.

(c) Keep the own one-sided amplitude spectrum:4at10Hz and3at25Hz. Preserve the
low-pass shape and25-30Hz roll-off. Dotted filter curve marked schematic and
rescaled for shared axes. Complete only the condition needed for this own
sketch to permit reconstruction:fs/2>=30, hence fs>=60Hz.60Hz is calculated
from the handwritten30Hz edge, not an arbitrary example. Anti-alias filtering
is before sampling; it cannot repair the aliased30Hz case in(b).

## Updated files and validation

Authoritative source: `tenta/signal latex/2026-01-07_compiled_notes.tex`.

| Part | Filename | Pixels |
|---|---|---|
| a | 4 61a-l.png | 384 x 528 |
| b | 4 61b-l.png | 384 x 606 |
| c | 4 61c-l.png | 384 x 728 |

All final images inspected at native384px width: PASS. No clipped text, figures,
equations, axes or labels. Final(b) rechecked after plain-English clarification;
(a)/(c) hashes unchanged after that wording-only rerender. Complete question,
figure-crop fidelity, geometry, margins, overflow and glyph checks passed.
Original figure is PDF page3/image0 crop[745,2030,1930,2210], source2481x3516.
Text checks split around extracted math subscripts; original wording unchanged.

Independent internal verification confirms frequency conversion, alias folding,
181 equal-sample comparisons of25Hz versus5Hz at30Hz sampling, and the sampling
condition derived from the sketch. These checks are not added as examples.

All102 previous calculator files,95 other source/workflow files and105 original
or reference inputs preserved. Questions1-3 TeX definitions, registries and
images unchanged. All existing folders, AGENTS.md, shared exporter/layout
preserved. Exactly three new calculator PNGs; no new output folder.

All work local. No GitHub upload, commit, push or publication.
Evidence: `tmp/pdfs/signal-export/2026-01-07/Q04/validation.json` and
`equation-verification.json`.
