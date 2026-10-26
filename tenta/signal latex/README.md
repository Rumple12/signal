# Signal calculator-note export

One authoritative TeX source is kept for each **exact** exam date:
`YYYY-MM-DD_compiled_notes.tex`. `signal_layout.tex` supplies the shared 10pt
article layout: 384pt paper width, 900pt paper height, and 10pt margins.

## Current saving preferences

Keep all changes local. Do not upload or push anything to GitHub unless the user
explicitly authorizes it again.

Save final calculator-note images in the existing numbered folders under
`tenta/signal tenta/signal calc/`, grouped by subject across exam years and
question numbers. Preserve the folders' actual names, including
`1 - random question`. Record the chosen subject folder as `folder_number` in
each `SIGNAL_QUESTION` record; the exporter requires this explicit choice.
Never create an output folder. If the subject destination is unknown or
ambiguous, clarify the destination before exporting.

Keep the actual exam question number in filenames and solution headings.
Explicitly inform the user when it differs from the folder number; the exporter
also includes this notice in listings and validation reports. For example,
2024-10 Question 3 belongs in folder `2` beside the matching feedback
block-diagram notes, with filenames `3 410a-l.png` and `3 410b-l.png`.
Use the short title `<question> <date code><part>-l.png`, adding `-l`
at the end of the image title. The date code is the last year digit followed by
the unpadded month: `61`, `68`, `510`, and so on. Original/reference images keep
their existing names.

For a question without lettered subparts, register `parts: [""]` and an empty
`part` value. Use `\SignalSolution{number}{}{...}` and
`\SignalRender{number}{}`. The image omits the part letter (for example,
`7 410-l.png`), and its headings show the main question and `Solution`.

## Repeat the verified Question 6 export

Run this PowerShell command from the Signal repository root:

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B '.\tenta\signal latex\export_notes.py' --exam 2026-08-18 --question 6
```

There is no separate command for each letter. The exporter discovers all
completed subquestions in the dated source. The same command regenerates:

- `tenta/signal tenta/signal calc/6/6 68a-l.png`
- `tenta/signal tenta/signal calc/6/6 68b-l.png`

Append `--list` to inspect completed and incomplete parts without rendering.
The command is independent of the current working directory if the script is
given by its absolute path.

## What is automatic

1. Select the exact dated source and requested question.
2. Read its `% SIGNAL_EXAM`, `% SIGNAL_QUESTION`, and `% SIGNAL_PART` JSON records.
3. Select **all** completed parts; list missing/incomplete ones explicitly.
4. Require recorded visual source verification and source SHA-256 checksums.
5. Check each registered question figure against a crop of the original PDF.
6. Compile each part from the same source with the entire multipart question.
7. Check that every original question paragraph appears **before** the solution.
8. Check required solution text, embedded figures, page geometry, missing glyphs,
   overflowing boxes, and text/math/image bounds.
9. Render at three times the final resolution, remove unused top/bottom page
   space, and join page bands vertically. Math is not sliced across raster pages.
10. Save a color, 256-entry palette PNG exactly 384 pixels wide. Vertical height
    depends on the solution. The palette keeps the Bayer figure readable while
    reducing file size.
11. Reopen and validate each PNG and confirm the exam/source files did not change.

PDFs, compilation wrappers, logs, raster pages, and the machine validation report
are kept under `tmp/pdfs/signal-export/<exam>/Q<number>/`, outside both the source
and final-image folders. That directory is ignored by Git.

The machine report deliberately leaves `visual_review` as `NEEDS REVIEW`.
Actual-size visual inspection must be performed for each new transcription.
The dated workflow report records the completed inspection for this test.

## Provenance for this test

- Original: `tenta/signal tenta/2026-08/2026-08 exam.pdf`, PDF page 4, printed page 3.
- Approved part (a): `tenta/signal tenta/signal calc/6/6 68a.jpg`.
- Approved part (b): `tenta/signal tenta/signal calc/6/6 68b.jpg`.
- These last two sources are **typed solution images**, not handwritten pages.
  On 2026-10-25 the user explicitly said: **Use the existing typed solutions**.
- The genuine handwritten match is
  `tenta/signal tenta/exaam/exaam/IMG_20261024_155408.jpg`, with its duplicated
  crop `tenta/signal tenta/2026-08/6 68 f.png`. It contains a short unfinished
  reminder and no completed solution for either part. Its crossed-out search
  keyword is unclear and is recorded as an uncertainty comment in the TeX.
- `tenta/signal tenta/2026-08/6 68.jpg` concerns compression and is excluded.
  January 2026 and August 2025 material on the same handwritten sheet is also
  excluded from this exact-date question.

The original question was transcribed verbatim, including both parts, the hint,
and both `(2p)` allocations. The original Bayer diagram and legend are included
as a lossless crop. The typed solutions retain their method, order, values,
examples and final answers; repeated summaries are consolidated. The arithmetic
steps `460/4` and `340/4` are directly implied by the supplied averages.

## Add another verified question later

The exporter is reusable; transcription and content verification remain explicit.
It does not claim automatic handwriting recognition or manufacture a solution.

1. Locate the exact exam and inspect all relevant question/solution pages.
2. Inspect the user's existing notes to choose the matching subject folder and
   record its `folder_number` in `SIGNAL_QUESTION`. Add the original question
   once with `\SignalQuestion{number}{...}` and register
   its complete original wording in `required_question_text`. Put essential
   diagram crops in `assets/` and register their PDF page/image index/crop box.
3. Add each solution with `\SignalSolution{number}{letter}{...}`. Preserve its
   method, corrections, order, numerical values, and cross-page references.
4. Record its actual source path, checksum, provenance (`handwritten` or expressly
   `user-approved-typed`), and `content_verified`. Do not mark a part complete if
   its source is missing or its mathematics is unresolved.
5. Mark additional reasoning with `\textbf{English clarification:}`. Record
   unreadable or inconsistent content in an uncertainty comment and the report.
6. Mark completed parts `status: complete`; leave other parts `status: incomplete`.
7. Run the exporter once with `--exam YYYY-MM-DD --question number` and inspect
   all generated PNGs at 384px width.

Exit codes: `0` means the selected completed parts rendered and passed machine
checks; `2` means no completed parts exist; `1` means a source/build/validation
error. A report containing incomplete parts is `NEEDS REVIEW`, even if the
available completed parts rendered successfully.

Only **2026-08-18, Question 6** was export-tested in this workflow test. No other
exam dates or questions were batch-exported. The previously completed Question
2(b) was preserved in the authoritative dated source. The older month-only TeX
and build command now delegate to it and contain no independent question copy.
