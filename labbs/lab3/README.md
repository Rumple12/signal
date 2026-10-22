# DT081A Lab 3 - Sections 1 and 2

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

The script prints the tables, saves three figures in `figures/` and opens the
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

## Verification and sources

The script ran successfully with the selected TIFF. Numerical checks covered
the gamma outputs, histogram counts, channel ordering, Y values, unchanged Y
during subsampling, reduced channel sizes and memory counts. The three saved
figures were also reviewed. Lab 1, Lab 2 and course materials were not changed.

Sources: Lab 3 Version 1.1, pages 1-3; Lecture 8, pages 14-15 and 21;
Lecture 9, page 26; Lecture 11, pages 3-4 and 9.
Only Sections 1 and 2 are implemented.
