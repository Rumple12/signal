# 2025-01-07, Uppgift 7: 2D low-pass frequency response

**PASS: complete unlettered question saved in existing `signal calc/7 kernels`. Question and folder numbers match.**

All work remains local. No output folder was created and no GitHub upload was performed.

## Sources and fidelity

- Original: [2025-01 exam.pdf](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/2025-01 exam.pdf>), PDF page 5 / printed page 4, Q7 (3p). Full wording and original response surface retained.
- Existing calculator notes inspected first: [7 68.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7 kernels/7 68.jpg>). These cover averaging, sharpening and edge kernels; they establish folder 7 as the image-filtering subject group, but are not the closest response-surface solution.
- Primary own handwriting: [7 510-1.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/7 510-1.jpg>), handwritten page 2/3 for 2025-10-28 Q7. Retained the method: surface height gives gain, compare the center with frequencies farther away, classify the filter, describe the image effect.
- Supporting own handwriting: [7 510.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/7 510.jpg>), page 1/3 defines low spatial frequencies as smooth areas/gradual brightness changes and high frequencies as sharp edges/fine details. [7 510-2.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-10/7 510-2.jpg>), page 3/3 explicitly draws a central hill as low-pass and labels blurred output as low-pass behavior.
- Adaptation is explicit: the October main answer describes a high-pass graph, while January has a high center and low outer region. The own low-pass sketch matches January. The October high-pass classification and unrelated image choices were not copied. The PNG states that it is adapted from the user's handwritten graph-reading notes.
- Verification only: [January graded paper](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2025-01/DT081A-2025-01-07 (1)/F6PACQ9N0000_Grade-C.pdf>), PDF page 10 / handwritten page 9, received 3/3 for low-pass, high center, low outer response and the spatial-frequency interpretation. It did not replace the own-note method.

## Interpretation

Near u=v=0 the magnitude is close to 1, so low spatial frequencies pass strongly. Farther from the center the magnitude falls toward 0, attenuating high frequencies. Smooth regions remain while edges and fine details are reduced: low-pass smoothing / blurring.

High gain is described as passing strongly, without claiming amplification above 1. The graph suggests a smooth low-pass shape; no exact Gaussian formula, kernel, phase or cutoff is inferred.

## Final image and checks

- [7 51-l.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/7 kernels/7 51-l.png>): 384 x 707 pixels; 75019 bytes.
- SHA256: `b593b32ea7341c85c4cdf2e1fc9684dd108aa22bd8b7d45eb7cfed3ffd3d86b1`.
- One image for the complete unlettered question; no invented part letter.
- Entire original question and 3p allocation above the solution; original graph crop verified pixel-for-pixel against PDF page 5, image 0, box [850,510,1780,1345].
- Native 384-pixel final PNG visually inspected. Text, axes, colorbar, explanation and final answer fit without clipping. PDF geometry, text, figure, missing-glyph and margin checks passed.
- All 67 previous calculator files, 52 other existing source/workflow files and 6 original/reference inputs preserved by SHA256. Q1-Q6 definitions and 22 previous registry entries preserved. Existing eight calculator folders and shared exporter/layout unchanged.
- No incomplete subparts or unresolved classification. Cross-year adaptation recorded rather than presented as an exact handwritten January solution.

Authoritative source: [2025-01-07_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2025-01-07_compiled_notes.tex>).

Reproduce from the course root:

```powershell
& 'C:/Users/Jake_/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B 'tenta/signal latex/export_notes.py' --exam 2025-01-07 --question 7
```

Detailed validation and build intermediates: `tmp/pdfs/signal-export/2025-01-07/Q07/`.
