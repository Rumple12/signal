# Signal calculator notes: failure review and recovery plan

Report date: 2026-10-27

## 1. What went wrong

The user reports that the Signal LaTeX material failed to support them in the test. The intended product was a set of understandable worked exam answers: simple English, all necessary calculations, and a method that could be followed without already knowing the solution.

Some Signal answers instead became technical discussions of the problem. They contained correct calculations or legitimate qualifications, but required too much interpretation from the person using them. A mathematically defensible answer can still be a poor learning aid and a poor reference under exam pressure.

The assistant is responsible for this drift. The user repeatedly requested simple, complete, beginner-friendly work. The instructions did not require advanced exposition, compressed reasoning, or extensive discussion of every possible interpretation.

This report separates three findings:

- **Reported outcome:** the material did not meet the user's needs in the test.
- **Observed failure:** representative Signal notes do not consistently match the teaching style of the statistics notes.
- **Not established by this review:** that every Signal answer is mathematically wrong, or that the notes alone explain the test outcome. This was a comparative style and usability review, not a complete mathematical re-audit of every answer.

## 2. The reference that shows what was wanted

The statistics notes demonstrate that the requirement was never simply "use fewer words."

The reviewed examples include:

- [Three-set probability](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/calcu formats/7 stat/stat calcu/1 ABC set theory/51a triple-set.jpg>).
- [Finding a density's constant](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/calcu formats/7 stat/stat calcu/2 cdf, pdf/61a tathet-a.jpg>).
- [Expected value and standard deviation](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/calcu formats/7 stat/stat calcu/2 cdf, pdf/61d EX-0.2bound.jpg>).
- [Maximum-likelihood estimation](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/calcu formats/7 stat/stat calcu/4 ML.summ,theta/58 ML theta GOODte.jpg>).

These notes explain the route before following it. They identify the useful information, state the relevant rule, substitute the actual values, and expose intermediate algebra. Short instructions such as "Expand," "Integrate," and "Plug in the bounds" tell the learner what happens next.

The maximum-likelihood notes also explain the particular rules needed at the point of use: how products become powers, how logarithms change products into sums, and which variable is being differentiated. Their annotations address likely sticking points directly.

Several statistics images are longer than the Signal examples. The reviewed maximum-likelihood image is 1,756 pixels tall; the Signal example Q2(b) image is 772 pixels tall. Height and word count therefore do not explain the difference. The statistics material spends its space helping the reader perform the work.

## 3. Where the Signal material drifted

| Area | Statistics reference | Observed Signal drift |
|---|---|---|
| Orientation | Explains the goal and useful givens | Some answers begin reasoning before establishing a clear route |
| Working | Shows the next operation and its result | Some explanations use technical vocabulary as shorthand |
| Scope | Follows the calculation needed for the answer | Alternative interpretations can become a substantial part of the answer |
| Terminology | Explains the needed rule where it is used | Terms such as ROC and left-sided response appear without enough beginner-level preparation |
| Practical use | Helps the reader reproduce the method | Some answers require the reader to select or interpret the method first |

### Concrete examples

**Example Q3(ii), pole-zero diagram.** The [current image](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/9. exempl tenta/example_Q03_ii-l.png>) moves from poles to growing exponentials, absolute integrability, regions of convergence and left-sided realizations. The missing ROC is a genuine qualification. However, the main explanation should first make the practical test easy to follow: identify the crosses, locate them relative to the imaginary axis, state the causal assumption, and explain the stability conclusion. The qualification should be clearly separated and proportionate.

**Example Q2(b), sampled spectrum.** The [current image](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/9. exempl tenta/example_Q02_b-l.png>) includes general indexing, a phase column, spectral normalization and a schematic whose spacing is not numerical. These details were qualified, but the practical task of placing the original lines and repeating them should have been easier to extract. Because the sampling rate is unspecified, an exact numerical frequency axis cannot be supplied without an assumption. That limitation must remain visible; invented numbers would not fix the teaching problem.

**August 2026 Q3(b), output samples.** This [answer](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/3 y(n) x(n) (electro map func)/latex/3 68b-l.png>) is much closer to the statistics reference: initial values, input samples, successive substitutions and final outputs are visible. This shows that the drift is uneven. Useful work should be retained rather than rewriting everything indiscriminately.

## 4. How the process allowed it

1. **Completeness was interpreted too broadly.** Necessary explanation expanded into coverage of technical possibilities. The main answer lost prominence.
2. **Useful teaching structure was removed along with repetition.** Short orientation and given-information sections can help a beginner. Removing them did not make the remaining terminology easier.
3. **Correctness was confused with usability.** Numerical checks, faithful question reproduction, 384px width and unclipped rendering are valuable. They do not establish that a student can understand and reproduce the method.
4. **Style assurances were too broad.** The assistant said the recent notes followed the intended style without establishing a concrete, representative comparison with the statistics material.
5. **Batch completion magnified the problem.** Producing an entire exam efficiently repeated the writing approach before its usefulness had been tested against a concrete reference.
6. **Completion labels were insufficiently specific.** Some example-exam answers were explicitly conditional because the PDF was ambiguous. A broad PASS or completion message can still make technically checked, conditional material look fully resolved. Source uncertainty, mathematical checking and learning usability need separate statuses.

The user had already given the relevant instructions. The failure was inconsistent execution and inadequate review of the resulting teaching material.

## 5. What should be preserved

Keep the original questions and figures, the user's handwritten methods, verified calculations, the narrow LaTeX layout, separate 384px images, existing subject folders, the source index and unchanged-output caching.

Do not remove genuine assumptions to make an answer sound more confident. Do not replace correct handwritten methods with a different method merely to simplify presentation. Do not shorten answers by deleting necessary algebra.

The recovery should improve the explanation while preserving these working parts.

## 6. The corrected writing standard

Use the actual statistics examples above as the reference, rather than relying only on adjectives such as "simple" or "complete."

For a calculation answer, use this structure where it helps:

1. **What we are doing:** state the requested result and the route in one or two plain sentences.
2. **Given information:** identify the values, initial conditions or graph readings actually needed.
3. **Worked steps:** state the relevant formula, insert the current question's values, show every meaningful operation, and explain why a non-obvious move is allowed.
4. **Final answer:** make the result easy to locate, with units or the required classification.
5. **What to remember:** include one useful reusable rule only when it helps solve the next similar question.

For theory answers, give the requested conclusion and a direct justification. Explain necessary terminology where it appears. A short theory question does not need an artificial sequence of calculations.

For graph answers, show how to read the original, identify the necessary anchor points, and construct the required plot. Distinguish exact coordinates from schematic spacing. Keep genuinely unspecified parameters symbolic unless an explicit assumption is authorized.

Use one main solving route. If an assumption changes the answer, state it before the affected calculation. Keep secondary cases in a short, clearly labelled note. Where the source prevents a unique answer, say exactly what is unresolved instead of silently choosing an interpretation.

## 7. Recovery plan

**First, establish a working reference.** Rewrite one complete question containing both explanation and calculation, such as example Q1(a-b), against the statistics examples. Compare the resulting 384px images side by side. Establish the writing standard on this concrete result before applying it across the collection.

**Next, triage the indexed material.** Classify answers as retain, clarify, rewrite or mathematically recheck. Prioritize the difficult theory and graph answers. Preserve answers already close to the intended style, including the useful structure in August Q3(b). Do not search the whole repository again or regenerate unchanged questions.

**Then, recover one complete question at a time.** Keep its handwritten method and verified values. Repair the explanation, compile once, export all affected parts and inspect the changed images. The current report does not authorize or perform those rewrites.

**Keep mathematical review separate.** A readability rewrite must not silently change a sign, coefficient, boundary convention, transform normalization, initial condition or final answer. Any proposed mathematical correction needs an explicit explanation and verification.

**Track source ambiguity separately.** For example Q3, retain clear records of the single-trace limitation, missing ROC, unspecified impulse-response support and unclear crossed-out derivative. A conditional interpretation must remain distinguishable from an unconditionally resolved answer.

## 8. Acceptance checks that would prevent a repeat

An answer is ready only when all three checks pass:

- **Source and mathematics:** the exact question is represented, sources are identified honestly, the method matches the relevant handwriting, and the calculations are verified.
- **Teaching:** a beginner can identify the rule, locate the needed values, follow each meaningful transition and reproduce the result without guessing a missing step. Unexplained terminology or a buried main answer fails this check.
- **Calculator use:** the answer is readable at native 384px width, symbols and units remain clear, the result is easy to find, and nothing is clipped. No fixed height limit should force useful working out of the image.

A practical review should ask: "What would I do next using this note?" The answer should be evident at each stage. Compilation success and correct final numbers cannot substitute for that check.

## 9. Status of this report

This is an assessment and recovery plan. Only this report was created. No exam LaTeX, calculator image, exporter or AGENTS.md instruction was changed during this reporting task. Nothing was uploaded to GitHub.
