# 2026-01-07 Uppgift 8 - handwritten histogram-equalization explanation

PASS. Complete unlettered Question8, saved in the existing `signal calc/8 castle`
subject folder as `8 61-l.png`. Question and folder numbers match.

## Actual sources and permission

- Original question: `tenta/signal tenta/2026-01/2026-01 exam.pdf`, PDF page5,
  printed page4. Its exact question,5p allocation and all six figures are preserved.
- No personal January Question8 handwriting was found. The user explicitly
  answered: **Use my August handwritten notes** for this January question.
- Primary: personal handwriting in `signal calc/8 castle/8 68.jpg`.
- Additional handwritten clarification: `signal calc/8 castle/8 68-j.jpg`.
  Its printed header belongs to October2025; only the August2026 handwritten
  region was used. The current question and figures come from the January PDF.
- All four raw August pages inspected and used:
  `tenta/signal tenta/2026-08/8 68.jpg`, `8 68-2.jpg`, `8 68-3.jpg`, `8 68-4.jpg`.
  They explicitly identify August18,2026,Question8.
- No graded answer, typed explanation or earlier generated solution used as a
  solution source. The final image honestly identifies the authorized August notes.

## Faithful and complete explanation

Preserve the handwritten order: original histogram(c), original cumulative
histogram(e), transformation, enhanced cumulative histogram(f), enhanced
histogram(d). Merge repeated axis and cumulative-distribution explanations.
Explain the original and enhanced image relationship directly.

The only equation is the handwritten `s=(L-1)H(r)`. Define r,s,L and normalized
H(r). Make its necessary application steps explicit: read r, find H(r), multiply
by L-1, replace r with s and repeat for each pixel. No invented numerical
example, extra formula, alternative method or lengthy derivation.

Explicitly flag the handwritten wording error: a straight cumulative histogram
means an even distribution across intensity levels, not that all pixels have
the same constant intensity. Retain the handwritten observation that actual
digital cumulative distributions can be stepped. The enhanced histogram is
more balanced, not necessarily perfectly flat; its plotted peaks remain visible.

## Updated outputs and checks

- Authoritative source: `tenta/signal latex/2026-01-07_compiled_notes.tex`.
- Image: `tenta/signal tenta/signal calc/8 castle/8 61-l.png`.
- Dimensions:384 x1098;155371bytes.
- Image SHA256:`d5875c62239fd8b958db818c4080e8af05463e43c3182e717c5033bf2b162093`.
- Lossless original crop: PDF page5/image0, native2484 x3519,
  box[800,1415,1670,2240], saved as `assets/2026-01-07_Q08_castle-original.png`.
  Includes images(a,b), histograms(c,d), cumulative plots(e,f), all six labels
  and h,h-prime,H,H-prime labels. Crop pixel equality verified by exporter.
- Exporter checks: PASS for full original question before solution, figure,
  source hashes, required explanation coverage, margins, geometry, overflow,
  missing glyphs and valid384px PNG. Two narrow PDF pages joined between
  numbered steps3and4, with no paragraph or formula clipped.
- Final native384px visual inspection: PASS. All original text, six figures,
  labels, equation, numbered steps, correction and final answer are readable.

Question1-7 definitions, registries, solution text and existing render calls are
unchanged.317 other files remain byte-identical at their original paths.
During this task,11 preexisting files in folder4 were externally renamed/moved
into its `latex` subfolder or renamed `overview.png`; identical contents were
located and verified by SHA256. These concurrent moves were left untouched.
Together this accounts for all328 prior files other than the dated source,
including119 prior calculator-folder files. No external changes were reverted.
Shared layout, exporter, AGENTS.md and original handwritten/reference files are
unchanged by this question. No output folder created.

The dated source now has all8 exam questions complete, with21 calculator images
present. Prior images in folder4 were located at their externally moved paths;
their old source definitions were not rewritten during this Question8 task.

All work local. No commit, push or upload.
Evidence: `tmp/pdfs/signal-export/2026-01-07/Q08/validation.json`,
`content-verification.json` and `preservation-before.json`.
