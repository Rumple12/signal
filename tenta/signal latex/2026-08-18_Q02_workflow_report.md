# 2026-08-18 Uppgift 2 - handwritten feedback block-diagram solution

PASS. Complete Question2(a-b), saved in the existing subject folder
`signal calc/2 electro map/latex`. Question and subject-folder numbers match.
The existing generated part(b) image was already in this user-created child
folder; updated there rather than creating a duplicate in the parent folder.

## Original question and actual handwritten sources

- Original: `tenta/signal tenta/2026-08/2026-08 exam.pdf`, PDF page2, printed page1.
  Exact date August18,2026 verified from cover and first exam page. Unchanged
  SHA256:`f0a44d790df6c154ef9165ac0467ddb8210c23b567860b64c8790bc2cc4c90c8`.
- Part(a): own handwriting in `signal calc/2 electro map/2 68a.jpg`, with raw
  `2026-08/2 68a.jpg`. Keep the return-path feedback -> IIR reasoning.
- Part(b): own colored input/feedback grouping in
  `signal calc/2 electro map/2 68b.jpg`, with additional handwritten route tracing
  in `2 68a-j.jpg`. Also inspect raw `2026-08/2 68b.jpg`, `2 68bb.jpg`, and the
  original unfiled photo `exaam/exaam/IMG_20261024_154103.jpg`.
- Only personal handwriting supplies the solutions. Printed prompt regions and
  the generated explanation appended to `2 68b.jpg` are excluded as sources.
  No cross-year, graded or typed solution copied. No missing source or unresolved
  handwriting uncertainty affects either completed part.

## Preserved method and full steps

(a) Explain that delayed outputs return through the right-hand paths. They
continue to feed back after the input impulse has ended, giving an Infinite
Impulse Response. No extra causality or stability discussion.

(b) Preserve the handwritten order: input paths on the left, feedback paths on
the right, then combine them at y(n). Define x,y,n and the delay/gain/adder blocks.
Show each necessary multiplication separately. Input delays0,1,3 with gains1,2,1
give `x(n)+2x(n-1)+x(n-3)`. Feedback delays1,3 with gains0.3,-0.1 give
`0.3y(n-1)-0.1y(n-3)`. Explain that the second-delay positions have no branches
into sums. Add the two contributions without changing the handwritten grouping:

`y(n)=x(n)+2x(n-1)+x(n-3)+0.3y(n-1)-0.1y(n-3)`.

No alternate rearrangement, transfer-function derivation, invented numerical
example or unrelated theory. No errors found in the handwritten terms used.
The earlier Q2(b) text and its redundant introductory/summary sections were
replaced by the faithful current step-by-step version; the earlier source and
generated image are backed up only in the ignored build folder.

## Updated outputs and verification

Authoritative source: `tenta/signal latex/2026-08-18_compiled_notes.tex`.

| Part | Existing-folder image | Size | SHA256 |
|---|---|---|---|
| a | `2 electro map/latex/2 68a-l.png` | 384 x432 | `ecb3dc4b3e90457368cc01fb19478b23c5ab09778a0b853b2f6ce76b63c05690` |
| b | `2 electro map/latex/2 68b-l.png` | 384 x845 | `71c96caf87d82bfb1a79a213114a0f3ddae6230feb5bf073d7fca869924ac6e9` |

Each repeats the full original question, both1p/2p allocations and its original
diagram. Lossless diagram crop: page2/image0, native2491 x3505,
box[420,2300,1640,3010]. All6 delays,5 gains, arrows, adders and x(n)/y(n) labels
preserved. Source asset `assets/2026-08-18_Q02_block-original.png`.

Both final PNGs visually inspected at native384px: PASS. Diagram, all question
and solution text, intermediate equations, minus signs and boxed final answer
readable and unclipped. One narrow PDF page per part. Exporter checks pass for
full-question coverage/order, figure pixel equality, source hashes, geometry,
margins, overflow, missing glyphs and valid PNGs.

160 exact rational checks compare the transcribed recurrence with independently
maintained left/right delay-chain states for impulse and varying inputs. All pass.
These checks add no numerical examples to the solutions.

The exporter now supports an optional `output_subfolder` registry field, used
only for Q2's existing `latex` child. It rejects missing/invalid child folders
and creates none. Verification confirms Q2(b) updates at the existing path,
the default Q1 destination remains unchanged, and invalid paths are rejected.

All prior August Q1 and Q6 definitions, registries, solutions and render calls
are unchanged.360 other files remain unchanged at their original paths,
including116 calculator files. Nine folder4 files were externally moved into
the user's new `4.5 battery freq` folder during this task; identical contents
were located by SHA256, and those moves were left untouched. No external
changes are unresolved. Only the dated source, shared routing support and
existing Q2(b) image were intentionally updated; Q2(a), its diagram asset and
this report are new. Layout, AGENTS.md and original/reference sources untouched.

All work local. No commit, push or upload.
Evidence: `tmp/pdfs/signal-export/2026-08-18/Q02/validation.json`,
`content-verification.json` and `preservation-before.json`.
