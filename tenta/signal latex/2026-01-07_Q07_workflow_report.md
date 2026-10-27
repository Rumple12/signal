# 2026-01-07 Uppgift 7 - point sources, PSF and convolution

PASS. Complete Question7(a-b), saved in existing `signal calc/7 kernels`.
The question and subject-folder numbers match. Each image repeats the complete
original two-part question, the given operator equation and both3p allocations.

## Sources found and actually used

- Original exam: `tenta/signal tenta/2026-01/2026-01 exam.pdf`, PDF page5,
  printed page4. Exact dated exam already verified from its cover and first page;
  unchanged SHA256 `2f0b1c6dd76c2b636a7986dead6c4fa5c3ef5eda5957a2bffb66c86fd65d6caf`.
- No matching personal handwritten derivation found in the existing calculator
  subject folders, January raw notes, other raw topic files or the visual inventory
  of all36 unfiled paper photographs.
- Own `signal calc/7 kernels/7 68.jpg` was inspected. Its August2026 handwriting
  explains matching filter kernels to image results, not weighted point-source
  superposition or the shift-invariant PSF derivation. It was not used as a
  solution source. The raw kernel pages are represented in that composite and
  in the unfiled-photo inventory.
- Both answers are newly authored under the missing-handwriting rule, explicitly
  labelled as such in the images and registered as `independently-solved`.
  No graded answer, cross-year solution or earlier generated solution copied.

## Simple but complete derivation

(a) Define the input image and unit point source; explain the image intensity as
its weight. Write the weighted point-source integral. Explain why linearity
allows applying the operator to each point separately. Substitute the given
point spread function and obtain the general output integral.

(b) Explain shift invariance as moving the response without changing its shape.
Write the relative-position PSF, substitute it into the result from(a), identify
the resulting2D convolution and explain its flip/shift/multiply/add implementation.
For a digital image the addition is a sum over pixels, rather than an integral.

Coordinate notation is explicit: the original definition uses the first pair
of h as output coordinates and the second pair as source coordinates. The
solution introduces dummy source coordinates xi,eta and relabels the output
alpha,beta to match the question's requested g(alpha,beta). The two-coordinate
h in(b) is the PSF for a source at the origin. Original notation in the question
has not been silently changed.

No arbitrary numerical examples, unrelated methods, frequency-domain derivations
or extra theory. Necessary symbols and each meaningful substitution are explained
in easy English. Question7 has no figures; the castle figures below it belong to
Question8 and are not included.

## Outputs and verification

Authoritative source: `tenta/signal latex/2026-01-07_compiled_notes.tex`.

| Part | Existing-folder output | Size | SHA256 |
|---|---|---|---|
| a | `signal calc/7 kernels/7 61a-l.png` | 384 x762 | `2970817086a30955c5c4ec207132a074c7ffb6baa7f2133372ce3a96b5ad135f` |
| b | `signal calc/7 kernels/7 61b-l.png` | 384 x721 | `2c0a4bab40792e3a588f6b9ba9b8201a651734938cbf5a8df2558812a67c657b` |

Both final images visually inspected at native384px width: PASS. All original
question text, point values, Greek symbols, integral limits and boxed final
answers are readable. No text, figures or equations clipped. Each part compiles
on one narrow page. Exporter checks pass for wording coverage, geometry, margins,
overflow, glyphs, source integrity and PNG validity.

All324 other preexisting source/reference/workflow files remain byte-for-byte
unchanged, including all116 prior calculator-folder files. The dated source's
Question1-6 definitions, registries, solutions and render calls are preserved;
only Question7 and its render calls were added. No original notes, folder names,
AGENTS.md, shared exporter or layout changed during this question.

All work local. No commit, push or GitHub upload.
Evidence: `tmp/pdfs/signal-export/2026-01-07/Q07/validation.json`,
`content-verification.json` and `preservation-before.json`.
