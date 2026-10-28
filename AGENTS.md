# Local Signal calculator-note preferences

- Keep work local. Do not upload, push, or publish anything to GitHub unless the
  user explicitly gives a new instruction authorizing it. This supersedes older
  requests to keep the repository synchronized with GitHub.
- Save generated calculator-note images in the PREMADE numbered folders under
  `tenta/signal tenta/signal calc/`. Preserve their actual names, including
  descriptions. The existing first folder is `1 - random question`.
  Do not create a new `1` folder or any other output folder.
- Choose the existing destination by SUBJECT, using matching notes across years
  and question numbers. Keep the same subject in the same folder even when the
  actual exam question number differs. Preserve the actual exam question number
  in filenames and solution headings, and explicitly tell the user whenever it
  differs from the destination folder number. For example, 2024-10 Question 3
  belongs in folder 2 with the matching feedback block-diagram notes; its images
  remain named `3 410a-l.png` and `3 410b-l.png`.
- Record the chosen subject folder as `folder_number` in the question registry.
  Resolve that existing folder by its leading number. If no suitable subject
  folder is established or multiple folders match, clarify instead of creating
  one or choosing solely by the exam question number.
- Use the existing short image-title style, with `-l` immediately before
  the image extension. For example, Question 6(a) from August 2026 is
  `tenta/signal tenta/signal calc/6/6 68a-l.png`.
- The date code is the last digit of the year followed by the unpadded month:
  January 2026 is `61`, August 2026 is `68`, and October 2025 is `510`.
- Preserve existing original/reference images. Generated LaTeX images use their
  own `-l` filenames.
- Keep the authoritative exam TeX sources in `tenta/signal latex/` and temporary
  build files outside both the source and final-image folders.
- One complete main question (Uppgift) is the unit of work. Given an exam date
  and question number, locate and verify all available subquestion sources,
  update the single dated TeX source, and export every completed part without
  requiring separate prompts for its letters. Repeat the entire original
  multipart question above each solution. Report missing sources explicitly.
- Source priority: first inspect the user's own handwritten solution material in
  the existing `signal calc` folders, then search the raw notes under
  `tenta/signal tenta/`. Match by the actual question family across exam years
  and question numbers, not just the target date or folder number. Finding a
  cross-year match does not authorize reusing it: obtain an explicit user request
  before copying another year's solution, and record the source exam/date.
- Do not force a match just because two problems share a question number:
  feedback block-diagram derivations and finite-sequence convolution questions
  are different families, though grouping weighted/delayed terms may transfer.
- When corresponding personal handwriting exists, use only that handwriting as
  the solution source. Do not supplement it with graded answers or another
  year's solution. Identify any explicitly authorized reference material honestly.
- For comparison-only requests, compare the existing work without rewriting
  its LaTeX solution content or regenerating its calculator images.

## Permanent simplified-solution rules for all DT081A exam questions

These rules override earlier instructions encouraging expanded examples, long
explanations, extra theory, or automatic reuse of cross-year/reference solutions.
Priority: the user's handwritten notes -> faithful transcription -> simple
explanations -> complete exam answer.

- If corresponding handwritten notes exist, transcribe and clarify the user's
  work; do not replace it with a new solution. Preserve the exact method, order
  of reasoning, calculation steps, formulas, term grouping, and final answers.
  Clean up handwriting, make the English readable, and merge repeated material.
  Fill only small, necessary missing steps. Do not add new methods, examples,
  formulas, calculations, or unnecessary theory. Flag errors and uncertainties
  explicitly instead of silently changing the method or answer.
- Do not copy another year's solution without an explicit user request, even
  when the question is similar. Report which handwritten notes were found and
  actually used, including their exam/date. Report missing sources honestly.
- If no corresponding handwritten notes exist, solve the question using the
  simplest correct method. Explain every necessary step in plain English and
  show the calculations required to reach the answer. Do not skip essential
  steps, use advanced methods when simpler ones work, invent numerical examples,
  or add unrelated theory. Keep the established straightforward step-by-step
  Signal style, short but sufficient for a complete exam answer.
- State what must be found, explain the simplest method, show only necessary
  calculations or reasoning, and give the final answer. For theory questions,
  use short direct explanations instead of unnecessary derivations. Include
  equations only when needed or present in the user's notes. Simple must remain
  complete: include what is required for full marks and nothing irrelevant.
- Keep the existing calculator workflow: preserve the complete original question
  and its figures above the solution, use the existing narrow LaTeX formatting,
  update only the requested question in its dated authoritative TeX source, and
  regenerate its corresponding 384px-wide image in the existing subject folder.
  Preserve every other question and original/reference file. Visually verify
  that no text, figures, or equations are clipped. Confirm the updated TeX and
  image in the completion report. Keep all work local unless newly authorized.

## Critical rule: simple but fully step-by-step

Apply this rule to every future DT081A exam solution. Simple language must never
mean short or incomplete reasoning. Within the handwritten-source and faithful-
transcription rules above, prioritize complete steps -> clear reasoning -> simple
English -> no unnecessary content. This overrides any preference for brevity
that would remove steps needed for understanding.

- Assume the reader is learning the subject for the first time. Explain necessary
  mathematical symbols and use easy English.
- For each meaningful calculation step, explain what is being calculated, briefly
  why it is needed, show how through the formula, substitution and calculation,
  and clearly state the result before continuing. Present these naturally;
  separate What/Why/How/Result headings are not required.
- Show one mathematical operation at a time where needed for understanding.
  Never jump from a formula to a final answer when meaningful intermediate
  algebra or reasoning is missing. Do not shorten at the expense of understanding.
- When following handwritten notes, preserve the user's method and step order.
  Make necessary intermediate substitutions and algebra explicit without adding
  another method, unrelated formulas, invented examples or extra theory. Continue
  to flag errors and uncertain handwriting explicitly.
- For theory questions, explain every necessary concept clearly and directly,
  without forcing a calculation template or adding irrelevant theory.
- Keep solutions detailed in their steps and simple in their language. Avoid
  lengthy introductions and repeated explanations of obvious arithmetic.

## Efficient one-question workflow

- Look up the exact exam/question in `tenta/signal latex/source_index.json` first.
  Use its PDF page, personal-note paths and subject folder. Extend only missing
  entries; search narrowly only when an indexed source is missing or ambiguous.
- Reuse the dated TeX source, shared layout and exporter. Edit only the requested
  question. One invocation exports all its completed parts in a single compile;
  unchanged parts/images are skipped using verified content fingerprints.
- Preserve handwritten methods, every necessary calculation step, the full
  original multipart question above each answer, and separate 384px images.
  Check mathematics, question/figure fidelity, width and clipping. Visually
  inspect only new or changed images; never rebuild completed questions merely
  to review them or profile performance.
- Avoid repository-wide repeated searches/hashing, unrelated source reviews,
  unnecessary tool changes, extra reports and duplicate files. Keep evidence and
  timings in the exporter's existing validation report; add files only when
  required by the exporter, source index or original-question figures.
- Measure source discovery, transcription/solution, TeX updating, compile/export
  and verification. Separate one-time optimization setup from normal run time.
  Keep progress brief; report optimization changes and genuine uncertainties or
  remaining bottlenecks. All work stays local unless newly authorized.
