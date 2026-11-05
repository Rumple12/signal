# Obid — DT081A Lab 2: Codex Workflow

**Status:** Project instructions, not a finished lab report.  
**Location in repository:** `labbs/obid/lab2/`  
**Primary authority:** Mårten's `DT081A Signal and Image Processing - Lab 2` assignment and the course report template.

## Goal and page budget

Create an independent, technically correct Lab 2 report for Jakob Obid, **aiming for 5–7 readable pages**. Seven pages is a target, **not** permission to omit a required teacher question, result, plot, or code. Prefer fewer, informative multi-panel figures over redundant figures. Keep scientific text short, but do not make plots unreadable or shrink fonts excessively.

Target layout, adaptable after the user visually checks the PDF:

| Report part | Space guide | Evidence to include |
|---|---|---|
| Introduction + Experimental Setup + Sec. 1 | ~1 page | time signal + full and positive-frequency FFT in one figure |
| Secs. 2–3 | ~1–1.5 pages | window comparison + System 1 and System 2 impulse responses |
| Secs. 4–5 | ~1–1.5 pages | amplitude/phase spectra and system response |
| Sec. 6 | ~1–1.5 pages | LP/HP and filter-order/cutoff comparisons, plus BP/BS code |
| Sec. 7 | ~1 page | Obid's own voice spectrogram(s) + small k comparison |
| Discussion, Conclusion, short Appendix | ~0.5–1 page | brief findings and essential code only |

**Expected:** around 7 pages may be realistic; **5 pages is ambitious**. Do not try to copy another student's page layout.

## Who does what

**GPT in the chat:** Reads the teacher's section, prepares mathematical reasoning, specific experimental parameters, plain-English answers, small tables and figure instructions. **Treat those as a draft to assemble, not as measurements unless verified against actual output.**

**Codex:** Implement the named section, run the script **once if needed to generate its figures or collect measurements**, insert the supplied prose and verified values into the LaTeX source, and stop. Work on only the requested section.

**User:** Compile LaTeX to PDF in **TeXstudio**; visually inspect the PDF with GPT; handle Git commit/push (with Grok); apply final spacing changes.

**Do not use Codex for:** PDF builds, page rendering, visual review, screenshots, Git commits, Git push, unrelated research, broad refactors, unnecessary validation or long explanations. If the editor *requires* a compilation check, do only that required check; do not export or inspect a PDF for this task.

## Writing — compulsory

Read `SIMPLE_WRITING_STYLE.txt` before touching report prose.

- Natural, very simple university-student English, as in Obid's approved Lab 1.
- An **individual report**: use "I" when Obid describes actions he actually performed; neutral language for facts. Never use "we/our" to imply collaboration.
- Under Results and Analysis, use the teacher question (or a faithful shortened heading only if needed for space), followed by **Answer:** and usually 1–4 short sentences.
- Explain what was done, what happened, and why it matters. Use actual numbers and units when available.
- No padded theory, fake measurements, copied conclusions, formal jargon, generic AI-sounding prose or repeated arguments.
- Keep the template sections: Introduction; Experimental Setup; Results and Analysis with Sections 1–7; Discussion; Conclusion; selected Appendix code.

## Independence

Use the teacher's assignment, teacher starter code, and Obid's own experiments. Yacoub's completed report is **not a source for Obid's answers, figures, code or experimental measurements**. Matching mathematical results for teacher-fixed signals are expected. Do not cosmetically modify someone else's figures or text to simulate independent work. Obid's voice recording must be his own.

## Teacher-specific technical cautions

1. **Sections 1 and 4:** `fs=250 Hz`, `t=np.arange(0,0.6,1/fs)` gives **150 samples**, bin spacing **1.6667 Hz**. The signals have frequencies **50, 55, 120 Hz**, amplitudes **1, 0.1, 0.3**, and phases **0, pi/4, pi/2**. Preserve these constants.
2. **Section 2 typo:** prose says **0.4 seconds**, but the teacher's provided time vector uses **0.6 seconds**. Preserve the runnable starter code's **0.6 s** and mention the inconsistency if relevant; do not silently change sampling duration.
3. **Section 3.1:** `h=[1,0.5,0.3,0.1,-0.1,-0.4,-0.2,0.1]`. This is FIR. The teacher's old `plt.stem(..., use_line_collection=True)` may not work with newer Matplotlib; omit the obsolete argument if necessary.
4. **Section 3.2:** The printed difference equation repeats `y(n-1)` in the last term, but the provided `a=[1,0.6,-0.35]` with `lfilter` corresponds to **`y[n]=x[n]+0.3x[n-1]-0.6y[n-1]+0.35y[n-2]`**. Flag this source inconsistency in the work; implement the recurrence consistent with the provided filter coefficients and compare identical impulse lengths. The question also mentions both `len(x)` and **100 samples**; use 100 for the explicitly requested iterative 100-sample comparison and keep dimensions consistent.
5. **Section 5:** Use **System 2** and demonstrate `Y(f)=H(f)X(f)`; compare theoretical response and finite-length estimates carefully because filter startup can cause small differences.
6. **Section 6:** Design **Butterworth and Chebyshev Type I**, both **LP and HP**, and vary cutoffs/orders. Include the required **BP and BS Python design code**. Teacher's example uses **`fs1=2500 Hz, fc=200 Hz, order N=5, ripple Rp=3 dB`**. **Do not reuse an FFT frequency axis computed for `fs=250` with filters designed at `fs1=2500`**. Use the actual filter sampling frequency for axes and frequency response.
7. **Section 7:** Requires **Obid's own recording saying his own name**, in WAV format. Compare at least two or three window sizes `k` (e.g., 512/1024/2048), explain time/frequency resolution, and cautiously identify broad syllables or sound regions. **Do not invent a voice file or claim a particular letter is visible without evidence.** If the voice file is missing, state what is blocked and stop just that part.

## Figures and LaTeX

- Favor roughly **7–9 compact multi-panel figures total**, adjusted only to support required questions. Avoid repetition of the same spectrum if a shared figure can clearly answer two questions.
- Labels, units, normalizations, frequency ranges, legends and captions must be accurate. Do not crop away the evidence required for interpretation.
- Place each figure near the question it answers; use reasonable `\Needspace` if needed. Avoid mandatory `\clearpage` before each section.
- Follow the course report template. The report should not require a decorative title-only page.
- No page-limit tricks: do not hide text in tiny font, squeeze axes, or change margins unreasonably.

## File layout

```text
labbs/obid/lab2/
├── AGENTS.md
├── README_FOR_CODEX.md
├── SIMPLE_WRITING_STYLE.txt
├── code/                    # One or a few straightforward Python scripts
├── figures/                 # Figures created by Obid's code
├── audio/                   # Obid's own voice WAV (when supplied)
└── report/
    └── main.tex             # The user compiles this in TeXstudio
```

## Tiny checklist at the end of each section

1. Did I implement **only** this teacher section?
2. Are every requested part, result, and figure represented?
3. Is each reported measurement backed by actual code output?
4. Are previous approved sections unchanged?
5. Did I avoid PDF compile, PDF visual review, and Git changes?

**Response to user:** A few lines: files created/updated, figures generated, actual measured results if any, and blockers. No extensive write-up.
