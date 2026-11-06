# Obid — DT081A Lab 3: Codex Working Instructions

**Location:** `labbs/obid/lab3/`  
**Status:** SETUP ONLY. Do not implement experiments until GPT supplies the named section's ready-made calculations, answers and figure instructions.  
**Primary source:** `DT081A Signal and Image Processing - Lab 3` **version 1.1**, plus the official DT081A report template.

## Goal and length

Write Jakob Obid's own, technically accurate, individual Lab 3 report answering **all 24 questions in Sections 1–11**. The teacher asks for a **short report with clear support for the conclusions and relevant code**. Aim for **5–7 readable pages**, but with 11 sections a result around **8–9 pages may be more realistic**. Seven is a preference, never a rule that permits skipping questions, deleting necessary evidence, shrinking diagrams until unreadable, or using tiny text.

**Default report structure:** Title and student; Introduction; Experimental Setup; Results and Analysis (11 numbered subsections, teacher's questions and short direct answers); Discussion; Conclusion; compact Appendix with selected code. Use the course template's general structure. Avoid a cover-only page, unnecessary theory, repeated plots, forced page breaks, or redundant result tables.

## Division of work — keep Codex tokens low

- **GPT (chat):** Before *each section*, read the actual assignment and produce the reasoning, expected/theoretical calculations, clearly labelled draft answers, measurements to collect, code tasks and figure plan. GPT's draft numbers are **not measurements** until verified against Obid's run.
- **Codex:** Only implement the named section in `code/`, run the new code once **only when needed** for genuine measurements and figures, put the given answer text and confirmed results into `report/main.tex`, save figures to `figures/`, and stop. Preserve earlier sections.
- **User:** Compile `main.tex` in **TeXstudio**. Visually inspect the compiled PDF together with GPT. Edit spacing only after viewing pages. Handle all Git commits and pushes using **Grok**.

Codex must **NOT**: compile LaTeX, export PDF, render/view screenshots, visually inspect images or PDF pages, run exhaustive test suites, do unrelated research, refactor earlier code, edit Yacoub's files, commit, push, or write long summaries. A minimal syntax/source check is fine. If a local editor forces a compiler check, do only the mandatory check and do not export/review a PDF.

## Writing rules

Read `SIMPLE_WRITING_STYLE.txt`. Obid's report should read like a capable university student speaking plainly: very simple, short, clear English. Use **I** for genuine individual actions, neutral sentences for observed physics or mathematics, and never **we/our** to imply collaboration. Keep each question from Mårten (verbatim where practical), then **Answer:** usually 1–4 short sentences. Add a few more only if essential. State actual units and limitations. Never invent results, timings, image differences, citations, or observations. No AI-style filler.

## Academic independence and source boundaries

- **Use the teacher's PDF code snippets and Obid's own independently developed experiments as the baseline.** Keep teacher-provided code unchanged except where a TODO or required task calls for an extension, or when a bug must be fixed and explained.
- The uploaded `lab3(1).py` contains a **completed multi-section implementation** (including a `peppers.tiff` path); it is **not the teacher's starter code**. Do **not** take its finished computations, plots, or reported numbers as Obid's work.
- Yacoub's finished Lab 3 PDF is **scope reference only**, not source material for Obid's code, prose, choices, figures, timings or results. Do not simply recolor, relabel, or resize another student's figures to disguise reuse.
- Identical answers to teacher-fixed mathematical questions are fine; independent input choices, code execution, honest observations, and explanation of the method matter more than superficial visual differences.

## Inputs and path handling

- The teacher says to use `ManWoman.png` for the exercises, while the supplied user file was named `ManWoman(2).jpg` and was **actually WEBP-encoded**. The setup package includes `assets/ManWoman.png`: a lossless PNG conversion of those supplied pixels (**631 × 475 RGB**). Use that as the main Obid test image unless the user explicitly chooses another input. Record its dimensions in results; never claim it is 512 × 512.
- Other uploaded photos/test patterns are optional for experiments that genuinely benefit from them; do not introduce extra images for cosmetic uniqueness.
- For Q5.2, **512 × 512 is the teacher's hypothetical matrix-size calculation**, regardless of the real test-image dimensions. Calculate the storage amount; do not allocate the giant dense transformation matrix.
- For Q11.1, Obid can create and test a simple reproducible synthetic binary image with different shapes. Document the actual number of shapes and detection count. Do not copy someone else's synthetic scene.
- Use paths relative to `Path(__file__)`, not fixed Windows paths. Keep the original image unchanged.

## Teacher-specific cautions

1. **Q1:** Implement power law `I_out = I_in ** gamma` after normalizing 0..1. Report gamma=2 outputs for intensities 64,128,192 and show image histogram before/after gamma=2.2. Explain the histogram movement without claiming gamma is an exact human-eye model.
2. **Q2:** OpenCV's `COLOR_BGR2YCrCb` returns **Y, Cr, Cb**, not Y,Cb,Cr. Q2.2 chroma factor 2 reduces both chroma widths/heights: compute stored-channel sample savings **before upsampling for display**. For larger factors describe actual visible degradation.
3. **Q3:** For 4-bit quantization distinguish **theoretical packed storage** from the real `uint8` array. For 3 bits use eight allowed levels and a correctly labelled histogram.
4. **Q4:** Compare equal Gaussian filters with **actual timed measurements** (separable vs 2D); show horizontal edges via Sobel `dy=1` and gradient magnitude from both signed derivatives.
5. **Q5:** Compare vectorized and nested-loop brightness/contrast timing on the same image and transformation; state timing conditions. Q5.2 do not allocate H.
6. **Q6:** LUT versus direct method must calculate the **same transformation**. Time and quantify fairly (including whether LUT construction is counted). Q6.2 asks for midtone enhancement while compressing shadows and highlights: verify the transfer curve actually does that.
7. **Q7:** Four **16×16** elementary outer-product images; for Q7.2 use exactly **three** elementary images, find and report weights with an actual fitting method, and show honest reconstruction quality.
8. **Q8:** Centered 2D FFT magnitude; a spectrum gives edge **orientations/frequencies**, not positions of specific edges. Display spatial low-pass and high-pass results from appropriate inverse transforms and explain smoothing/detail loss.
9. **Q9:** Original and cumulative histograms, reduced-contrast then equalization image; compare your CDF method with `cv2.equalizeHist()` on the same input and report any discrepancies.
10. **Q10:** The teacher's Gaussian-noise example casts noise to `uint8` **before** adding, which can wrap negative values; do signed/float addition then clip and convert to `uint8`, noting the necessary correction. Compare PSNR using actual runs, keep comparisons fair with the **same noisy input** where required, and document how Q10.1 matched filtered PSNR by changing noise levels. Do not copy Yacoub's PSNR figures.
11. **Q11:** Detect and count shapes with a documented binary mask and morphology, and compare morphological gradient with the **Sobel** gradient from Q4. Include circumstances where each is preferable.

## Figures and layout

Plan **roughly 8–12 compact multi-panel figures** to cover all 11 sections, not 20+ unless evidence genuinely requires it. Figures may combine closely related experiments; do not combine unrelated things just to save pages. Make all labels, scales, captions, units, kernels, image dimensions, and input sources clear. Prefer a compact timing-results table covering Q4.1/Q5.1/Q6.1 when appropriate. Distinct visual styling is acceptable but must never modify numerical data or hide artifacts. The teacher's instructions outweigh the page budget.

## Suggested file structure

```text
labbs/obid/lab3/
├── AGENTS.md                 # Short auto-read Codex rules
├── README_FOR_CODEX.md       # This detailed guide
├── SIMPLE_WRITING_STYLE.txt  # User's original guide + individual-report override
├── TEACHER_QUESTIONS_CHECKLIST.md
├── assets/
│   └── ManWoman.png          # Converted copy of supplied image
├── code/
│   └── section01.py         # Later, one small script per requested section
├── figures/                  # Generated from Obid's code
└── report/
    └── main.tex             # User compiles manually in TeXstudio
```

## Minimal section-end checklist

1. Only this teacher section changed; previous approved text/plots remain intact.
2. Every requested sub-question addressed with real, traceable outputs.
3. Correct image, axes, units, scales and numerical quantities.
4. Straightforward individual English; no invented results.
5. No LaTeX compilation/PDF visual review/Git actions by Codex.

**Codex final response:** files changed, measurements/figures generated, and genuine blockers — **a few lines only**.
