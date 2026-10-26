# 2026-01-07 Uppgift 5 - own DC/cosine/sine method

PASS. Complete Q5(a-b), in the existing `signal calc/5 dc, cos, sin` subject
folder. Question/folder numbers match. Full original question, both original
amplitude/phase plots and both part scores appear above each answer.

## Handwritten sources actually used

- `tenta/signal tenta/signal calc/5 dc, cos, sin/5 61a.jpg` for(a).
- `tenta/signal tenta/signal calc/5 dc, cos, sin/5 61b.jpg` for(b).
- All raw pages read in full: `tenta/signal tenta/2026-01/5 61.jpg`,
  `5 61-1.jpg`, `5 61a.jpg`, `5 61b.jpg`, dated2026-01-07.
- Only the user's corresponding handwritten method supplies the solution.
  No graded, typed or cross-year answer used.

Preserve split input -> read gains at0,15pi,20pi -> straight-line phase slope
-> multiply component amplitudes -> add plotted negative phase -> combine
DC/cosine/sine. Merge repeated pages/calculations. Retain the own phase values
-0.15pi^2 and-0.2pi^2, original input phases, DC1 and low-pass classification.
Unrelated high-pass/band-stop comparison sketches omitted from(b).

## Explicit graph-reading correction

Original graph tick spacing gives gains1,0.8,0.4. The handwriting reads1,0.7,0.3.
The difference is explicitly labelled in image(a), not silently changed.
Therefore cosine amplitude is3*0.8=2.4 and sine amplitude2*0.4=0.8, replacing
the handwritten2.1 and0.6. The original plot is retained above the correction.
Manual source reading was independently checked against native scan line
positions: measured relative plateaus about0.798 and0.399.

Final output:
`y(t)=1+2.4cos(15pi*t-pi/10-0.15pi^2)+0.8sin(20pi*t+0.1-0.2pi^2)`.

The filter is low-pass: gain1 nearzero, decreasing thenzero at high frequencies.
No new method, arbitrary numerical example, transfer-function derivation or
unrelated theory added.151 internal complex-response evaluations verify the
combined expression; these checks are not examples in the calculator notes.

## Outputs and validation

Authoritative TeX: `tenta/signal latex/2026-01-07_compiled_notes.tex`.

| Part | Filename | Pixels |
|---|---|---|
| a | 5 61a-l.png | 384 x 839 |
| b | 5 61b-l.png | 384 x 409 |

Both latest images visually inspected at native384px width: PASS. Full original
plots, tables, equations and boxed answer readable; no clipping. Complete-question,
figure fidelity, geometry, margins, overflow and missing-glyph checks passed.
Original plot crops from PDF page4/image0, native2481x3516:
amplitude[555,660,1085,1115]; phase[1155,660,1725,1115].

All105 previous calculator files,96 other source/workflow files and105 original
or reference inputs unchanged. Questions1-4 definitions, registries and images
unchanged. All original images, folder names, AGENTS.md and layout preserved.
Exactly two new calculator images; no new output folder. Folder5.5 untouched.

Shared exporter changed by one regex boundary only so integer folder5 is not
confused with separate decimal folder5.5. The old file hash is recovered by
reverting just that text, proving no other exporter change. Live routing for
all existing integer subject folders1-8 verified; Q5 correctly resolves to the
folder containing its matching personal notes. No subject or file was moved.

All work local. No GitHub upload, commit, push or publication.
Evidence: `tmp/pdfs/signal-export/2026-01-07/Q05/validation.json` and
`equation-verification.json`.
