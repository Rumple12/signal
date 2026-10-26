# 2025-10-28, Uppgift 5(a-b): sinusoid/DC response and filter type

**PASS: both parts saved in existing `signal calc/5 dc, cos, sin`. Question and folder numbers match.**

Verified on 2026-10-26. All work remains local. No calculator folder was created and no GitHub upload was performed. Question 6 was not processed.

## Original and own-note fidelity

- Original: [2025-10.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/2025-10.pdf>), PDF page4 / printed page3, Q5, dated2025-10-28. Full original question, input formula, two source spectra and both point allocations repeated above each solution.
- Exact own October handwriting: [5 510a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/5 dc, cos, sin/5 510a.jpg>), and raw [5 510.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/5 510.jpg>) / [5 510-2.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/5 510-2.jpg>). All read visually, including the continuation. Preserve cosine/sine/DC identification, graph1 amplitude readings, graph2 slope/phase, output components and combine order.
- Two source corrections are visible in the new PNG: the first phase line has interceptpi, and the low magnitude plateau is1/8, not the conflicting1/4 used on the handwritten continuation. The first own page already records0.125; that correct reading is retained consistently.
- Part b uses own [5 61b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/5 dc, cos, sin/5 61b.jpg>), 2026-01-07 Q5(b), specifically its explicit comparison sketch for a band-stop response. The January target itself is low-pass; its low-pass final answer is not copied. The own note's low/high pass and middle suppression explanation is applied to the actual October graph.
- The existing typed `5 510a_weird-case.jpg` was inspected as related phase context. Its discussion concerns the later phase slope; 23pi lies below75rad/s, so that later slope is unnecessary here. It is not passed off as handwriting or used as the solving source.
- Verification only: [October graded paper](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/VWCHCLKL0000_Grade-B.pdf>), PDF page10 / handwritten page7 and included example-solutions page2. These agree with gain1/8, phase near1.2rad and the band-stop classification. Exact phase below is derived from the original straight line rather than rounded1.2.

## Verified readings and corrections

| Component | Angular frequency | Gain | System phase |
|---|---|---|---|
| DC | 0 | 1 | pi |
| Cosine | 10pi=31.4159265359rad/s | 1 | pi-pi^2/5=1.16767177337rad |
| Sine | 23pi=72.2566310326rad/s | 1/8 | 0 |

The graph's axes are angular frequency in rad/s; no conversion to Hz is made before reading them.

The first phase segment connects(0,pi) and(50,0). Slope is-pi/50, hence phase(omega)=pi-(pi/50)omega. The handwritten cosine evaluation omitted its+pi intercept; the new note explicitly retains it.

The magnitude-axis ticks divide0..1 into quarters. The low plateau lies halfway between0 and1/4, giving1/8=0.125. Therefore the sine amplitude is4*(1/8)=1/2, not1. This reconciles the first own page with the erroneous continuation.

DC gain is H(0)=1*exp(jpi)=-1, so the constant+1 becomes-1. The positive cosine output amplitude stays3, while its total phase becomes pi/10+pi-pi^2/5=11pi/10-pi^2/5=1.48183103873rad. Sine phase stays0 because50<23pi<75.

## Final results

```text
y(t) = -1
       +3*cos(10*pi*t +11*pi/10 -pi^2/5)
       +(1/2)*sin(23*pi*t)
```

The system is a nonideal band-stop / band-reject filter: low and high frequencies pass with near-unit gain while a middle band is attenuated. The middle response is nonzero; no complete cancellation or exact unlabelled band edge is claimed.

## Final images

| Part | Image | Dimensions | Bytes |
|---|---|---|---|
| a | [5 510a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/5 dc, cos, sin/5 510a-l.png>) | 384 x 1196 | 71613 |
| b | [5 510b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/5 dc, cos, sin/5 510b-l.png>) | 384 x 571 | 44580 |

## Validation and preservation

- Both latest PNGs visually inspected at actual width384. Entire question and both original graph crops present. Phase intercept, gain correction, DC sign, combined output and classification readable without clipping. Part-a two-page join checked.
- Both graph crops match original PDF page4, image0 pixel-for-pixel: amplitude box[440,515,1280,1170], phase box[1360,545,2185,1170], source2547x3522. Crops adjusted to retain the amplitude label1 and remove stray input-formula text above the phase plot.
- PDF text, geometry, margins, figure count and missing-glyph checks passed.
- Exact rational gain calculation4/8=1/2 verified. Independent positive/negative complex Fourier coefficients and conjugate gain pairs reproduce the output at301 times with maximum error1.55e-14. Phase forms pi/10+pi-pi^2/5 and11pi/10-pi^2/5 agree.
- All 84 previous calculator files, 71 other source/workflow files and 6 original/reference inputs unchanged by SHA256. Q1-Q4 definitions and 18 earlier registry entries preserved. Shared layout/exporter and existing eight calculator folders unchanged. Exactly two new calculator PNGs.
- All parts complete. Corrections to the own-note arithmetic/reading are labelled rather than silently replacing the method. No unresolved values remain for the requested components.

Authoritative source updated: [2025-10-28_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-10-28_compiled_notes.tex>). Detailed numeric checks, validation and build intermediates: `tmp/pdfs/signal-export/2025-10-28/Q05/`.

Reproduce from the course root:

```powershell
& 'C:/Users/Jake_/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B 'tenta/signal latex/export_notes.py' --exam 2025-10-28 --question 5
```

## Final PNG checksums

- 5 510a-l.png: `01884f983acc72024d590718fa8a64f3c78f0319d5a9359dfcc56f61db9a84c0`
- 5 510b-l.png: `bd72f79e410bd39c43979a116e878b998842acfcc2bd1f5eb5e90edab6c67979`
