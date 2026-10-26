# 2025-10-28, Uppgift 7(a-b): 2D high-pass response and output selection

**PASS: both parts saved in existing `signal calc/7 kernels`. Question and folder numbers match.**

Verified on2026-10-26. All work remains local. No calculator folder was created and no GitHub upload was performed. Question8 was not processed.

## Original and source priority

- Original: [2025-10.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/2025-10.pdf>), PDF page5 / printed page4, Q7. Full question, both2p/3p allocations, original magnitude surface, clock input and all four labelled candidate outputs repeated on each PNG.
- Existing calculator subject folder7 contains the related image-filter/kernel notes inspected during prior questions. Exact October raw notes are a closer match than those kernel exercises or the opposite January low-pass question.
- Primary part-a source: [7 510-1.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/7 510-1.jpg>), own dated2025-10-28 handwritten page2/3, with supporting [7 510.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/7 510.jpg>), page1/3. Preserve low/high spatial-frequency meaning -> surface height/gain -> compare center and outer region -> image effect. The exact target graph has a central dip, so its high-pass interpretation is retained; the January low-pass adaptation is not reused as an answer.
- Primary part-b source: [7 510-2.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/7 510-2.jpg>), own page3/3. Preserve predict dark/edge-dominant output -> compare i,ii,iii,iv -> select. Its choice(ii) is wrong and is explicitly corrected in the PNG, while preserving the comparison method.
- Verification/reference correction: [October graded paper](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/VWCHCLKL0000_Grade-B.pdf>), included typed example on PDF page2 and handwritten Q7 on PDF page12 / written page9. Both choose(iii), supported by the original magnitude shape and retained edges. Cover Q7 total5/5 is recorded as supporting evidence, not a computed output proof.

## Verified interpretation

### Part a

Low spatial frequencies represent smooth regions and gradual brightness changes; high spatial frequencies represent edges and fine details. Low surface means low gain and high surface means high gain. The surface has a minimum near(u,v)=(0,0), so low spatial frequencies are strongly attenuated. Gain rises outward and is above1 at higher spatial frequencies, emphasizing fine detail and edges across directions. Classification: high-pass / edge-enhancing behavior.

The response shape and image effect follow the own notes. No exact filter coefficients, cutoff, phase response or exact DC gain are inferred from this partial magnitude plot.

### Part b and visible correction

- (i) is blurred: low-pass behavior, not the target.
- (ii) is edge-dominant but more selective about which outlines remain.
- (iii) has a dark background and a more complete set of clock/digit outlines in several orientations: best qualitative match to the target.
- (iv) retains a bright smooth face and resembles a brightened image; this does not match strong attenuation of low-frequency regions.

Final answer: **Image(iii), most likely.**

The handwritten note chose(ii) and rejected(iii) as dark/missing edges. The PNG labels an English clarification: dark smooth regions are expected under low-frequency suppression; inspect which outlines and orientations remain rather than rejecting an image based on darkness alone. The unsupported handwritten band-pass label for(iv) is not copied.

Only a magnitude response and candidate images are given. The result is appropriately framed as the most likely candidate; no unique pixel-for-pixel output is claimed and no fabricated filtering experiment or kernel is introduced.

## Final images

| Part | Image | Dimensions | Bytes |
|---|---|---|---|
| a | [7 510a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7 kernels/7 510a-l.png>) | 384 x 1156 | 123911 |
| b | [7 510b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7 kernels/7 510b-l.png>) | 384 x 1176 | 129755 |

## Validation and preservation

- All six source crops checked pixel-for-pixel against original PDF page5, image0, source2535x3522. Crop boxes: surface[415,520,1020,980], input[525,1188,800,1375], i[515,1480,795,1735], ii[895,1480,1175,1735], iii[1270,1480,1550,1735], iv[1650,1480,1935,1735]. The input crop excludes stray text above; result labels are retained.
- Both latest final PNGs visually inspected at native width384, including the faint original image(iii), labels, surface, full question, page join, explanations and correction. No clipping or missing content.
- PDF text, figure count, geometry, margins and missing-glyph checks passed. Both outputs contain six original figures and join two PDF pages vertically.
- This is a qualitative interpretation task. Verification uses the original plots/images, own method and two consistent reference explanations; no unnecessary numerical implementation tests were added.
- All 88 previous calculator files, 76 other source/workflow files and 5 original/reference inputs unchanged by SHA256. Q1-Q6 definitions and 24 previous registry entries preserved. Shared layout/exporter and existing eight calculator folders unchanged. Exactly two new calculator images.
- Both parts complete. The source selection error is disclosed and corrected explicitly.

Authoritative source updated: [2025-10-28_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-10-28_compiled_notes.tex>). Detailed validation and build intermediates: `tmp/pdfs/signal-export/2025-10-28/Q07/`.

Reproduce from the course root:

```powershell
& 'C:/Users/Jake_/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B 'tenta/signal latex/export_notes.py' --exam 2025-10-28 --question 7
```

## Final PNG checksums

- 7 510a-l.png: `6454811e36f821fd2953f8c4417198982047ad8ad263052540cdc1976c6d107e`
- 7 510b-l.png: `15abe64850e022c4c6730757d628ba446b5afbe5d4c0e2213be520595ab55f71`
