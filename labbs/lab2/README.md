# DT081A Lab 2 - Sections 1, 2 and 3

This folder contains a simple script, six figures and draft answers. The work
stops after Section 3. This is not the complete Lab 2 report.

## Run the script

From the repository root:

```powershell
python -m pip install -r labbs/lab2/requirements.txt
python labbs/lab2/lab2.py
```

The existing local environment can also run it:

```powershell
.\labbs\lab2\.venv\Scripts\python.exe labbs/lab2/lab2.py
```

The script prints basic checks, saves six PNG files in `labbs/lab2/figures/`
and opens the plots. Close the plot windows to finish. Running it again replaces
the saved figures.

## Draft material for the university report template

### 2 Experimental Setup

I used NumPy, SciPy and Matplotlib. I added three cosine waves using the
teacher's values:

- Sampling frequency: 250 Hz.
- Time vector: `np.arange(0, 0.6, 1/fs)`.
- Frequencies: 50, 55 and 120 Hz.
- Amplitudes: 1, 0.1 and 0.3.
- Phases: 0, pi/4 and pi/2 radians.

There are 150 samples. The record length is 0.6 seconds. The last sample is at
0.596 seconds because `np.arange` excludes the endpoint. The FFT frequency
points, called bins, are about 1.67 Hz apart (`250 / 150`). The highest frequency,
120 Hz, is below half the sampling frequency, so the lab's condition for avoiding
aliasing is met.

The PDF also mentions 0.4 seconds in Section 2. I followed its Python example,
which uses 0.6 seconds.

### 3.1 Results and Analysis: Time-Domain Analysis

The time plot shows the three cosine waves added together. The full spectrum
has matching peaks at positive and negative 50, 55 and 120 Hz. The positive
spectrum shows the three frequencies clearly. The 55 Hz peak is the smallest.

| Frequency (Hz) | Positive raw FFT magnitude |
| --- | --- |
| 50 | 75.0 |
| 55 | 7.5 |
| 120 | 22.5 |

These are raw values from `np.abs(fft(x))`, as in the teacher's code. Their
heights are not the original cosine amplitudes. For these peaks,
`2 * magnitude / 150` gives 1, 0.1 and 0.3, matching the input.

**Why does the spectrum contain negative frequencies?**

The Fourier transform represents each real cosine using a positive and a
negative frequency. Both parts have the same magnitude. This explains the
matching peaks in our plot. They are part of the mathematical representation,
so they do not mean that we added extra waves. The positive half is enough to
show this real signal's frequency magnitudes.

Figures: `section1_time_domain.png`, `section1_two_sided_fft.png` and
`section1_positive_fft.png`, saved in `figures/`.

### 3.2 Results and Analysis: Frequency Identification

I left the signal unchanged for the rectangular window. I then used
`windows.hann(len(x))` and `windows.hamming(len(x))`, with the default settings
from the PDF, and calculated their FFTs.

In `figures/section2_window_spectra.png`, the left column shows all three
spectra on the same raw magnitude scale. The right column zooms in on 45-60 Hz.
For that column only, each spectrum is divided by its highest peak. This gives
the largest peaks the same height and makes their widths easier to compare.
Dots show the actual FFT bins; lines just connect them.

| Window | Raw magnitude at 50 Hz | At 55 Hz | At 120 Hz |
| --- | --- | --- | --- |
| Rectangular | 75.0000 | 7.5000 | 22.5000 |
| Hann | 37.2524 | 3.7489 | 11.1729 |
| Hamming | 40.2722 | 4.0490 | 12.0790 |

Hann and Hamming lower the raw peak heights because they give less weight to
samples near the ends. The frequencies are still present.

**Which window best separates close frequencies? Why?**

For this signal, the rectangular window gives the clearest separation of
50 and 55 Hz. Its peaks are narrower, and the FFT bins between them are nearly
zero. Hann and Hamming spread the peaks over more nearby bins. However, all
three windows still show a separate small peak at 55 Hz.

Frequency resolution means how well nearby frequencies can be told apart.
Narrower peaks help. Here, 50 and 55 Hz are three FFT bins apart. All three
frequencies land exactly on FFT bins and complete whole numbers of cycles in
0.6 seconds: 30, 33 and 72 cycles. This explains the clean rectangular result.

Spectral leakage means that a frequency spreads into other FFT bins when we
use only a short part of a signal. Hann and Hamming generally reduce leakage
farther from a peak, but make the peak wider. Our rectangular spectrum already
has almost no leakage into other bins. These results do not mean that the
rectangular window is always best.

### Lab Section 3: Linear Time-Invariant Systems

**3.1 System 1: Convolution**

I used a unit impulse with 150 samples, the same length as the signal from
Section 1. Convolution gives the eight values in `h`, followed by zeros:
`1, 0.5, 0.3, 0.1, -0.1, -0.4, -0.2, 0.1`.

**Does convolution give the correct response?** Yes. The checks confirm that
the first eight values match `h` and all later values are zero. Full convolution
returns `150 + 8 - 1 = 157` samples. This longer output is normal.

**Is it FIR or IIR?** System 1 is FIR, meaning finite impulse response. It has
only eight non-zero values. The response is zero after sample 7.

Figure: `figures/section3_system1_convolution.png`. It shows samples 0-20 so the
eight non-zero values are easy to see. All 157 output values were checked.

**3.2 System 2: Difference Equation**

I used a 100-sample unit impulse for both the manual loop and `lfilter`, with
`b = [1, 0.3]` and `a = [1, 0.6, -0.35]`. Values before sample 0 were zero.
The equation is:

```text
y[n] = x[n] + 0.3*x[n-1] - 0.6*y[n-1] + 0.35*y[n-2]
```

The first five output values are `1, -0.3, 0.53, -0.423, 0.4393`. The response
alternates between positive and negative values and gradually gets smaller.

**Is it FIR or IIR?** System 2 is IIR, meaning infinite impulse response.
It uses earlier output values to calculate new ones. This is called feedback.
Its impulse response keeps going in theory, although it gets smaller. The
plot shows only the first 100 samples.

**Do the two implementations give the same results?** Yes. `np.allclose()`
returns `True`. The largest absolute difference was `0.0` in this run.

Figure: `figures/section3_system2_comparison.png`. The two stem plots show the
manual and SciPy responses separately, using the same 100-sample input.

**Small corrections:** The PDF repeats `y[n-1]` in its last output term. I used
`y[n-2]` to match its `lfilter` coefficients. I also omitted the outdated
`use_line_collection=True` argument from `plt.stem()`. For System 2, I followed
the explicit 100-sample instruction rather than the example's `len(x)`.

Section 3 references: Lab 2, pages 3-4; Lecture 4, pages 20-21 (convolution and
impulse input); Lecture 7, page 23 (FIR and IIR).

## Source checks and small corrections

The extensionless Lab 2 file was verified as a PDF using its `%PDF-` header
and a PDF reader. Its local copy already had a `.pdf` extension before this
task. It matches the original bytes in Git. Course materials and Lab 1 were
not edited.

No outdated function arguments needed fixing in Sections 1 and 2. I added
`fftshift` to order the full spectrum from negative to positive frequencies.
This avoids a line across the graph caused by the FFT's original ordering.
It does not change the FFT values.

Relevant theory: Lecture 4, slide 10, and Lecture 5, slides 20-23. The draft
uses the university template's setup and results headings. The complete report
will be prepared after the other sections are finished.
