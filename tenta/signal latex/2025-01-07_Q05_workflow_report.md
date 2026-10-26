# 2025-01-07, Uppgift 5(a-b): amplitude and phase spectra

**PASS: both parts saved in existing subject folder `signal calc/5 dc, cos, sin`. Question and folder numbers match.**

All work remains local. No output folder was created and no GitHub upload was performed.

## Sources and fidelity

- Original: [2025-01 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/2025-01 exam.pdf>), PDF page 4 / printed page 3, Q5(a-b).
- Primary own sources: [5 68a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/5 dc, cos, sin/5 68a.jpg>) and [5 68b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/5 dc, cos, sin/5 68b.jpg>), 2026-08-18 Q5. The graph values and phase shapes directly match.
- Preserve Y=XH, multiply amplitudes, add signed phases, evaluate 0/10/20/30, then sketch. Part (a) retains the exact established wording. Related sinusoid/DC variants were inspected and excluded.
- January graded reference p7 confirms (a), but misreads the amplitude intervals in (b); its proposed formula is not copied.

## Verified result

| f | Input magnitude | System magnitude | Output magnitude |
|---|---|---|---|
| 0 | 4 | 10 | 40 |
| 10 | 4 | 10 | 40 |
| 15 | 3.5 | 7.5 | 26.25 |
| 20 | 3 | 5 | 15 |
| 30 | 0 | 5 | 0 |

For nonnegative f: magnitude is 40 on [0,10], (5-f/10)(15-f/2) on (10,20], 45-(3/2)f on (20,30], and zero above 30. The product is an exact quadratic between 10 and 20. The additional midpoint 15 gives 105/4=26.25 and makes the curved segment clear while preserving the own-note method.

The phase graphs are negatives, so output phase is zero on 0<=f<30. The handwritten f=20 phase example omitted the negative sign; an explicit English clarification gives pi/4+(-pi/4)=0. At f=0 the magnitude is 40 and phase is defined. At and above f=30 the output magnitude is zero and phase is undefined. No negative-frequency extension or time-domain waveform is invented.

## Final images

| Part | Image | Dimensions | Bytes |
|---|---|---|---|
| a | [5 51a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/5 dc, cos, sin/5 51a-l.png>) | 384 x 818 | 61045 |
| b | [5 51b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/5 dc, cos, sin/5 51b-l.png>) | 384 x 1356 | 90300 |

## Validation

- Full original multipart question, all four source graphs and point allocations repeated. Source crops verified pixel-for-pixel against the exam.
- Both final PNGs inspected at actual 384-pixel width; no clipped text, graphs or formulas; joined pages checked. PDF text, figure, margin, geometry and missing-glyph checks passed.
- Exact rational checks at 301 frequencies verify amplitude products and phase cancellation. Another 101 checks verify the exact quadratic Bezier sketch.
- All 63 prior calculator contents and 42 other source/workflow files unchanged. Q1-Q4 definitions and registry preserved exactly.
- No missing subparts or unresolved values. Original handwritten references preserved.

Authoritative source: [2025-01-07_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-01-07_compiled_notes.tex>). Shared exporter and layout reused unchanged.

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2025-01-07 --question 5
```

Temporary PDFs, math verification, preservation snapshot and detailed validation are under `tmp/pdfs/signal-export/2025-01-07/Q05/`.

## Final PNG checksums

- 5 51a-l.png: `a58487b11353fcf680595227b46fcc1fce772ee0984c132db0d640e867fb20b7`
- 5 51b-l.png: `5720f0a6ab874a41c1d68229bf9cf6fa5b391ec2890358877771571a5e858428`
