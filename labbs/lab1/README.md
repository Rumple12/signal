# Lab 1 - individual implementation and verified draft answers

These are working notes for Phase 2, not the final report. The experiments were
run on 28 October 2026. The three new scripts follow the teacher's examples and
basic course methods. Measurements and figures below come from these new runs.
The previous student's answers and saved results were not copied. The four
existing course TIFF images are reused as inputs, without changing their files.

## Run the experiments

From the repository root:

```text
python -m pip install numpy scipy matplotlib pillow requests scikit-image
python labbs/lab1/signals.py
python labbs/lab1/images.py
python labbs/lab1/audio.py
```

Python 3.12 was used for verification. Each script prints its measurements and
saves figures without opening windows or playing audio. File paths are relative
to the script, so running from another working directory also works.

The image and audio scripts download their examples on the first run. Their
local `data/` cache is ignored by Git. Later runs reuse it. Internet access is
needed when the cache is empty. A descriptive request header is included because
the image server rejected the first request without it. A failed download stops
the script instead of substituting a different experiment.

## Parameters and figure list

- Signals: the teacher's `np.linspace(0, 1, 1000)` time vector. Its sample spacing
  is 1/999 s, so the FFT uses 999 Hz rather than assuming 1000 Hz.
- Random generator: `np.random.default_rng(2026)`, separately in the signal and
  image scripts. Noise results repeat with the same inputs and parameters.
- Images: grayscale values from 0 to 255. All image panels use these same limits.
  PSNR uses floating-point differences and peak value 255. SSIM uses
  `structural_similarity(..., data_range=255)` with its default 7 by 7 window.
- Audio: stereo channels are averaged after conversion to floating point. Each
  complete clip is normalized to its own largest absolute sample. Its cropped
  and downsampled versions keep that normalization. Original recording loudness
  therefore cannot be compared between clips.

| Figure in `figures/` | Questions supported |
|---|---|
| `signal_examples.png` | 1.1 Q1-Q4 |
| `fft_comparison.png` | 1.2 Q1-Q3 |
| `chirp.png` | 1.2 Q4 |
| `sampling_aliasing.png` | 1.3 Q1-Q4 |
| `image_sampling_quantization.png` | 2.1 Q1-Q4; visual comparison for 2.2 |
| `image_types_bicubic.png` | 2.1 Q5-Q6 |
| `image_metrics.png` | 2.2 Q1-Q5 |
| `noise_filtering.png` | 2.3 Q1-Q4 |
| `audio_types.png` | 3.1 Q1-Q2 and Q4 |
| `audio_half_second.png` | 3.1 Q3 |
| `audio_downsampling.png` | 3.1 Q5 |

## 1.1 Signal generation and visualization

**Q1.** The sawtooth is `2 * ((5 * t) % 1) - 1`. Multiplying time by 5 gives
five periods per second. The remainder `% 1` rises from 0 towards 1 and then
starts again. Multiplying by 2 and subtracting 1 gives a ramp from -1 towards +1.

**Q2.** The 20 Hz sine has twice as many cycles as the 10 Hz sine over the same
time. In the 0.2 s detail, there are four cycles instead of two.

**Q3.** The sign and ceil expressions are almost identical on this time grid.
They have 499 positive samples each and differ at one sample: at `t=0`, sign
gives 0, while the ceil expression gives -1. Positive sine values become +1 and
ordinary negative sine values become -1 in both expressions. Ceil does not make
the positive part longer. There is also a special case: if the sine is exactly
-1, the ceil expression gives -3. That case is not present on this sampled grid.

**Q4.** Adding the 10 Hz sine and 5 Hz square wave gives a curved waveform with
jumps at the square-wave transitions. Its measured range is about -1.999999 to
+1.999999. The shape repeats every 0.2 s. These results do not establish a
separate slow beat pattern.

**Q5.** Waveform shape matters in sound generation. A sine gives a single tone,
while square and sawtooth waves contain extra harmonics. A synthesizer can use
these different waveforms to make different sounds.

## 1.2 Fourier transform and frequency-domain analysis

| Component added | Set amplitude | Measured FFT bin |
|---|---:|---:|
| 10 Hz | 1 | 9.990 Hz |
| 20 Hz | 0.5 | 19.980 Hz |
| 30 Hz | 0.25 | 29.970 Hz |

**Q1.** The first signal contains 10 Hz and 20 Hz. Two clear peaks appear near
these frequencies. The FFT bins are slightly offset because the teacher's time
vector includes both ends of the one-second interval.

**Q2.** Setting the added 30 Hz amplitude to 0.25 gives a third peak near 30 Hz.
It is smaller than the peaks from the two larger components.

**Q3.** Gaussian noise with standard deviation 0.2 makes the time trace less
smooth. It also adds small components across the spectrum. The 10 Hz and 20 Hz
peaks remain easy to see in this run. The fixed seed makes this comparison repeat.

**Q4.** The chirp uses `sin(2*pi*(10*t + 0.5*40*t**2))` for a one-second sweep.
Its frequency is `10 + 40*t`, which starts at 10 Hz and ends at 50 Hz. The
duration, rather than the number of samples, sets the sweep rate. A check using
successive phase differences gives 10.0200 to 49.9800 Hz at the interval
midpoints, agreeing with this formula. The time plot becomes more tightly
spaced, and the spectrogram has an upward band. The whole-signal FFT spreads
energy across a frequency range. The spectrogram uses
`10*log10(abs(STFT)**2)` for power in dB, with reference 1. Values are floored
only to avoid taking the logarithm of zero. The STFT window has 256 samples.

**Q5.** An audio equalizer changes selected frequency ranges. The FFT helps show
which frequencies are strong, so we can understand which parts an equalizer
would change.

## 1.3 Sampling and aliasing

| Signal | Sampling rate | Nyquist frequency (`fs/2`) | Matching sampled frequency |
|---|---:|---:|---:|
| 10 Hz | 15 Hz | 7.5 Hz | -5 Hz |
| 10 Hz | 25 Hz | 12.5 Hz | 10 Hz |
| 20 Hz | 30 Hz | 15 Hz | -10 Hz |
| 10 Hz | 11 Hz | 5.5 Hz | -1 Hz |

Negative signs here describe the phase progression of the matching sine. The
usual positive alias frequencies are 5 Hz, 10 Hz, and 1 Hz. The script checks
that the reference and alias give the same values at every sample time.

**Q1.** The Nyquist rate of a 10 Hz sine is `2*10 = 20 Hz`. Sampling at 15 Hz
is below that rate. The samples also match a 5 Hz sine with reversed sign, so
they cannot identify the original 10 Hz wave uniquely.

**Q2.** Sampling at 25 Hz is above 20 Hz. There are more samples per cycle, and
the 10 Hz component is below the 12.5 Hz Nyquist frequency. It does not fold to
a different frequency in this example.

**Q3.** A 20 Hz sine needs a sampling rate above 40 Hz to avoid this ambiguity.
At 30 Hz sampling, it is above the 15 Hz Nyquist frequency. It appears at
`30 - 20 = 10 Hz`, with reversed phase progression for this sine.

**Q4.** Sampling a 10 Hz sine at 11 Hz makes it match a -1 Hz sine at the sample
points. The phase seems to move slowly backwards. This illustrates why a wheel
in a video can appear to turn slowly or backwards even though it rotates fast.
The graph demonstrates the sampled phase effect, rather than an actual wheel.

**Q5.** Fine repeating patterns in photographs can produce false patterns
called moire. This happens when the image sensor cannot sample the fine detail
well enough. Appropriate sampling and filtering help avoid it.

## 2.1 Image sampling and quantization

The main image is the teacher's grayscale Lenna example, 512 by 512 pixels.
Simple resampling keeps every nth pixel and repeats it back to the original
size. Requantization uses the teacher's floor formula.

| Factor and bit depth | Ideal size reduction | Measured PSNR |
|---|---:|---:|
| Factor 2, 6 bpp | 5.33x | 28.1407 dB |
| Factor 2, 4 bpp | 8.00x | 25.6964 dB |
| Factor 4, 6 bpp | 21.33x | 22.6638 dB |
| Factor 4, 4 bpp | 32.00x | 21.8147 dB |

**Q1.** Larger resampling factors make larger blocks and remove more detail.
Factor 2 changes fine edges. Blockiness is clear at factor 4 and stronger at
factor 8 in the saved comparison. What counts as noticeable depends on viewing
size and the person looking at the image.

**Q2.** Resampling removes spatial detail and creates blocks. Requantization
reduces grey levels and creates bands in smooth areas. These are different
effects: one changes detail across pixels, while the other changes pixel values.

**Q3.** The 6 bpp image is close to the original at this display size. Banding
is clear at 4 bpp and very strong at 2 bpp. There are 64, 16, and 4 possible
levels respectively, since the number of levels is `2**bits`. The metric sweep
also checks the other bit depths from 1 to 8. This is an observation about this
image, not a fixed limit for every image.

**Q4.** The combined function applies resampling and then requantization.
Factor 2 with 6 bpp keeps more detail than the other tested combinations and
gives a useful 5.33x ideal reduction. Factor 4 with 6 bpp gives 21.33x but is
more blocky. The ratio is `8*factor**2/bits`, assuming an 8 bpp original and
packed reduced pixels. It does not include file headers. The displayed NumPy
arrays are expanded to full size and are not physically compressed files.

**Q5.** Both methods reduce each dimension by factor 4 and reconstruct to the
original dimensions. The main comparison therefore uses 512 by 512 pixels for
both outputs. The bicubic method uses Pillow's bicubic resize in both directions.
It looks smoother and has fewer block edges, but some fine detail is softened.
Its measured PSNR is 28.8441 dB, compared with 22.7098 dB for simple resampling.
One verified run took 1.504 ms for simple resampling and 4.181 ms for bicubic.
These are single-run times on this computer and will vary. Bicubic does more
calculation to get the smoother result.

**Q6.** All four existing TIFF inputs were loaded and processed. The portrait,
grass, and aerial images are 1024 by 1024; peppers is 512 by 512. Fine grass and
aerial detail is lost during resampling. The portrait also loses texture and
small edges. Bicubic makes these outputs smoother but cannot restore all the
lost detail. Requantization keeps the pixel positions, so much texture remains,
but broad smooth areas show bands. This is especially visible on peppers.

## 2.2 PSNR and SSIM

| Processing of the main image | PSNR | SSIM, range 255 |
|---|---:|---:|
| Simple resampling, factor 4 | 22.709823 dB | 0.658905 |
| Requantization, 4 bpp | 29.207423 dB | 0.883202 |

The error is calculated after converting BOTH images to floating point. Known
checks pass: identical arrays give infinite PSNR, a 0-versus-255 image gives
0 dB, and a constant error of 10 gives `20*log10(255/10) = 28.1308 dB`.

**Q1.** Resampling introduces more distortion according to PSNR in this
comparison, because its PSNR is lower. These are newly calculated values using
the teacher's input. Their agreement with the audit is a check, not a reuse of
the previous student's measurements.

**Q2.** The requantized image also looks closer to the original in the saved
comparison. Its higher PSNR agrees with that observation. PSNR measures average
squared pixel error, so it does not fully describe how a person sees an image.

**Q3.** The script checks factors 1, 2, 4, and 8 at every bit depth from 1 to 8.
Higher bit depths improve PSNR. With resampling, improvement becomes small at
high bit depths because lost spatial detail remains. At 8 bpp, factors 2, 4,
and 8 give 28.2987, 22.7098, and 19.2334 dB. Factor 1 with 8 bpp exactly matches
the original, so its PSNR is infinite and that point cannot be drawn on a finite
vertical axis. More compression generally means more distortion in these tests.

**Q4.** SSIM compares local brightness, contrast, and structure. It can describe
some visible structural changes that a single average pixel-error value misses.
It is another way to measure differences, not a guarantee of human preference.

**Q5.** The standard scikit-image function gives 0.658905 for resampling and
0.883202 for requantization with `data_range=255`. Both metrics favour
requantization in this experiment. They use different scales and calculations.
The parameter plots show that neither extra grey levels nor a high SSIM score
can restore detail removed by spatial resampling.

## 2.3 Noise addition and PSNR

Noise is generated with seed 2026, added in floating point, clipped to 0-255,
and converted to uint8 as in the teacher's example. Very large added noise is
strongly clipped, so its input standard deviation is not the standard deviation
of the final pixel errors.

| Added noise standard deviation | Measured PSNR |
|---|---:|
| 2 | 41.746800 dB |
| 5 | 34.108573 dB |
| 10 | 28.101160 dB |
| 20 | 22.133699 dB |
| 50 | 14.629918 dB |
| 150 | 8.463939 dB |
| 500 | 6.244537 dB |
| Same sd=20 image, then Gaussian sigma=1 | 30.076583 dB |

**Q1.** Slight grain can be seen in smooth areas at standard deviation 5,
around 34.11 dB in this run. It is much clearer at standard deviation 20.
This is a visual observation, not a universal threshold.

**Q2.** About 34.11 dB lies inside the quoted 30-50 dB range. An image in that
range can still show noise. The type of distortion and image content also matter.

**Q3.** At standard deviation 150, the image is badly damaged but its main shape
is still visible. At 500, around 6.24 dB, the content becomes difficult to
recognize in this comparison. Faint shapes can remain, so this is not an exact
boundary between recognizable and unrecognizable images.

**Q4.** Gaussian filtering with sigma 1 changes the same sd=20 noisy image from
22.133699 to 30.076583 dB. It reduces grain by averaging nearby values. The
result looks cleaner, but fine texture and edges become softer. PSNR is measured
against the original clean image before and after filtering. The filter receives
floating-point pixels, avoiding unnecessary rounding during filtering.

**Q5.** Non-Local Means compares small image patches and averages information
from similar patches. It can keep texture and edges better than simply averaging
all nearby pixels. It needs more calculation and suitable settings. Only this
description is required; the advanced filter is not implemented.

## 3.1 Audio signal analysis

All three sources loaded successfully. The full clips were analyzed for the
type comparison. Stereo averaging is used for piano and speech; rain is mono.

| Clip | Sampling rate | Full/analyzed duration | Strongest full-clip FFT peak | Highest bin meeting the 1% rule |
|---|---:|---:|---:|---:|
| Piano note | 44100 Hz | 0.501791 s | 219.214605 Hz | 4832.685616 Hz |
| Rain | 22050 Hz | 30.030068 s | 272.560155 Hz | 11021.153855 Hz |
| Speech | 44100 Hz | 1.301315 s | 290.475361 Hz | 15737.155851 Hz |

For the last column, a bin is counted when its amplitude is at least 1% of the
strongest non-DC bin. DC means the zero-frequency average. This is a declared
measurement rule, not an exact upper limit of the sound. Smaller components,
noise, and effects from cutting a finite clip may extend higher. The Nyquist
frequencies are 22050 Hz for piano/speech and 11025 Hz for rain.

**Q1.** The selected speech file lasts 1.301315 s. Its strongest FFT peak is
290.475361 Hz. The highest bin passing the stated 1% rule is about 15.737 kHz,
which is a different measurement. A strong low-frequency peak must not be
reported as the highest frequency present. The table records the other clips
separately, so their results are not mixed.

**Q2.** The waveform shows amplitude changes and quiet parts over time. In the
speech spectrogram, the stronger sections contain several bands, with quieter
gaps between them. The spectrum shows which frequencies contribute to the whole
clip. Brighter spectrogram areas mean greater power at that frequency and time.
The plots use a 1024-sample window and 512-sample overlap. The colour scale is
-100 to -20 dB/Hz relative to squared normalized amplitude. The thin band near
15.7 kHz is present in the recording, but its cause was not identified.

**Q3.** The first-half-second analysis uses exactly 22050 samples at 44100 Hz.
Its duration is 0.500000 s, compared with 1.301315 s for the full speech file.
FFT bin spacing changes from 0.768453 Hz to 2 Hz. The strongest peak stays near
290 Hz, but peak strengths and other components change because the crop contains
only the beginning. The full and cropped spectra use the same amplitude scale.
Their detailed plots show 0-6000 Hz; the full range is in the audio-type figure.

**Q4.** The piano note has a regular waveform that fades, clear spectral peaks,
and horizontal harmonic bands. Rain is less periodic and spreads energy across
a broad frequency range. Its strongest single FFT bin does not mean it has a
stable musical pitch. Speech has changing bursts and gaps, and its frequency
bands change with time. These observations come from the three loaded clips and
their plots. No listening test or identification of spoken words was performed.

**Q5.** Downsampling keeps every nth sample and divides the sampling rate by n.
Speech was tested at 44100, 22050, 14700, and 7350 Hz. The waveform has fewer
points, and its spectrum ends at the new Nyquist frequency. Its main low-frequency
peak remains near 290 Hz. The full recording also contains frequencies above
the reduced Nyquist limits, which fold into lower frequencies when samples are
dropped without filtering. A low-pass filter is normally needed before reducing
the sampling rate; it is deliberately omitted in this aliasing demonstration.

The known 2500 Hz sine makes the effect clear:

| Sampling rate after downsampling | Nyquist frequency | Measured FFT peak |
|---|---:|---:|
| 12000 Hz | 6000 Hz | 2500 Hz |
| 6000 Hz | 3000 Hz | 2500 Hz |
| 4000 Hz | 2000 Hz | 1500 Hz |
| 2000 Hz | 1000 Hz | 500 Hz |

The tone needs sampling above 5000 Hz. Aliasing is visible at 4000 Hz in these
tests, where the original tone exceeds the 2000 Hz Nyquist frequency. It folds
to 1500 Hz, then to 500 Hz at 2000 Hz sampling. The script checks these measured
peaks against the alias formula. These are observable signal changes; no claim
is made about the exact point where a listener would notice reduced quality.

**Q6.** Spectral noise reduction estimates background noise at each frequency,
for example from a quiet part of the recording. An FFT gives the signal's
frequency components. The noise estimate can be used to reduce their magnitudes
while keeping the signal phases. An inverse FFT changes the result back to a
time signal. This can reduce noise, but it can also damage quiet wanted sounds.

## Three concluding discussion questions

**1. Sampling and quantization across signals.** Sampling chooses positions or
times: time points for 1D signals and audio, and pixel positions for images.
Quantization chooses a limited set of amplitude or grey-level values. Too few
samples lose detail or cause aliasing. Too few levels cause rounding errors.

**2. Image and audio processing.** Both use sampling, quantization, Fourier
analysis, and filtering. Images have two spatial directions, while mono audio
changes along one time direction. Image changes are seen as changes in detail
and tone; audio changes affect the represented waveform and frequency content.

**3. Applications.** Communication systems need suitable sampling to preserve
signals. Medical images need enough detail and controlled noise to show useful
features. Multimedia systems balance stored data size against picture and sound
quality. The experiments show why that balance involves some loss of information.

## Verification and sources

- All three scripts completed successfully with their simple numerical checks.
- All 37 numbered questions and the three discussion questions are covered above.
- Eleven figures were generated and visually inspected. Noise values in the
  figures agree with the printed measurements.
- PSNR checks include identical pixels, maximum uint8 differences, and a known
  constant error. FFT peaks, chirp phase changes, alias sample values, image sizes,
  half-second sample counts, and downsampled tone peaks were checked.
- The previous student's files, Lab 2, and Lab 3 were checked against their
  original file hashes and remain unchanged.
- All inputs were available. No private voice recordings were used. Downloaded
  source files remain local and ignored by Git. No final report has been created.
- Timings vary by run. Visual noise thresholds are subjective. Audio conclusions
  describe calculated and plotted results, not listening judgements.

Sources:

- Teacher: [Lab 1 instructions](../DT081A%20Signal%20and%20Image%20Processing%20-%20Lab%201%20%281%29.pdf),
  version 1.0, 18 September 2024. The teacher's sampling and quantization formulas
  are used; floating-point PSNR and the duration-based chirp avoid the audited errors.
- Image input: [Lenna supplied by the teacher](https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png).
  The other four TIFF inputs are in `../DT081A_Labs-main/DT081A_Labs-main/images/`.
- Audio: [piano note](https://raw.githubusercontent.com/parisjava/wav-piano-sound/master/wav/a1.wav),
  [rain](https://www.pacdv.com/sounds/ambience_sounds/rain_2.wav),
  [speech](https://www.pacdv.com/sounds/voices/can-you-keep-a-secret.wav).
- [scikit-image SSIM documentation](https://scikit-image.org/docs/stable/api/skimage.metrics.html#skimage.metrics.structural_similarity).
- [Non-Local Means explanation](https://scikit-image.org/docs/stable/auto_examples/filters/plot_nonlocal_means.html).
