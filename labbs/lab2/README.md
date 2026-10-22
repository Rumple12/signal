# DT081A Lab 2 - Sections 1-7

This folder contains a simple script, twelve figures and draft answers.
Sections 1-6 are complete. The Section 7 code is ready, but the voice experiment
is pending until the real recording is provided. This is not the final report.

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

The script prints basic checks, saves twelve PNG files in `labbs/lab2/figures/`
and opens the plots. Close the plot windows to finish. Running it again replaces
the saved figures. Section 7 adds two more figures when `voice.wav` is available.

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

### Lab Section 4: Frequency-Domain Analysis

I reused the original signal and FFT from Section 1. The amplitude spectrum is
`np.abs(X)`, and the phase spectrum is `np.angle(X)` in radians. I found the
positive-frequency peaks using a raw FFT magnitude above 1. The other bins
contain only tiny rounding errors for this signal.

The raw peak heights are 75, 7.5 and 22.5. To recover the cosine amplitudes,
I used `2 * np.abs(X[index]) / len(x)` at each peak. The table contains the
calculated FFT results, rounded to six decimal places:

| Frequency (Hz) | Cosine amplitude | Phase (radians) |
| --- | --- | --- |
| 50 | 1.000000 | 0.000000 |
| 55 | 0.100000 | 0.785398 |
| 120 | 0.300000 | 1.570796 |

**Do the amplitudes and phases agree with the original signal?** Yes. The
amplitudes match 1, 0.1 and 0.3. The phases match 0, pi/4 and pi/2. The tiny
differences are rounding errors. All three `np.allclose()` checks pass for
the measured frequencies, amplitudes and phases.

Figure: `figures/section4_amplitude_phase.png`. The left plot shows the raw FFT
magnitudes. The right plot shows the phase at the three peaks. I hid phase
values where the raw magnitude is below 1, since phase is not useful when
there is almost no signal at that frequency. The original phase array is
unchanged. No correction to the teacher's Section 4 calculations was needed.

Section 4 references: Lab 2, pages 4-5; Lecture 4, page 9; Lecture 6, page 5.

### Lab Section 5: System Frequency Response

I reused System 2's coefficients, `b = [1, 0.3]` and `a = [1, 0.6, -0.35]`.
I used `lfilter` with a 150-sample unit impulse, then calculated
`H = fft(h_system2)`. Its magnitude gives the estimated amplification, and its
angle gives the phase shift. The first 100 impulse-response samples match
Section 3.

I then filtered the teacher's single 50 Hz cosine. I found the strongest
positive-frequency FFT bin for the input and output. Both are at 50 Hz.
The cosine amplitudes use `2 * np.abs(FFT[index]) / len(x)`, and the phases
use `np.angle(FFT[index])`. These are the calculated values, rounded:

| Signal | Frequency (Hz) | Cosine amplitude | Phase (radians) |
| --- | --- | --- | --- |
| Input | 50 | 1.000000 | 0.000000 |
| Output | 50 | 0.748103 | -0.010340 |

At 50 Hz, the amplification from `H` is **0.745376**, and the phase shift is
**-0.012772 radians**. The system reduces the input's amplitude and shifts its
phase slightly.

**Does the result support `Y(f) = H(f) * X(f)`?** To check this, I multiplied
the input amplitude by the amplification. I added the input phase to the
system's phase shift:

| Output comparison at 50 Hz | Amplitude | Phase (radians) |
| --- | --- | --- |
| Predicted from H and input | 0.745376 | -0.012772 |
| Measured from output FFT | 0.748103 | -0.010340 |
| Measured minus predicted | +0.002727 | +0.002432 |

The amplitude difference is about **0.366%** of the prediction. The measured
and predicted values are close, which supports the expected relationship.
They do not match exactly for these finite arrays.

The filter starts at rest, so the output includes a start-up effect. We also
keep only 150 samples of the impulse response and output, cutting off their
later values. This explains the small differences. They are not just rounding
errors. No exact equality check was forced across the FFT arrays.

Figures:

- `figures/section5_system_frequency_response.png`: amplification and phase
  shift versus frequency, estimated from the 150-sample impulse response.
- `figures/section5_input_output_spectra.png`: input and output amplitude and
  phase spectra. The output also contains small values at other frequencies.
  These appear because the filter needs a short time to settle when the signal
  starts. Their phases also appear in the plot. The comparison above uses the
  50 Hz bin. Phase at almost empty bins is hidden.

The script checks the impulse response, both peak frequencies and the input's
amplitude and phase. It prints the prediction and actual differences. No
correction to the teacher's Section 5 code was needed.

Section 5 references: Lab 2, pages 5-6; Lecture 6, pages 12 and 14.

### Lab Section 6: Filtering

I used `fs1 = 2500 Hz`, cutoff 200 Hz, order 5 and Chebyshev ripple 3 dB.
I calculated the responses using `lfilter` on a unit impulse, followed by an
FFT, as in the teacher's example. I used 1000 samples so the filters could
settle. The FFT bins are 2.5 Hz apart. The figures zoom in on 0-750 Hz.

**1. How do Butterworth and Chebyshev Type I differ?**

Butterworth has a smooth amplification response. Chebyshev has ripple, meaning
small rises and falls in the frequencies it passes. Its measured passband
ranges from about -3 to 0 dB. Chebyshev also drops more sharply after the
cutoff. At 300 Hz, it gives -37.351 dB, compared with -18.866 dB for Butterworth.
A value of 0 dB means unchanged amplitude. Negative dB means a weaker signal.

Their phase responses also differ. At 100 Hz, the phase is -1.649 radians for
Butterworth and -2.111 radians for Chebyshev.

**2. What changes when we change type, cutoff and order?**

I used Butterworth for these comparisons and changed one setting at a time:

- Low-pass keeps lower frequencies and reduces higher ones. High-pass does
  the opposite. The phase curves also change.
- Raising the cutoff from 200 to 350 Hz lets more high frequencies through.
  It also makes the phase shift less negative at 100 Hz.
- Raising the order from 3 to 7 makes the drop after the cutoff steeper.
  The phase shift becomes more negative at 100 Hz.

These measured FFT values support the observations:

| Filter settings | Amplification at 300 Hz (dB) | Phase at 100 Hz (radians) |
| --- | --- | --- |
| Butterworth LP, 200 Hz, order 5 | -18.866 | -1.649 |
| Butterworth HP, 200 Hz, order 5 | -0.057 | -0.078 |
| Butterworth LP, 350 Hz, order 5 | -0.711 | -0.877 |
| Butterworth LP, 200 Hz, order 3 | -11.597 | -1.033 |
| Butterworth LP, 200 Hz, order 7 | -26.343 | -2.282 |

The phase plots use `np.angle()`, as in the teacher's example. The jumps between
-pi and pi come from how angles are displayed. Angles differing by 2*pi mean
the same phase. Phase is hidden where the amplification is almost zero.

**3. How are band-pass and band-stop filters designed?**

I used the same Butterworth function with two cutoff frequencies:

```python
band = [150, 400]
b_bp, a_bp = signal.butter(filter_order, band, btype="bandpass", fs=fs1)
b_bs, a_bs = signal.butter(filter_order, band, btype="bandstop", fs=fs1)
```

Band-pass keeps frequencies within the band and reduces those outside it.
Band-stop reduces frequencies within the band and keeps those outside it.
The band-pass response is about 0 dB at 250 Hz, -65.011 dB at 50 Hz and
-36.263 dB at 600 Hz. The band-stop response is below -100 dB at 250 Hz,
but about 0 dB at 50 and 600 Hz. The checks confirm both behaviours.

Figures:

- `figures/section6_butterworth_chebyshev.png`: the two low-pass designs.
- `figures/section6_filter_variations.png`: type, cutoff and order comparisons.
- `figures/section6_bandpass_bandstop.png`: band-pass and band-stop responses.

**Corrections:** Section 6 uses its own frequency axis from
`fftfreq(filter_samples, 1/fs1)`. The teacher's old axis used 250 Hz instead of
2500 Hz. The phase axis is labelled in radians, not dB. A small positive floor
avoids `log10(0)` in the amplification plots.

References: Lab 2, pages 6-7; Lecture 7, pages 18-19;
SciPy's [butter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html)
and [cheby1](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cheby1.html)
documentation.

### Lab Section 7: Frequency-Time Domain Analysis

**Recording setup and current status**

The real recording is not available yet. Save a WAV recording of your own name
as `labbs/lab2/voice.wav`, beside `lab2.py`, then run the same script. The audio
stays local because `voice.wav` is listed in `.gitignore`.

The code reads the file with `wav.read()`, averages stereo channels to mono,
and prints the actual sampling frequency and recording duration. It splits the
samples into complete parts, applies an FFT to each part and squares the FFT
magnitudes. Any incomplete part at the end is left out, as in the example.
The comparison needs at least 2048 samples. Missing or shorter recordings
produce a helpful message while Sections 1-6 still run.

**1. What are X(t,f) and |X(t,f)| squared called?**

X(t,f) is the Short-Time Fourier Transform (STFT). It shows which frequencies
are present at different times. Its squared magnitude is the power spectrum
over time. The picture of this power is called a power spectrogram.

**2. How does changing k affect time and frequency resolution?**

Smaller parts give more detail in time, so changes can be located more closely.
Larger parts give more detail in frequency, but blur when changes happen.
The code compares 512, 1024 and 2048 samples without overlapping the parts.

The actual voice results are **pending**. The table gives the calculations
that will use the recording's sampling frequency, `fs_voice`:

| Samples per part, k | Part duration (seconds) | Frequency spacing (Hz) |
| --- | --- | --- |
| 512 | 512 / fs_voice | fs_voice / 512 |
| 1024 | 1024 / fs_voice | fs_voice / 1024 |
| 2048 | 2048 / fs_voice | fs_voice / 2048 |

These are formulas, not measured voice results. The script prints the numerical
values once the WAV is available. The comparison uses the same time and
frequency ranges. Colours show raw FFT power in dB, so brightness across
different k values should not be treated as a loudness measurement.

**3. Can parts of the spoken name be identified?**

This answer is **pending**. No letters, sounds or syllables have been identified
because the recording is missing. Individual letters may not be clear from a
spectrogram alone. Any sound regions will be described after reviewing the
real recording and its plots.

The following figures will be saved when the recording is available:

- `figures/section7_voice_spectrogram.png`: the teacher's 1024-sample case.
- `figures/section7_window_comparison.png`: the three window lengths.

**Plot correction:** Only the non-negative FFT bins are displayed, including
the Nyquist bin at half the sampling frequency. The frequency row centres
match those bins, and the time axis covers the complete parts. A small value
of `1e-12` avoids `log10(0)`.

**Verification so far:** The complete script runs without a WAV. Numerical
checks using arrays in memory passed for stereo averaging, FFT power, known
frequency peaks, all three k values, plot generation and axes. No audio file
was generated. Loading the real WAV and checking its voice results are still
pending. Section 7 has not been fully experimentally verified.

References: Lab 2, pages 7-9; Lecture 7, pages 25-27.

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
