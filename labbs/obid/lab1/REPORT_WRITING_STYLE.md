# Obid — Report Writing Style Guide

**Project:** DT081A Signal and Image Processing, Labs 1–3  
**Applies to:** Obid's report text, Q&A answers, introductions, experimental setup, discussion, conclusion, figure captions, table descriptions, and code explanations.  
**Reference tone:** The already approved `DT081A_Lab1_Report_Jakob_Obid.pdf`, especially Section 3.1 (Signal Generation and Visualization). This guide describes its style. It does not authorize copying other students' work.

## 1. Voice: a normal, competent university student

Write in **clear, natural, easy-to-understand English**. Imagine Obid explaining his work to another university student who knows the course basics.

- Straightforward, calm, professional, and not excessively formal.
- Use familiar words and short to medium-length sentences.
- Keep one main point per sentence when possible.
- Explain **what was done, what happened, and why**, in that order when helpful.
- Use the necessary technical term rather than an imprecise substitute, but explain difficult concepts simply.
- Sound like a student who understands the work, not a lecturer, a sales pitch, or a PhD paper.

The language should be simple, but the analysis must still be correct.

## 2. Exact Q&A structure to preserve

For each teacher question under `Results and Analysis`:

**Q1. [Teacher's exact question]**

**Answer:** [Direct answer based on Obid's experiment. Usually 1–4 short sentences. Longer only if needed for accuracy.] [Brief figure reference if useful.]

Use Q1, Q2, etc. **within each subsection**, matching the approved Lab 1 Section 1.1 format. Keep the teacher's exact question wording (correct only obvious PDF formatting breaks). Do not paraphrase the assignment question as if it were Obid's writing.

When the answer needs a calculation, show the relevant values and units. When a figure is expressly requested or materially supports the answer, place it close to the answer. A question with a clear textual answer does not automatically need a diagram.

## 3. Real examples from Obid's approved Section 1.1 PDF

**Q2 answer style:**

> The 20 Hz sine has 20 cycles in one second instead of 10. The waves are closer together in time. The amplitude stays the same (Figure 2).

Why it works: three simple statements — result, visible effect, what stayed unchanged.

**Q4 answer style:**

> The original 10 Hz sine was added to the 5 Hz square. The sine gives the curved parts, and the square gives sudden jumps. The sampled values range from about −2 to +2 (Figure 3).

Why it works: method, interpretation, measured behavior. No unrelated background.

**Q5 answer style:**

> A square wave can act as a clock signal in a digital circuit. Its regular changes tell parts of the circuit when to act. Its frequency tells us how often these changes repeat.

Why it works: one concrete application, explained naturally in three sentences.

The Q3 answer is longer because it distinguishes positive, negative, and exact-zero input values and checks a special case. **Accuracy takes priority over an arbitrary word limit.**

These examples illustrate the approved voice; do not repeat them as filler in later sections.

## 4. Preferred writing choices

| Instead of... | Write... |
| --- | --- |
| "The methodological framework facilitated an assessment..." | "We used the same method to compare the results." |
| "The frequency-domain representation exhibited..." | "The FFT showed..." |
| "A substantial increase was observed..." | "The value increased..." |
| "This phenomenon can be attributed to..." | "This happened because..." |
| "Furthermore, it is important to note that..." | State the relevant fact directly, or remove the sentence. |
| "The experimental results demonstrate the efficacy of..." | "The results show that..." |
| "The signal underwent a transformation..." | "The signal was changed..." |

These are examples, not mandatory phrases. Do not overuse "This happened because" or "The results show".

## 5. Paragraph and sentence length

- Most single-part questions: **2–4 short sentences**.
- A simple definition, observation, or real-world example: **1–3 sentences** if enough.
- A multi-part question: answer **every part**, even if it needs more sentences.
- Introduction: one compact paragraph about the lab's purpose.
- Experimental Setup: one compact paragraph with tools, data, and settings; expand only when necessary.
- Discussion: connect the most important findings, trade-offs, and genuinely relevant limitations.
- Conclusion: short, specific summary of what the experiments established; do not re-list every answer.
- Captions: identify what is shown, with relevant units/parameters; avoid long analysis in captions.

No strict word count. **Complete and accurate is more important than artificially brief.**

## 6. Avoid AI-like or overengineered writing

Avoid:

- Inflated, self-congratulatory, generic, or overly polished prose.
- Unnecessary phrases such as "Moreover," "Furthermore," "It is important to note that," and "In conclusion, this comprehensive investigation...".
- Repeating the same point in the answer, figure caption, discussion, and conclusion.
- Long chains of abstract nouns; sentences that take more than one reading to understand.
- Overly defensive statements about tests not performed. **But disclose real limitations when they affect the answer's validity.**
- Technical explanations longer than the teacher's task requires.
- Invented explanations, measurements, screenshots, figures, observations, or citations.
- Writing different words merely to disguise similarity. Independently understand and report the experiment.

Do **not** sacrifice correctness or omit requested theory, methods, or data to make the text shorter.

## 7. Numbers, graphs, and evidence

- Use Obid's own executed code and output for all observed values. Recalculate when inputs or parameters change.
- Keep correct units: Hz, s, dB, pixels, etc.
- Distinguish theoretical expectations from measured results; do not present predictions as measurements.
- If the teacher fixes values, identical correct results across students are expected. Never force different numbers.
- Use brief references such as `(Figure 2)` where helpful, as in Section 1.1.
- Put figures next to the question they answer and make axes readable and scientifically correct.
- Explain *what the plot shows*, not every plotting command.
- Include short code excerpts only when they help a reader understand how a requested operation was implemented.
- Cite outside sources when information comes from outside the assignment and experiment.

## 8. Independence and consistency

- The teacher's assignment and starter code are the primary references.
- Obid's completed, reviewed sections set the writing voice and format for future sections.
- Do not import, reuse, lightly paraphrase, or cosmetically alter Yacoub's report text, diagrams, code, or measured results.
- Do not change approved Obid text simply to make it sound more academic or different. Preserve it unless there is a factual error, a teacher requirement to fix, or an explicit user edit request.
- Keep the separate Obid directory and avoid editing other lab reports.
- If the teacher's instructions and a draft conflict, **follow the teacher** and point out the difference.

## 9. Review checklist before finalizing each Codex section

1. Does each required question appear, with a direct answer immediately below it?
2. Does every answer use language similar in simplicity and tone to Obid's approved Section 1.1?
3. Are all claims supported by Obid's code, outputs, figures, or clearly identified theoretical reasoning?
4. Are the numbers, frequency bins, units, special cases, and figure references correct?
5. Does each figure directly help answer a teacher question? Can unnecessary figures be removed?
6. Is there any jargon, filler, repetition, robotic transition, or unsupported claim to delete?
7. Are the existing approved report sections unchanged unless editing them was requested?
8. Was the PDF compiled and visually checked, including figure labels and any page overflow?

**Final test:** "Would a normal university student naturally write this, and would another student understand it on the first read?" If not, simplify without losing accuracy.

**Writing standard:** Natural. Clear. Readable. Straightforward. Academically correct without sounding artificially academic.
