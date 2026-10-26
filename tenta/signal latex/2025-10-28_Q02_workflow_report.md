# 2025-10-28, Uppgift 2(a-b): feedback diagram, causality and difference equation

**PASS: both parts saved in existing `signal calc/2 electro map`. Question and folder numbers match.**

All work remains local. No calculator folder was created and no GitHub upload was performed. Question 3 was not processed.

## Original and source priority

- Original: [2025-10.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/2025-10.pdf>), PDF page 2 / printed page 1, dated 2025-10-28. Complete question, both 2p subparts and original block diagram repeated on each image.
- Own notes inspected first: [2 68a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2 electro map/2 68a.jpg>) and [2 68b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2 electro map/2 68b.jpg>), 2026-08-18 Q2; [2 61a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2 electro map/2 61a.jpg>) and [2 61b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2 electro map/2 61b.jpg>), 2026-01-07 Q2.
- Part (a) retains delay -> feedback -> FIR/IIR -> causality order. August notes supply the feedback explanation; January notes supply present/past versus future causality. The unrelated aside about previous exams always being IIR is excluded.
- Part (b) preserves the own handwritten input group + feedback group -> combine -> collect method. January backward gain tracing supports the location of the shared gain. No equation from the composite's appended typed block is copied; that block has a coefficient discrepancy.
- Adapt to the target topology: direct undelayed input, one feedback delay, return gain 0.3, and shared output gain 0.4 after the sum. Do not copy January's input delay or two-delay return path, nor August's three-delay branches.
- Verification only: [October graded paper](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/VWCHCLKL0000_Grade-B.pdf>), PDF page 6 / handwritten page 3. Its final y[n]=0.4x[n]+0.12y[n-1] and IIR/causal classification agree; cover Q2 mark 4/4. The own-note method is the primary source.

## Verified reasoning

1. Input group entering the sum: x[n].
2. Feedback group: y[n] passes one T, becoming y[n-1], then gain 0.3.
3. Signal after the sum: s[n]=x[n]+0.3y[n-1].
4. Output gain multiplies the whole sum: y[n]=0.4s[n]=0.4x[n]+0.12y[n-1].
5. Collected form: y[n]-0.12y[n-1]=0.4x[n].

Loop gain is 0.4*0.3=0.12. At initial rest the impulse response is h[n]=0.4*(0.12)^n for n>=0, zero for n<0. It remains nonzero for arbitrarily large n, establishing IIR for this actual system rather than assuming every feedback diagram must be IIR. Only present/past values are used, so it is causal.

Exact Fraction arithmetic verifies 16 branch-expansion substitutions and 16 impulse samples against the closed form. Detailed results: `tmp/pdfs/signal-export/2025-10-28/Q02/equation-verification.json`. No extra implementation tests or converter changes were introduced.

## Final images

| Part | Image | Dimensions | Bytes |
|---|---|---|---|
| a | [2 510a-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2 electro map/2 510a-l.png>) | 384 x 651 | 53174 |
| b | [2 510b-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/2 electro map/2 510b-l.png>) | 384 x 799 | 52065 |

## Validation

- Source diagram crop matches original PDF page 2, image 0, box [856,2449,1649,2727] pixel-for-pixel; original image dimensions 2484 x 3519. All gain values, arrow directions, delay and input/output labels preserved.
- Both latest PNGs visually inspected at actual width 384. Full original question, source diagram, matching solution and final answer present; no clipping or excessive whitespace.
- PDF text, figure count, geometry, margins and missing-glyph checks passed. Each output is a single rendered page.
- All 76 prior calculator files, 66 other source/workflow files and 6 original/reference inputs unchanged by SHA256. Q1 definitions and 7 registry entries preserved exactly. Existing eight calculator folders unchanged; exactly two new calculator PNGs.
- No missing subparts or unresolved values. No grading mark is substituted for the independent arithmetic check.

Authoritative source updated: [2025-10-28_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-10-28_compiled_notes.tex>). Shared layout and exporter reused unchanged.

Reproduce from the course root:

```powershell
& 'C:/Users/Jake_/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B 'tenta/signal latex/export_notes.py' --exam 2025-10-28 --question 2
```

Detailed validation/build files: `tmp/pdfs/signal-export/2025-10-28/Q02/`.

## Final PNG checksums

- 2 510a-l.png: `cb6a3079038f5fcfe97ee9b342b574d7d74a7d8b4203a9c89d3dcf4e37ace041`
- 2 510b-l.png: `fe05fcfca316d00ab2b8f64c2490fcec0e097b670b1c36e1549eee16b9fa2983`
