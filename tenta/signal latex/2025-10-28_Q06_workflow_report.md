# 2025-10-28, Uppgift 6(a-b): Bayer sampling and demosaicing

**PASS: both parts saved in existing `signal calc/6 long theory rgb`. Question and folder numbers match.**

Verified on2026-10-26. All work remains local. No calculator folder was created and no GitHub upload was performed. Question7 was not processed.

## Original and source priority

- Original: [2025-10.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/2025-10.pdf>), PDF page4 / printed page3, Q6, dated2025-10-28. Full original question, both2p allocations, hint and source Bayer diagram/legend repeated above each corresponding answer.
- Original wording matches the already approved2026-08-18 Q6: color-fidelity/spatial-resolution trade-off and reconstruction of missing RGB values from Bayer samples. A different exam date does not change this question family.
- Personal handwritten material checked first: [6 68 f.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2026-08/6 68 f.png>). It only states that each pixel measures one color; it contains no complete answer to a or b. The original photo audit and available raw inventory identify no other completed handwritten Bayer solution. January6 61a/b were inspected and cover a broader camera pipeline, so their different question is not substituted.
- The user previously explicitly chose **Use the existing typed solutions**. Those approved files are [6 68a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/6 long theory rgb/6 68a.jpg>) and [6 68b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/6 long theory rgb/6 68b.jpg>). They were viewed again and matched against the actual October question and figure. Both final PNGs explicitly say they use previously approved typed solutions and that personal handwriting is unfinished.
- Existing approved solution bodies from [2026-08-18_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2026-08-18_compiled_notes.tex>) are preserved verbatim, including method/order, example values, colored grids, explanations and final answers. Only the provenance annotation is added; target date and original figure become October2025. No new converter or unrelated solution is introduced.
- Verification only: [October graded reference](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/VWCHCLKL0000_Grade-B.pdf>), included example sheet on PDF page2 and handwritten page11 / written page8. Its one-color-per-site and same-color-neighbor averaging agree. Cover Q6 total3/4 is recorded, not treated as a guarantee of every phrase. The completed approved typed source remains primary.

## Retained method and examples

Part a keeps the Bayer explanation: each site measures one component; the other two are estimated. RGGB has50% green and25% each red/blue. Color fidelity means accurate colors; spatial resolution means fine detail/edges. Strong smoothing can reduce false color while blurring detail; preserving fine edges can leave false color. The missing measurements prevent a universal exact reconstruction of both.

Part b keeps bilinear interpolation: preserve the measured channel and average nearby samples of each missing channel. At a red site, use adjacent greens and diagonal blues; reverse red/blue roles at a blue site. At green sites, use the appropriate horizontal/vertical same-color pairs. The example's measured values remain clearly identified as an example, rather than numbers supplied by the exam.

```text
R = 180
G = (100+120+110+130)/4 = 460/4 = 115
B = (70+90+80+100)/4 = 340/4 = 85
RGB = (180,115,85)
```

The reconstructed color patch and green/red/blue cell layouts are retained. Image-edge handling is mentioned without inventing a different interpolation method.

## Final images

| Part | Image | Dimensions | Bytes |
|---|---|---|---|
| a | [6 510a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/6 long theory rgb/6 510a-l.png>) | 384 x 1254 | 120415 |
| b | [6 510b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/6 long theory rgb/6 510b-l.png>) | 384 x 1552 | 126201 |

## Validation and preservation

- Both latest PNGs visually inspected in full at native width384, including page joins, color/number cells, figures, formulas, example values and final answers. No clipped text or images.
- Original diagram crop verified pixel-for-pixel against PDF page4, image0, box[460,1770,1960,2305]. Crop retains the Bayer layer and complete red/green/blue legend while excluding text from part a below.
- PDF text, figure count, geometry, margins and missing-glyph checks passed. Both outputs are joined from two PDF pages.
- Approved a/b bodies compared exactly after removing only the new source annotation. Original August source and PNGs remain unchanged.
- Exact arithmetic verifies RGB(180,115,85). The6x6 RGGB grid has9red,18green,9blue sites. Neighbor-pattern checks verify red-center adjacent greens/diagonal blues and both green-site orientations.
- All 86 previous calculator files, 74 other source/workflow files and 5 original/reference inputs unchanged by SHA256. Q1-Q5 definitions and 21 earlier registry entries preserved. Shared layout/exporter and existing eight calculator folders unchanged. Exactly two new calculator PNGs.
- No missing solution parts. The missing completed personal handwriting and use of the approved typed sources are disclosed; the typed answers are not presented as handwritten work.

Authoritative source updated: [2025-10-28_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-10-28_compiled_notes.tex>). Detailed validation, example checks and build intermediates: `tmp/pdfs/signal-export/2025-10-28/Q06/`.

Reproduce from the course root:

```powershell
& 'C:/Users/Jake_/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B 'tenta/signal latex/export_notes.py' --exam 2025-10-28 --question 6
```


## Final PNG checksums

- 6 510a-l.png: `d2ded4de37a519e52fbc70746485bbf1874f8ef0a8aa0786d30e27667c4e0f21`
- 6 510b-l.png: `517b56e7024eba65de2d45e059b0ca23fe3807e00d3216f80d09412fd92be2c4`
