# 2025-10-28, Uppgift 4(a-c): sampling, reconstruction and anti-alias spectrum

**PASS: all three calculator images saved in existing `signal calc/4 sketching symmetry`. Question and folder numbers match.**

All work remains local. No calculator folder was created and no GitHub upload was performed. Question 5 was not processed.

## Original and source priority

- Original: [2025-10.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/2025-10.pdf>), PDF page 3 / printed page 2. Date 2025-10-28. Entire original question, signal formula, fs=100Hz, fc=100Hz, contradictory aliasing hint, point allocations and reconstruction diagram retained on all three PNGs.
- Primary own handwriting: [4 61a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/4 sketching symmetry/4 61a.jpg>), [4 61b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/4 sketching symmetry/4 61b.jpg>) and [4 61c.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/4 sketching symmetry/4 61c.jpg>), 2026-01-07 Q4(a-c). These are a matching question family across years. August 2025 sampled-spectrum/periodicity notes were also inspected and are less direct matches.
- Preserve own order for a: identify angular frequencies -> divide by2pi -> choose maximum -> double. Source values25/10Hz become target30/15Hz.
- Preserve own b method: compute fs/2 -> test input components -> consider reconstructed output/filter. Source fs30Hz truly aliases25Hz; target fs100Hz does not alias15/30Hz. Do not blindly transfer the source conclusion or its low-pass-filter/aliasing conflation.
- Preserve own c method: amplitude stems from the given sinusoids, then a smooth low-pass response passing the signal. Source uses one-sided amplitudes; this convention is explicitly retained and then converted to a full two-sided spectrum. The normalized filter gain is distinguished from signal amplitudes.
- Verification reference: [October graded paper](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/VWCHCLKL0000_Grade-B.pdf>), PDF page 9 / handwritten page6, plus included example-solutions sheet on PDF page2. Both give15,30,70,85Hz in b. Their use of the term aliasing is not adopted. The example sketch's equal spectrum-line heights are not copied; target cosine and sine have different amplitudes.
- Course check: [Lecture 2](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/lectures/Lecture 2 - Introduction II.pdf>), complete pages19 and21 visually inspected. Page19 shows ideal reconstruction rejecting replicas above fs/2; page21 gives fs>2fmax and distinguishes practical reconstruction approximations. These support the explicit reconstruction qualification.

## Results and original-question ambiguity

### Part a

60pi/(2pi)=30Hz and30pi/(2pi)=15Hz. Highest input frequency30Hz gives Nyquist rate60Hz. The PNG calls60Hz the exam's limiting rate and states fs>60Hz for general ideal reconstruction, matching the course rather than promising exact reconstruction at the boundary.

### Part b

fs/2=50Hz, and both15/30Hz are below50Hz. Sampling therefore causes no baseband aliasing for this input. Original hint is misleading.

The sampled spectrum repeats every100Hz. The positive-frequency copies inside the final100Hz low-pass band are15,30,70,85Hz, with70=100-30 and85=100-15. If the reconstruction stage retains these images and the final fc100Hz filter defines the output bandwidth, the reference's intended answer is15,30,70,85Hz.

With proper ideal bandlimited reconstruction, images70/85Hz have already been rejected and the later100Hz low-pass leaves only15/30Hz. The diagram does not specify the reconstruction operator. Both answers are provided with their assumptions; no unique reconstruction behavior is invented. Extra70/85Hz terms are called spectral images, not undersampling aliases.

### Part c

Own one-sided amplitude convention:3 at15Hz and2 at30Hz. Full two-sided Fourier line weights are3/2 at+-15Hz and1 at+-30Hz; phase constants do not change these weights. The plot includes all four correct stems.

For fs100Hz, a normalized input anti-alias filter should pass through30Hz with gain near1, allow a smooth transition over30..50Hz, and strongly attenuate the stopband by50Hz. It belongs before sampling. The sketch is a qualitative real-filter roll-off, not a particular Butterworth order, cutoff specification, phase response or exact realizable filter. Dashed curve is normalized gain; stems/dots are signal line weights. This avoids silently equating the handwritten filter plateau with the largest input amplitude.

## Final images

| Part | Image | Dimensions | Bytes |
|---|---|---|---|
| a | [4 510a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/4 sketching symmetry/4 510a-l.png>) | 384 x 689 | 53606 |
| b | [4 510b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/4 sketching symmetry/4 510b-l.png>) | 384 x 769 | 70131 |
| c | [4 510c-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/4 sketching symmetry/4 510c-l.png>) | 384 x 952 | 74905 |

## Verification and preservation

- All latest PNGs visually inspected at actual width384. Complete original question and diagram, calculation steps, conditional answers and full spectrum/filter sketch are readable; no clipping. Part-c page join checked.
- Original reconstruction diagram crop matches PDF page3, image0, box [735,2042,2002,2243] pixel-for-pixel. Source raster2535x3522. Both100Hz values are preserved.
- PDF text, margins, geometry, figure count and missing-glyph checks passed. Text-check phrases were split around subscripts that the PDF extractor places on separate lines; the original question itself was unchanged.
- Exact rational frequency conversion, baseband folding and replica enumeration verify the two reconstruction models. Complex Fourier coefficients reconstruct the time-domain signal at101 times with maximum error 2.66e-15. Filter sketch passes both input frequencies and rolls off within the labelled interval.
- All 81 earlier calculator files, 69 other source/workflow files and 6 original/reference inputs preserved by SHA256. Q1-Q3 definitions and 14 existing registry entries unchanged. Existing eight subject folders and shared exporter/layout unchanged. Exactly three new calculator images.
- All subparts completed. The original b ambiguity remains inherent to the prompt and is handled explicitly with conditional results. It is not hidden by a PASS layout status.

Authoritative source updated: [2025-10-28_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-10-28_compiled_notes.tex>). Detailed validation, numeric verification and build files: `tmp/pdfs/signal-export/2025-10-28/Q04/`.

Reproduce from the course root:

```powershell
& 'C:/Users/Jake_/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B 'tenta/signal latex/export_notes.py' --exam 2025-10-28 --question 4
```

## Final PNG checksums

- 4 510a-l.png: `c45453963f8df1dbfe8af39d5aeda4bd72498c67c962e127fab219db41b428b3`
- 4 510b-l.png: `ddd7371c66dfe74cb6392e81949ac86e1c5da646b3844860975868ea9d600bd2`
- 4 510c-l.png: `75f36a5e299ab874625e5fbf0bcda594fc330f34cd5d3df7c40daae7e8485848`
