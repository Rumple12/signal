# 2024-10-29, Uppgift 3(a-b): own-note adaptation report

**PASS: both parts saved in the existing signal calc/2 folder by subject. The user's own cross-year notes are the primary sources.**

All work remains local. No output folder was created, and no GitHub upload was performed. Questions 1 and 2 and their existing images remain unchanged.

**Question/folder mismatch: the exam question is 3; the subject folder is 2.** Both images were moved from folder 3 to folder 2 beside the matching block-diagram notes. Filenames retain the original question number. PNG content and checksums are unchanged. The registry now explicitly records `folder_number: 2`; future exports report the mismatch and use this destination.

## Verified source mapping

| Target | Part | Original question | Primary own-note source | Origin |
|---|---|---|---|---|
| 2024-10-29, Uppgift 3 | a | [Original exam, PDF page 3 / printed page 2](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/2024-10 exam.pdf>) | [2 68a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2/2 68a.jpg>) | 2026-08-18, Uppgift 2(a) |
| 2024-10-29, Uppgift 3 | b | Same original question and diagram | [2 68b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2/2 68b.jpg>) | 2026-08-18, Uppgift 2(b) |

The actual diagrams and tasks match: the same delay chains, tapped input branches, feedback branches, gains and output summation layout. The match was established by content rather than the main question number. Existing 3 68a/b/c notes were inspected first; they concern a different supplied recurrence/input/spectrum question and were not substituted for this block-diagram family.

Your original method is retained:

1. Read T as one sample of delay; gains multiply and sums combine.
2. Collect the input contribution as one group.
3. Collect the returned output contribution as the feedback group.
4. Add the two groups at y(n).
5. Move feedback terms to the left to collect the output terms.
6. Identify IIR from the delayed return paths, following the own-note explanation.

## Exact value adaptation

| Branch | Delay | Own-note gain (2026) | Target gain (2024) |
|---|---|---|---|
| Input | 0 | 1 | 1 |
| Input | 1 | 2 | 2 |
| Input | 3 | 1 | 1 |
| Feedback | 1 | +0.3 | -3 |
| Feedback | 3 | -0.1 | +2 |

The second delay in each chain has no tap entering a sum, so no x(n-2) or y(n-2) contribution is invented. Both changed feedback signs are taken from the actual 2024 diagram.

## Verified results

- Part (a): IIR, because the target system uses delayed previous outputs through feedback; no stability assumption is added.
- Input group: x(n) + 2x(n-1) + x(n-3).
- Feedback group: -3y(n-1) + 2y(n-3).
- Output equation: y(n) = x(n) + 2x(n-1) + x(n-3) - 3y(n-1) + 2y(n-3).
- Collected form: y(n) + 3y(n-1) - 2y(n-3) = x(n) + 2x(n-1) + x(n-3).

Group combination and sign collection were checked independently using exact arithmetic. The numerator 1+2D+D^3 and denominator 1+3D-2D^3 are equally sized and not proportional, so their quotient is not a finite polynomial; this independently verifies IIR. This check is not substituted for your original feedback-based explanation in the calculator image.

## Secondary reference and source inconsistency

The included example-solutions sheet in [Z6EHWWR50000_Grade-B.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/graded references/Z6EHWWR50000_Grade-B.pdf>), PDF page 2, Question 3 was used only to cross-check the target signs and result. It was not used as the primary solving method.

The original PDF page 3 has an inconsistent running header reading DT056A Visualization. The dated DT081A cover/first question page and the actual Q3 question, diagram and coefficients match the accompanying DT081A example-solutions entry. The inconsistency is recorded in the TeX comments; that unrelated page header is not included as part of Question 3. No unresolved diagram coefficient or solution uncertainty remains.

The own-note aside that previous exams never show FIR is not generalized or presented as a mathematical rule.

## Verification

| Check | Result |
|---|---|
| Entire original question, both parts and point allocations repeated | PASS |
| Readable original block-diagram crop present above each solution | PASS |
| Crop checked against the original PDF image, not redrawn with old gains | PASS |
| Own cross-year notes prioritized over graded reference answers | PASS |
| Input/feedback grouping and original solving order retained | PASS |
| Target gains -3 and +2 and both collected signs verified | PASS |
| Both PNGs exactly 384 pixels wide, inspected at actual size | PASS |
| No overfull boxes, missing glyphs or clipped text/math/diagram | PASS |
| Questions 1 and 2 definitions preserved exactly | PASS |
| Existing 43 image/workflow files unchanged | PASS |
| Existing output folders unchanged; no new folder created | PASS |
| No GitHub upload | PASS |

## Final images

| Part | File | Dimensions | Bytes |
|---|---|---|---|
| a | [3 410a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2/3 410a-l.png>) | 384 x 631 | 55356 |
| b | [3 410b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2/3 410b-l.png>) | 384 x 1001 | 73415 |

## Source and repeat command

- Authoritative source: [2024-10-29_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2024-10-29_compiled_notes.tex>)
- Shared converter with explicit subject-folder routing: [export_notes.py](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/export_notes.py>)

From the repository root:

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2024-10-29 --question 3
```

Both completed parts are discovered in one invocation. Temporary PDFs, wrappers, logs, raster pages and validation data are in `tmp/pdfs/signal-export/2024-10-29/Q03/`, outside source/final-image folders.

## Final PNG checksums

- 3 410a-l.png: `035c8ad17b12ffbef4e62e9f86ca23995dfb2832f3ef3a4feee1b435ccf63293`
- 3 410b-l.png: `f9f4c93748691370ee478e9ffb74e189be8736e750b928594b307260ddf1252a`
