# DT081A Lab 3 - Sections 1-5

Draft work by Jakob and Obid. This is not the final report.

## Setup and running

We used NumPy, OpenCV and Matplotlib. The image is the existing 512 x 512
`peppers.tiff` in `labbs/DT081A_Labs-main/DT081A_Labs-main/images/`.
The PDF names `ManWoman.png`, but it is missing from the repository and course
ZIP. The PDF also allows experiments with other images. We chose peppers
because it has clear colour boundaries and different colour values. The script
reads the TIFF directly without copying or changing it.

Run from the repository root:

```powershell
python -m pip install -r labbs/lab3/requirements.txt
python labbs/lab3/lab3.py
```

The existing local environment can also run it:

```powershell
.\labbs\lab3\.venv\Scripts\python.exe labbs/lab3/lab3.py
```

The script prints the tables, saves nine figures in `figures/` and opens the
plots. Close the plot windows to finish. Running it again replaces the figures.

## 1.1 Gamma calculation

We used the lab's formula on values between 0 and 1:
`output = 255 * (input / 255) ** gamma`.
The function is named `apply_gama`, as in the question. The starter code spells
it `apply_gamma`.

| Input | Output before integer conversion, gamma = 2.0 | Output as uint8 |
| --- | --- | --- |
| 64 | 16.063 | 16 |
| 128 | 64.251 | 64 |
| 192 | 144.565 | 144 |

All three values get darker. Raising a value between 0 and 1 to a power above
1 makes it smaller. Conversion to `uint8` removes the decimal part.
We followed the PDF's exponent `gamma`. Lecture 8 also shows `1/gamma` for
camera pre-correction; that is a different operation.

## 1.2 Gamma and the intensity histogram

We used a grayscale copy for this part, so each pixel has one intensity value.
We applied gamma = 2.2. The corrected image looks darker, and its histogram
moves towards lower values. The mean intensity falls from **120.22 to 61.00**.
Dark values become packed closer together. Some output levels have no pixels
because the result is converted back to whole numbers from 0 to 255.
Gamma changes brightness in a nonlinear way, rather than adding the same
amount to every pixel. This relates to the eye's unequal sensitivity to changes
in brightness; this power curve is not an exact logarithmic model of vision.

Figure: `figures/section1_gamma_histograms.png`. Both images use the same
0-255 display scale. Both histograms use the same axes and 256 bins.

## 2.1 RGB and Y histograms

We used the original colour image for Section 2. OpenCV reads BGR. We converted
it to RGB for display and used the teacher's `cv2.COLOR_BGR2YCrCb` conversion.
Its channel order is **Y, Cr, Cb**, so we extracted them in that order.
Y is approximately `0.299*R + 0.587*G + 0.114*B`.

| Channel | Minimum | Maximum | Standard deviation |
| --- | --- | --- | --- |
| Y | 0 | 228 | 53.88 |
| R | 0 | 231 | 45.17 |
| G | 0 | 237 | 75.05 |
| B | 0 | 229 | 44.29 |

Standard deviation measures how spread out the values are. Here, G has the
largest spread. R has many high values, while B has mostly low values. Y mixes
information from all three channels. Its spread is smaller than G's, but
larger than R's and B's. Y is not always the narrowest histogram.

**Why use Y for edge detection?** Y describes brightness. Edges often appear
where brightness changes quickly. Using Y gives one channel to process rather
than three separate colour channels. A boundary between colours with similar
brightness can still be missed.

Figure: `figures/section2_channel_histograms.png`. All four use the same
intensity range. Their pixel-count scales are labelled separately.

## 2.2 Chroma subsampling

The PDF suggests `cv.resize()` but gives no resize example or dimensions.
We used `cv2.resize()` and divided **both width and height** by each factor.
We kept Y unchanged. We used area interpolation to reduce Cb and Cr, then
linear interpolation to restore their size for colour display.

With factor 2, each chroma channel keeps one quarter of its samples.
For N pixels, the original has `3N` channel samples. The smaller version has
`N + N/4 + N/4 = 1.5N`. This saves **50%**.

| Factor | Size of each chroma channel | Stored channel samples | Saving |
| --- | --- | --- | --- |
| 1, original | 512 x 512 | 786,432 | 0% |
| 2 | 256 x 256 | 393,216 | 50% |
| 4 | 128 x 128 | 294,912 | 62.5% |
| 8 | 64 x 64 | 270,336 | 65.625% |

This counts Y plus the two reduced chroma channels, before reconstruction.
Each sample uses one byte here. It does not measure compressed TIFF or JPEG
file size. Rebuilding full-size channels for display uses more memory again.

Factor 2 looks close to the original at the full image size. Small changes are
easier to see in the enlarged crop. At factor 4, colour boundaries look softer.
At factor 8, colour blending is clearer, especially along the yellow-green and
red pepper boundary in the crop. Brightness detail remains because Y was kept.
The point where this becomes noticeable depends on the image and viewing size.

Figure: `figures/section2_chroma_subsampling.png`. The top row shows the full
images. The bottom row enlarges the same 128 x 128 region, using rows 128-255
and columns 128-255.

## 3.1 Four-bit colour quantization

We reused the original RGB image. Integer division by 16 groups each channel
value into a level from 0 to 15. Multiplying by 16 gives display values
`0, 16, 32, ..., 240`. This follows the teacher's lower-value convention.
For example, all input values from 32 to 47 become 32 in the displayed image.

There are 16 possible levels per channel. This image uses **15** in each of R,
G and B, because the original has no channel values from 240 to 255.
The main shapes still look clear. The image looks slightly darker, and some
smooth colour changes look more stepped. The difference is fairly small at
the full image size.

**Theoretical compression ratio:** `8 / 4 = 2:1`, with **50% storage saving**.
This assumes two 4-bit values are packed into each byte.

| Storage for the RGB image | Bytes |
| --- | --- |
| Original uint8 array, measured | 786,432 |
| Packed 4-bit values, theoretical | 393,216 |
| Quantized levels in a uint8 array, measured | 786,432 |

Our NumPy array still uses one byte per value. Its actual size is unchanged.
We did not pack the values into 4-bit storage or measure compressed file-size
savings. The saved figure is a comparison, not a compressed version of the TIFF.

Figure: `figures/section3_4bit_quantization.png`.

## 3.2 Three-bit grayscale quantization

We reused the original grayscale image from Section 1, before gamma correction.
Dividing by 32 gives eight levels, numbered 0-7. For display, we multiply these
levels by 32, giving `0, 32, 64, 96, 128, 160, 192, 224`. Both images use the
same 0-255 display scale, following the teacher's lower-value convention.

The original histogram has many occupied intensity values. After quantization,
the histogram has only eight occupied levels. Each new bar combines 32 of the
original intensity values. Level 7 has only 29 pixels, so its bar is barely visible.
Both histograms still count **262,144 pixels**. Their horizontal axes show
different units: original intensity values and quantized level numbers.

Smooth changes in brightness now look like bands, especially on the large
peppers. The outlines remain clear, but some shading and texture are lost.
This happens because nearby brightness values become identical. Their small
differences cannot be recovered from the quantized image.

Figure: `figures/section3_3bit_histograms.png`. It shows both grayscale images
and their histograms. The pixel-count scales are labelled separately.

## 4.1 Gaussian filtering

We reused the original 512 x 512 grayscale image. We made a 1D Gaussian kernel
with `cv2.getGaussianKernel()` and used `np.outer()` to form the matching 2D
kernel. Both methods used sigma = 1.0, float64 output and the same reflected
border rule, `cv2.BORDER_REFLECT_101`.

We compared `cv2.filter2D()` with `cv2.sepFilter2D()`. Each method ran once
before timing. We then measured 30 calls using `time.time()` and calculated
the average per call. Kernel creation and plotting were outside the timed loops.
These values are from a normal script run with OpenCV 5.0.0:

| Kernel size | Ordinary 2D filtering (ms) | Separable filtering (ms) |
| --- | --- | --- |
| 5 x 5 | 5.420 | 1.429 |
| 11 x 11 | 9.880 | 10.455 |
| 21 x 21 | 23.481 | 24.022 |

Separable filtering was clearly faster for 5 x 5. At 11 x 11 and 21 x 21,
the times were close, with ordinary 2D slightly faster. Larger kernels took
longer for both methods in this run. Times can change between runs.

A direct 2D calculation uses `k*k` weights per pixel. A separable filter uses
one pass along rows and one along columns, using about `2*k` weights. This can
save many calculations with large kernels and large images. The actual time
also depends on the filtering routines and computer. Our measurements do not
show that separable filtering is always faster.

The two Gaussian outputs look the same. Their largest measured difference was
about **0.000002 intensity units** across the three kernel sizes. Both blur
fine texture and soften boundaries. The figure shows the teacher's 5 x 5,
sigma = 1.0 example with the same 0-255 display scale for all three images.

Figure: `figures/section4_gaussian_comparison.png`.

## 4.2 Horizontal edges

The short function `detect_horizontal_edges()` uses Sobel with `dx=0, dy=1`.
It measures brightness changes from top to bottom. We display the absolute
values so both directions of brightness change appear as positive strengths.

The horizontal image shows curved top and bottom pepper boundaries and the
edge along the bottom of the picture strongly. The long vertical sides of
the thin pepper are weaker. Those sides are clearer in the vertical-edge
comparison, which uses `dx=1, dy=0`. Curved and sloping edges can appear in
both images. The two edge images use the same display scale.

Figure: `figures/section4_sobel_edges.png`.

## 4.3 Gradient magnitude

We combined the signed derivatives using
`sqrt(sobel_x**2 + sobel_y**2)`. We kept those values and made a separate
0-255 version for display, as in the teacher's example.

The result shows more complete pepper outlines and stem details. It includes
the long vertical sides as well as top and bottom boundaries because it uses
brightness changes in both directions. The horizontal-only image leaves more
of these outlines weak. Bright pixels mean a stronger edge.

Figure: `figures/section4_gradient_magnitude.png`.

## 5.1 Brightness and contrast with vectors and loops

We reused the original grayscale image. Both methods use
`1.2 * (intensity - 128) + 128 + 20`. This changes contrast around 128 and then
adds brightness. We use floats during the calculation, clip to 0-255 and
remove the decimal part when converting back to `uint8`.

The NumPy method uses `reshape(-1, 1)` to stack the pixels into one column,
adjusts the values and reshapes the result back into an image. The other
method uses nested Python loops to adjust every pixel separately.

We timed five runs of each method with `time.time()` and calculated the
average per run. The times include the calculations, output creation and
type conversion. Image loading and plotting are outside the timed loops.

| Method | Average execution time (ms) |
| --- | --- |
| NumPy vectorized | 2.040 |
| Nested Python loops | 468.915 |

NumPy was **229.82 times faster**, using the unrounded timing values. It handles
the array operations inside its library, avoiding a Python loop for every
pixel. These times are from one run on this computer and can vary.

`np.array_equal()` returned **True**. Both methods gave exactly the same image,
with values from **0 to 255**. The adjusted image looks brighter overall.
Highlights look whiter, while the dark gaps between peppers remain dark.
Some highlights are clipped at 255. Both images use the same display scale.

Figure: `figures/section5_brightness_contrast.png`.

## 5.2 Memory needed for the full convolution matrix H

A 512 x 512 image has **262,144 pixels**. Its stacked vector has that many
values, so H has **262,144 rows and 262,144 columns**. This gives
**68,719,476,736 elements**.

| Value type | Bytes per element | Total bytes | Memory (GiB) |
| --- | --- | --- | --- |
| float32 | 4 | 274,877,906,944 | 256 |
| float64 | 8 | 549,755,813,888 | 512 |

We calculated `pixels * pixels * bytes_per_element` and divided by `1024**3`
to get GiB. H was not created; the code calculates these numbers only.

The full matrix stores an entry for every input and output pixel pair. Most
entries would be zero for a 3 x 3 filter, but the full matrix still stores them.
It is much more practical to store just the **nine kernel weights** and apply
them to each small image neighbourhood.

## Verification and sources

The script ran successfully with the selected TIFF. Numerical checks covered
the gamma outputs, histogram counts, channel ordering, Y values, unchanged Y
during subsampling, reduced channel sizes and memory counts. The three saved
figures were also reviewed. Lab 1, Lab 2 and course materials were not changed.

Section 3 checks covered the allowed levels, the teacher's quantization rule,
the 2:1 ratio, 50% theoretical saving, actual array sizes and histogram pixel
counts. Both new figures were reviewed. The approved Sections 1-2 calculations
and their three saved figures are unchanged.

Section 4 checks confirmed matching Gaussian kernels, input, output type and
border handling. All three output comparisons differed by less than 0.00001.
Simple step arrays confirmed the horizontal edge direction. The magnitude
calculation and displayed arrays were also checked. All three new figures
were reviewed. Sections 1-3 and their five saved figures are unchanged.

Section 5 passed checks for stacking, known pixel values, clipping, integer
conversion and exact agreement between methods. The measured timing ratio
and both memory calculations were checked. The new figure was reviewed.
Sections 1-4 and their eight saved figures are unchanged.

Sources: Lab 3 Version 1.1, pages 1-3; Lecture 8, pages 14-15 and 21;
Lecture 9, page 26; Lecture 11, pages 3-4 and 9.
Section 3 sources: Lab 3 Version 1.1, pages 3-4; Lecture 8, page 25;
Lecture 11, page 7.
Section 4 sources: Lab 3 Version 1.1, pages 4-5; Lecture 9, pages 4-8 and 15.
Section 5 sources: Lab 3 Version 1.1, page 5; Lecture 9, pages 9-14 and 17.
Only Sections 1-5 are implemented.
