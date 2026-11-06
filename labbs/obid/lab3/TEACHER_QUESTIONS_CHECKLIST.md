# Lab 3 v1.1 — Teacher Question Coverage (24 questions)

Source of truth: Mårten's `DT081A Signal and Image Processing - Lab 3`, version 1.1. This is a *short tracking paraphrase*, not a replacement for the exact teacher wording. Quote the PDF when building each section.

- [ ] 1.1 Gamma correction: `apply_gama` function, 64/128/192 at gamma 2.0 and table
- [ ] 1.2 Compare histogram before/after gamma 2.2 and explain relation to perception
- [ ] 2.1 Y vs R/G/B histogram spread, why Y for edges
- [ ] 2.2 Chroma factor-2 sample savings, inspect higher factors visually
- [ ] 3.1 Quantize to four bits, theoretical compression ratio
- [ ] 3.2 Histogram before/after three-bit quantization, interpret levels
- [ ] 4.1 Timed separable vs non-separable Gaussian filtering; when speed advantage occurs
- [ ] 4.2 Highlight horizontal edges, suppress vertical edges, explain Sobel implementation
- [ ] 4.3 Show gradient-magnitude result
- [ ] 5.1 Vectorized brightness/contrast vs nested-loop timing on same image
- [ ] 5.2 Explicit 512×512 convolution matrix H memory (calculation only)
- [ ] 6.1 LUT vs direct transformation timing and speed comparison
- [ ] 6.2 Logarithmic/midtone transfer function with plot
- [ ] 7.1 Four 16×16 outer-product elementary images using ramp/step/sine, explain features
- [ ] 7.2 Reconstruct simple 16×16 shape with exactly three elementary images, fit weights
- [ ] 8.1 Centered 2D FFT and dominant edge-frequency interpretation
- [ ] 8.2 Remove high frequencies, inverse FFT, compare with original
- [ ] 8.3 Remove low frequencies, inverse FFT, compare with original
- [ ] 9.1 Original intensity histogram and cumulative histogram, interpret both
- [ ] 9.2 Reduce contrast, perform histogram equalization, compare original and OpenCV
- [ ] 10.1 Add noise and tune levels to obtain close filter-output PSNR; document settings
- [ ] 10.2 Mean vs median filtering for Gaussian and salt/pepper noise, PSNR on matching inputs
- [ ] 11.1 Morphological object detection/counting with multiple object shapes
- [ ] 11.2 Morphological vs Sobel gradients and when each method is preferable

Final notes: short report, conclusions supported by figures/tables/measurements and relevant code, relation to lectures where useful, submit to Moodle.
