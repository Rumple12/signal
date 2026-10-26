# 2024-10-29, Uppgift 4(a-b): spectrum and sampling notes

**PASS: both parts saved in the existing subject folder `signal calc/4`. Question number 4 and folder number 4 match.**

All work remains local. No output folder was created and no GitHub upload was performed.

## Sources and method

- Original: [2024-10 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/2024-10 exam.pdf>), PDF page 3 / printed page 2, Question 4(a-b).
- Primary for both parts: [4 68.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/4/4 68.jpg>), the user's handwritten 2026-08-18 Question 4 notes. Same plotted spectrum, cutoff and question family; source sampling rate 100 kHz changes to target 50 kHz.
- Preserve the user's order: mirror about zero, repeat every 2pi; read the cutoff, convert normalized frequency to Hz, then double the highest frequency.
- The real-signal magnitude symmetry used in the own notes and reference answer is retained.
- Other own notes in folder 4 were inspected. August 2025 notes 4 58a/b use a different graph and cutoff 7pi/8, so those values were excluded. January 2026 notes 4 61a/b/c concern a different sampling/aliasing variant.
- Secondary check only: [included example-solutions sheet](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2024-10/graded references/Z6EHWWR50000_Grade-B.pdf>), PDF page 2, Question 4. Its printed Hz units omit the kilo factor. Correct units are derived from the target sampling rate below.

## Verified result

- (a) Mirror the given magnitude spectrum about zero and repeat it with period 2pi throughout -2pi < Omega < 2pi. Central copy reaches zero at +/-3pi/4; neighboring copies start at +/-5pi/4.
- Preserve the flat-top shape and sloping sides. The original flat-top knee is not labeled; the solution sketch follows its visual proportions without assigning that knee an exact frequency.
- (b) Omega_max = 3pi/4; f_max = 50000*(3pi/4)/(2pi) = 18750 Hz. Minimum sampling rate = 2*18750 = **37500 Hz**.
- At this ideal limit the copies meet at zero amplitude; no nonzero components overlap.

The original PDF page 3 has the same inconsistent DT056A Visualization running header recorded for Question 3. The dated DT081A cover, actual Question 4 content, graph and example-solutions entry agree. The unrelated running header is not included in the output.

## Final images

| Part | File | Dimensions | Bytes |
|---|---|---|---|
| a | [4 410a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/4/4 410a-l.png>) | 384 x 857 | 53170 |
| b | [4 410b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/4/4 410b-l.png>) | 384 x 957 | 52759 |

## Validation

- Entire original multipart question repeated above each corresponding solution.
- Original spectrum crop checked pixel-for-pixel against the exam PDF.
- Own handwritten method retained; only the sampling rate and derived values adapted.
- Both final PNGs visually inspected at native 384-pixel width, including the extended spectrum sketch and the joined pages of part (b).
- PDF checks passed for complete question text, solution text, figure, page geometry, clipping and missing glyphs.
- All 42 pre-existing calculator files unchanged; previous Question 1-3 definitions preserved exactly.
- Existing output folder names unchanged; no new output folder.
- No missing subparts or unresolved calculations.

## Source and repeat command

- Authoritative source: [2024-10-29_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2024-10-29_compiled_notes.tex>).
- Existing shared exporter reused without changes for this question.

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2024-10-29 --question 4
```

Temporary build files and detailed validation remain under `tmp/pdfs/signal-export/2024-10-29/Q04/`.

## Final PNG checksums

- 4 410a-l.png: `ab0a6d74214c1849552a096f42fa4cd424553a9674bda4e532341f1a4584de59`
- 4 410b-l.png: `9b03ed63b5130c52f3b38c3d86486cff021df6744fa91c7934db609050e2155d`
