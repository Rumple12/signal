# 2025-01-07, Uppgift 4(a-b): spectrum extension and minimum sampling frequency

**PASS: both parts saved in existing subject folder `signal calc/4 sketching symmetry`. Question and folder numbers match.**

All work remains local. No output folder was created by this task and no GitHub upload was performed.

## Source and method

- Original: [2025-01 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/2025-01 exam.pdf>), PDF page 3 / printed page 2, Question 4(a-b).
- Primary for both parts: [4 68.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/4 sketching symmetry/4 68.jpg>), own handwritten 2026-08-18 Question 4. This is a direct match: same plotted shape, cutoff 3pi/4, and sampling rate 100 kHz.
- Keep the own-note order: mirror about zero, repeat every 2pi; read the highest normalized frequency, convert it to Hz, then apply the sampling theorem.
- The established October solution (a) is reused exactly for consistent wording and diagram style. In (b), update the October 50 kHz variant to the target 100 kHz values, which are already the values in the own handwritten notes.
- Secondary check: January graded reference PDF page 6. Its spectrum-extension method agrees. In part (b), it computes 37.5 kHz as the signal limit but omits the final doubling. The complete own-note calculation gives the correct sampling limit of 75 kHz. The incomplete graded result is not copied.

## Verified results

- (a) Mirror the real-signal magnitude spectrum around zero and repeat it every 2pi over -2pi < Omega < 2pi. Central support ends at +/-3pi/4; neighboring copies start at +/-5pi/4.
- The original flat-top knee is unlabeled. The schematic follows its visual shape without assigning that knee an exact frequency.
- (b) f_max = 100000*(3pi/4)/(2pi) = **37500 Hz**. Then f_s,min = 2*37500 = **75000 Hz**.
- The 100 kHz value is the given sampling rate used to interpret the normalized axis; 37.5 kHz is the signal limit; 75 kHz is the ideal minimum sampling rate.
- At the ideal limit, the copies meet where the plotted amplitude is zero, so no nonzero spectral components overlap.

## Final images

| Part | Image | Dimensions | Bytes |
|---|---|---|---|
| a | [4 51a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/4 sketching symmetry/4 51a-l.png>) | 384 x 870 | 54400 |
| b | [4 51b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/4 sketching symmetry/4 51b-l.png>) | 384 x 945 | 52321 |

## Validation

- Full original multipart question, diagram and both point allocations repeated above each solution.
- Original spectrum crop verified pixel-for-pixel against the target PDF; all axis labels retained.
- Both final PNGs visually inspected at native width, including spectrum symmetry/repetition, values, units and page join.
- PDF required text, figure count, margins, geometry and missing-glyph checks passed.
- Sampling arithmetic and periodic support endpoints verified with exact fractions.
- All 61 prior calculator contents and 40 other existing source/workflow files unchanged. Q1-Q3 definitions and registry preserved exactly.
- Existing subject folders retained; no new output folder.
- No missing subparts or unresolved values.

Authoritative source: [2025-01-07_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-01-07_compiled_notes.tex>). Existing exporter and shared layout reused unchanged.

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2025-01-07 --question 4
```

Temporary PDFs, math verification, preservation snapshot and detailed validation are under `tmp/pdfs/signal-export/2025-01-07/Q04/`.

## Final PNG checksums

- 4 51a-l.png: `f04a09e05751d3383708996c084f02924c929964638981f97c52b5fddd6721f0`
- 4 51b-l.png: `1f7599685c740dba5f9e3b3184fafcf7afb78deb43125447ed0bebdcc1bda63e`
