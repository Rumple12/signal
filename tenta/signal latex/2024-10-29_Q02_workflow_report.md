# 2024-10-29, Uppgift 2(a-b): local workflow report

**PASS: both parts exported using the existing converter and the existing numbered folder 2.**

All changes remain local. No output folder was created, and nothing was uploaded to GitHub. Only Uppgift 2 was exported in this run.

## Sources and scope

- Original question: [2024-10 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/2024-10 exam.pdf>), PDF page 2 / printed page 1. Complete wording, input sequence, filter taps, both parts and (3p)/(2p) allocations verified visually.
- Input sequence: s(n) = {3, 7, 10, 3, -5}. Impulse response: h(n) = {-0.5, 0, 0.5}.
- Personal 2024-10 Question 2 notebook notes were not found among the previously inventoried files. The user continued the explicitly approved graded-reference workflow. The unrelated 2026-01/2026-08 Question 2 notes were not used as this exam's solution sources.

| Part | Reference | PDF page | How it was used |
|---|---|---|---|
| a | [NVIXOOBS0000_Grade-D.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/graded references/NVIXOOBS0000_Grade-D.pdf>) | 5 | Handwritten convolution method and n=0..4 substitutions; originally incomplete, marked 2/3. |
| a | [Z6EHWWR50000_Grade-B.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/graded references/Z6EHWWR50000_Grade-B.pdf>) | 2 | Included typed example-solutions sheet supplies the complete seven-value sequence; used to check/complement the handwritten working. |
| b | Same included example-solutions sheet | 2 | Complete typed differentiation/change-emphasis explanation, clearly identified as a reference rather than personal handwriting. |

Both selected reference-paper covers were checked for the exact 2024-10-29 date. Extracted copies match their ZIP entries byte-for-byte.

## Corrections and assumptions

- The handwritten solution stops at n=4, giving only five output samples. Full linear convolution requires 5+3-1 = 7 samples. The notes explicitly flag this and show y(5)=1.5 and y(6)=-2.5, consistent with the included example solution.
- The handwritten boundary condition is written as an inconsistent chained inequality. The notes explicitly state the intended zero extension: s(n)=0 outside n=0..4 and h(n)=0 outside n=0..2.
- The question has no origin marker. The first element of each list is indexed n=0, matching the model calculations. This assumption is visible in the notes.
- The handwritten crossed-out s(0)h(3) term is preserved as an explicit explanation that h(3)=0; zero terms are not silently treated as unexplained arithmetic changes.
- Other inspected candidates contain a positive y(1) where -3.5 is required, incorrect y(4) arithmetic, and missing tails. Inversion/attenuation explanations for part (b) received no marks and were not presented as correct.
- Part (b) uses the complete included example solution. Its derivation of the tap difference, constant-input cancellation and sign convention is explicitly labelled English clarification.
- With the listed causal tap order, y(n) = (s(n-2)-s(n))/2. The sign is the reverse of the opposite difference. This is a finite-difference approximation to differentiation; DC is cancelled. The notes qualify the reference's high-pass interpretation near DC rather than claiming a monotone high-pass response across all frequencies.
- No unresolved numerical uncertainty remains after the explicit indexing assumption and source corrections.

## Independent numerical verification

Exact rational convolution gives:

```text
n:     0     1     2    3    4    5     6
y:   -1.5  -3.5  -3.5  2   7.5  1.5  -2.5
```

The direct convolution and tap-difference formula agree for all seven indices. The output sum is zero, agreeing with sum(s)*sum(h).

## Verification results

| Check | Result |
|---|---|
| Entire original multipart question above each separate solution | PASS |
| Existing premade folder 2 used, -l filenames | PASS |
| Both PNGs exactly 384 pixels wide | PASS |
| Correct full convolution values and seven-sample length | PASS |
| Differentiation explanation, DC cancellation and polarity checked | PASS |
| No overfull boxes, missing glyphs or clipped text/math | PASS |
| Both final PNGs inspected at native 384px width | PASS |
| Original exam/reference inputs unchanged | PASS |
| Previous 41 image/workflow files unchanged | PASS |
| Question 1 definitions preserved exactly | PASS |
| No output directory creation or GitHub upload | PASS |

## Final images

| Part | File | Dimensions | Size |
|---|---|---|---|
| a | [2 410a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2/2 410a-l.png>) | 384 x 1441 | 73735 bytes |
| b | [2 410b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2/2 410b-l.png>) | 384 x 661 | 46279 bytes |

## Source and repeat command

- Authoritative source, preserving Question 1: [2024-10-29_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2024-10-29_compiled_notes.tex>)
- Existing unchanged exporter: [export_notes.py](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/export_notes.py>)

From the repository root:

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2024-10-29 --question 2
```

Both completed parts are discovered and exported in one invocation. Temporary PDFs, wrappers, logs, rasters and validation data are under `tmp/pdfs/signal-export/2024-10-29/Q02/`, outside source and final-image folders.

## Final PNG checksums

- 2 410a-l.png: `7559e9c12386e95c30f5d26ba3edd17e6258a0a807bcf5f003e61615798710a2`
- 2 410b-l.png: `3239e6b06cb612ed155e15b0aee8b9f5831ef17a6d989888680cb7676cbd4217`
