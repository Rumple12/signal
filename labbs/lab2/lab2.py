"""DT081A Lab 2: Sections 1-7. The two voice recordings and their figures stay local."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
from scipy import signal
from scipy.fft import fft, fftfreq, fftshift
from scipy.signal import lfilter, windows

# Save figures beside this script, even when running from another folder.
figure_folder = Path(__file__).resolve().parent / "figures"
figure_folder.mkdir(exist_ok=True)

# Section 1: use the teacher's sampling values and three cosine waves.
fs = 250
# The PDF also says 0.4 seconds, but its Python example uses 0.6 seconds.
t = np.arange(0, 0.6, 1/fs)

A1, A2, A3 = 1, 0.1, 0.3
f1, f2, f3 = 50, 55, 120
ph1, ph2, ph3 = 0, np.pi/4, np.pi/2

x = (
    A1 * np.cos(2 * np.pi * f1 * t + ph1)
    + A2 * np.cos(2 * np.pi * f2 * t + ph2)
    + A3 * np.cos(2 * np.pi * f3 * t + ph3)
)

plt.figure(figsize=(9, 3.5))
plt.plot(t, x)
plt.title("Section 1: Time-domain signal")
plt.xlabel("Time (s)")
plt.ylabel("Signal amplitude")
plt.xlim(0, 0.6)
plt.grid()
plt.tight_layout()
plt.savefig(figure_folder / "section1_time_domain.png", dpi=150)

# Calculate the FFT and its magnitude, just as in the teacher's example.
N = len(x)
X = fft(x)
A_x = np.abs(X)
f = fftfreq(N, 1/fs)

plt.figure(figsize=(9, 3.5))
# fftshift puts the frequencies in order from negative to positive.
plt.plot(fftshift(f), fftshift(A_x))
plt.title("Section 1: Two-sided amplitude spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Raw FFT magnitude")
plt.xlim(-fs/2, fs/2)
plt.grid()
plt.tight_layout()
plt.savefig(figure_folder / "section1_two_sided_fft.png", dpi=150)

# Keep the same positive-frequency half used in the PDF (including 0 Hz).
f_positive = f[:N//2]
A_positive = A_x[:N//2]

plt.figure(figsize=(9, 3.5))
plt.plot(f_positive, A_positive, ".-")
plt.title("Section 1: Positive-frequency amplitude spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Raw FFT magnitude")
plt.xlim(0, fs/2)
plt.grid()
plt.tight_layout()
plt.savefig(figure_folder / "section1_positive_fft.png", dpi=150)

# Basic checks: 150 samples and the three expected FFT peaks.
assert N == 150
assert np.allclose(np.diff(t), 1/fs)
assert fs > 2 * max(f1, f2, f3)
# A threshold of 1 keeps the three peaks and ignores tiny rounding errors.
peak_frequencies = f_positive[A_positive > 1]
peak_magnitudes = A_positive[A_positive > 1]
assert np.allclose(peak_frequencies, [f1, f2, f3])
assert np.allclose(peak_magnitudes, [75, 7.5, 22.5])
print(f"Samples: {N}; record length: {N/fs:.1f} s; last sample: {t[-1]:.3f} s")
print(f"FFT bin spacing: {fs/N:.3f} Hz")
print("Frequency peaks (Hz):", peak_frequencies)
print("Raw FFT magnitudes:", peak_magnitudes)

# Section 2: leaving x unchanged is the rectangular window.
# Use the exact Hann and Hamming functions from the teacher's example.
x_hn = x * windows.hann(len(x))
x_hm = x * windows.hamming(len(x))
X_hn = fft(x_hn)
X_hm = fft(x_hm)
A_hn = np.abs(X_hn)
A_hm = np.abs(X_hm)

window_names = ["Rectangular", "Hann", "Hamming"]
window_spectra = [A_x, A_hn, A_hm]

plt.figure(figsize=(11, 9))
for i in range(3):
    spectrum = window_spectra[i][:N//2]

    # Left: full positive-frequency spectra on the same raw magnitude scale.
    plt.subplot(3, 2, 2*i + 1)
    plt.plot(f_positive, spectrum, ".-")
    plt.title(window_names[i] + ": full spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Raw FFT magnitude")
    plt.xlim(0, fs/2)
    plt.ylim(0, 80)
    plt.grid()

    # Right: zoom in and give each highest peak a height of 1.
    # This makes the peak widths easier to compare despite window attenuation.
    plt.subplot(3, 2, 2*i + 2)
    plt.plot(f_positive, spectrum / np.max(spectrum), ".-")
    plt.title(window_names[i] + ": 50 and 55 Hz detail")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude / highest peak")
    plt.xlim(45, 60)
    plt.ylim(0, 1.1)
    plt.xticks([45, 50, 55, 60])
    plt.grid()

    print(window_names[i] + " raw magnitudes at 50, 55 and 120 Hz:",
          np.round(spectrum[A_positive > 1], 4))

plt.tight_layout()
plt.savefig(figure_folder / "section2_window_spectra.png", dpi=150)

# Section 3.1: convolve the given impulse response with a unit impulse.
h = [1, 0.5, 0.3, 0.1, -0.1, -0.4, -0.2, 0.1]
impulse1 = np.zeros(len(x))
impulse1[0] = 1
response1 = np.convolve(h, impulse1)

# The response should be h followed by zeros. Full convolution adds lengths - 1.
assert len(response1) == len(h) + len(impulse1) - 1
assert np.allclose(response1[:len(h)], h)
assert np.allclose(response1[len(h):], 0)
print("System 1 output length:", len(response1))
print("System 1 first eight samples:", response1[:len(h)])

plt.figure(figsize=(9, 3.5))
# Modern Matplotlib uses plt.stem() without use_line_collection.
plt.stem(response1)
# Zoom in so the eight non-zero values are easy to see. The rest are zero.
plt.xlim(-1, 20)
plt.xticks(range(0, 21, 2))
plt.title("Section 3.1: System 1 impulse response (first 21 samples)")
plt.xlabel("Sample index")
plt.ylabel("Amplitude")
plt.grid()
plt.tight_layout()
plt.savefig(figure_folder / "section3_system1_convolution.png", dpi=150)

# Section 3.2: use the same 100-sample impulse for both implementations.
b = [1, 0.3]
a = [1, 0.6, -0.35]
impulse2 = np.zeros(100)
impulse2[0] = 1
y_manual = np.zeros(len(impulse2))

# Correct the PDF's last index to n-2, matching the lfilter coefficients:
# y[n] = x[n] + 0.3*x[n-1] - 0.6*y[n-1] + 0.35*y[n-2].
for n in range(len(impulse2)):
    y_manual[n] = b[0] * impulse2[n]
    # Skip terms before sample 0, since their input and output values are zero.
    if n >= 1:
        y_manual[n] += b[1] * impulse2[n-1] - a[1] * y_manual[n-1]
    if n >= 2:
        y_manual[n] -= a[2] * y_manual[n-2]

y_filter = lfilter(b, a, impulse2)
same_response = np.allclose(y_manual, y_filter)
assert np.allclose(y_manual[:5], [1, -0.3, 0.53, -0.423, 0.4393])
assert same_response
print("System 2 first five samples:", np.round(y_manual[:5], 4))
print("System 2 manual loop matches lfilter:", same_response)
print("System 2 largest absolute difference:", np.max(np.abs(y_manual - y_filter)))

plt.figure(figsize=(9, 6))
plt.subplot(2, 1, 1)
plt.stem(y_manual)
plt.title("Section 3.2: System 2 - manual loop")
plt.xlabel("Sample index")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(y_filter)
plt.title("Section 3.2: System 2 - SciPy lfilter")
plt.xlabel("Sample index")
plt.ylabel("Amplitude")
plt.grid()
plt.tight_layout()
plt.savefig(figure_folder / "section3_system2_comparison.png", dpi=150)

# Section 4: reuse x, X and the amplitude spectrum from Section 1.
phase_x = np.angle(X)

# Find the three positive-frequency peaks using their calculated magnitudes.
component_indices = np.where(A_positive > 1)[0]
measured_frequencies = f[component_indices]
measured_amplitudes = 2 * np.abs(X[component_indices]) / len(x)
measured_phases = phase_x[component_indices]

assert np.allclose(measured_frequencies, [f1, f2, f3])
assert np.allclose(measured_amplitudes, [A1, A2, A3])
assert np.allclose(measured_phases, [ph1, ph2, ph3])
print("Section 4 frequencies (Hz):", measured_frequencies)
print("Section 4 cosine amplitudes:", measured_amplitudes)
print("Section 4 phases (rad):", measured_phases)

# Hide phase values where the FFT magnitude is nearly zero.
# Only the plotting copy changes; phase_x keeps all calculated values.
phase_plot = phase_x[:N//2].copy()
phase_plot[A_positive < 1] = np.nan

plt.figure(figsize=(11, 4))
plt.subplot(1, 2, 1)
plt.plot(f_positive, A_positive, ".-")
plt.title("Section 4: Amplitude spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Raw FFT magnitude")
plt.xlim(0, fs/2)
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(f_positive, phase_plot, "o")
plt.title("Section 4: Phase spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.xlim(0, fs/2)
plt.ylim(-np.pi, np.pi)
plt.grid()
plt.tight_layout()
plt.savefig(figure_folder / "section4_amplitude_phase.png", dpi=150)

# Section 5: find System 2's frequency response from a 150-sample impulse.
impulse_system2 = np.zeros(len(x))
impulse_system2[0] = 1
h_system2 = lfilter(b, a, impulse_system2)
H = fft(h_system2)

# The first 100 samples should match the impulse response from Section 3.
assert len(h_system2) == len(x)
assert np.allclose(h_system2[:len(y_filter)], y_filter)

plt.figure(figsize=(11, 4))
plt.subplot(1, 2, 1)
plt.plot(f_positive, np.abs(H[:N//2]))
plt.title("Section 5: System 2 amplification")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplification (output / input)")
plt.xlim(0, fs/2)
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(f_positive, np.angle(H[:N//2]))
plt.title("Section 5: System 2 phase shift")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase shift (radians)")
plt.xlim(0, fs/2)
plt.grid()
plt.tight_layout()
plt.savefig(figure_folder / "section5_system_frequency_response.png", dpi=150)

# Pass the teacher's single 50 Hz cosine through the same system.
x2 = A1 * np.cos(2 * np.pi * f1 * t + ph1)
y3 = lfilter(b, a, x2)
X2 = fft(x2)
Y3 = fft(y3)
A_x2 = np.abs(X2)
A_y3 = np.abs(Y3)
phase_x2 = np.angle(X2)
phase_y3 = np.angle(Y3)

# Find the strongest positive-frequency component in each signal.
input_index = np.argmax(A_x2[:N//2])
output_index = np.argmax(A_y3[:N//2])
input_frequency = f[input_index]
output_frequency = f[output_index]
input_amplitude = 2 * A_x2[input_index] / len(x)
output_amplitude = 2 * A_y3[output_index] / len(x)
input_phase = phase_x2[input_index]
output_phase = phase_y3[output_index]
assert np.allclose([input_frequency, output_frequency], [f1, f1])
assert np.isclose(input_amplitude, A1)
assert np.isclose(input_phase, ph1)

# At the same frequency, multiply amplitudes and add phases to predict output.
system_gain = np.abs(H[input_index])
system_phase_shift = np.angle(H[input_index])
predicted_amplitude = input_amplitude * system_gain
predicted_phase = input_phase + system_phase_shift
amplitude_difference = output_amplitude - predicted_amplitude
phase_difference = output_phase - predicted_phase
amplitude_difference_percent = 100 * amplitude_difference / predicted_amplitude

print("Section 5 input frequency, amplitude, phase:",
      input_frequency, input_amplitude, input_phase)
print("Section 5 output frequency, amplitude, phase:",
      output_frequency, output_amplitude, output_phase)
print("System amplification and phase shift at 50 Hz:", system_gain, system_phase_shift)
print("Predicted output amplitude and phase:", predicted_amplitude, predicted_phase)
# Finite signals and the filter's start-up effect cause small differences.
print("Measured minus predicted amplitude:", amplitude_difference)
print("Measured minus predicted phase (rad):", phase_difference)
print("Amplitude difference (% of prediction):", amplitude_difference_percent)

# Hide phase only where the magnitude is almost zero from rounding errors.
phase_x2_plot = phase_x2[:N//2].copy()
phase_y3_plot = phase_y3[:N//2].copy()
phase_x2_plot[A_x2[:N//2] < 1e-8] = np.nan
phase_y3_plot[A_y3[:N//2] < 1e-8] = np.nan

plt.figure(figsize=(11, 4))
plt.subplot(1, 2, 1)
plt.plot(f_positive, A_x2[:N//2], ".-", label="Input")
plt.plot(f_positive, A_y3[:N//2], "x-", label="Output")
plt.title("Section 5: Input and output spectra")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Raw FFT magnitude")
plt.xlim(0, fs/2)
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(f_positive, phase_x2_plot, "o", label="Input")
plt.plot(f_positive, phase_y3_plot, "x", label="Output")
plt.title("Section 5: Input and output phases")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.xlim(0, fs/2)
plt.ylim(-np.pi, np.pi)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(figure_folder / "section5_input_output_spectra.png", dpi=150)

# Section 6: use the teacher's filter settings and a separate frequency axis.
fs1 = 2500
fc = 200
filter_order = 5  # The teacher calls this N; N above is the signal sample count.
Rp = 3

# Give the filters enough samples to settle before taking the FFT.
filter_samples = 1000
filter_impulse = np.zeros(filter_samples)
filter_impulse[0] = 1
filter_half = filter_samples // 2
f_filter = fftfreq(filter_samples, 1/fs1)
f_filter_positive = f_filter[:filter_half]

b_b, a_b = signal.butter(filter_order, fc, btype="low", fs=fs1)
b_c1, a_c1 = signal.cheby1(filter_order, Rp, fc, btype="low", fs=fs1)
h_b = lfilter(b_b, a_b, filter_impulse)
h_c1 = lfilter(b_c1, a_c1, filter_impulse)
H_b = fft(h_b)
H_c1 = fft(h_c1)

plt.figure(figsize=(11, 4))
for response, name in zip([H_b, H_c1], ["Butterworth", "Chebyshev I"]):
    magnitude = np.abs(response[:filter_half])
    # A small floor avoids log10(0). Phase near zero magnitude is hidden.
    gain_db = 20 * np.log10(np.maximum(magnitude, 1e-12))
    phase = np.angle(response[:filter_half])
    phase[magnitude < 1e-8] = np.nan
    plt.subplot(1, 2, 1)
    plt.plot(f_filter_positive, gain_db, label=name)
    plt.subplot(1, 2, 2)
    plt.plot(f_filter_positive, phase, label=name)

plt.subplot(1, 2, 1)
plt.title("Section 6: Low-pass filters, order 5, 200 Hz")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplification (dB)")
plt.xlim(0, 750)
plt.ylim(-100, 3)
plt.legend()
plt.grid()
plt.subplot(1, 2, 2)
plt.title("Section 6: Low-pass phase shifts")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase shift (radians)")
plt.xlim(0, 750)
plt.ylim(-np.pi, np.pi)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(figure_folder / "section6_butterworth_chebyshev.png", dpi=150)

# Change one setting at a time, using Butterworth for these comparisons.
b_high, a_high = signal.butter(filter_order, fc, btype="high", fs=fs1)
b_350, a_350 = signal.butter(filter_order, 350, btype="low", fs=fs1)
b_order3, a_order3 = signal.butter(3, fc, btype="low", fs=fs1)
b_order7, a_order7 = signal.butter(7, fc, btype="low", fs=fs1)
H_high = fft(lfilter(b_high, a_high, filter_impulse))
H_350 = fft(lfilter(b_350, a_350, filter_impulse))
H_order3 = fft(lfilter(b_order3, a_order3, filter_impulse))
H_order7 = fft(lfilter(b_order7, a_order7, filter_impulse))

variation_titles = ["Low-pass versus high-pass", "Cutoff frequency", "Filter order"]
variation_responses = [[H_b, H_high], [H_b, H_350], [H_order3, H_order7]]
variation_labels = [["Low-pass", "High-pass"], ["200 Hz", "350 Hz"], ["Order 3", "Order 7"]]

plt.figure(figsize=(11, 9))
for row in range(3):
    for i in range(2):
        response = variation_responses[row][i][:filter_half]
        name = variation_labels[row][i]
        magnitude = np.abs(response)
        gain_db = 20 * np.log10(np.maximum(magnitude, 1e-12))
        phase = np.angle(response)
        phase[magnitude < 1e-8] = np.nan
        plt.subplot(3, 2, 2*row + 1)
        plt.plot(f_filter_positive, gain_db, label=name)
        plt.subplot(3, 2, 2*row + 2)
        plt.plot(f_filter_positive, phase, label=name)

    plt.subplot(3, 2, 2*row + 1)
    plt.title(variation_titles[row] + ": amplification")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplification (dB)")
    plt.xlim(0, 750)
    plt.ylim(-100, 3)
    plt.legend()
    plt.grid()
    plt.subplot(3, 2, 2*row + 2)
    plt.title(variation_titles[row] + ": phase")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase shift (radians)")
    plt.xlim(0, 750)
    plt.ylim(-np.pi, np.pi)
    plt.legend()
    plt.grid()

plt.tight_layout()
plt.savefig(figure_folder / "section6_filter_variations.png", dpi=150)

# Band-pass and band-stop use two cutoff frequencies.
band = [150, 400]
b_bp, a_bp = signal.butter(filter_order, band, btype="bandpass", fs=fs1)
b_bs, a_bs = signal.butter(filter_order, band, btype="bandstop", fs=fs1)
H_bp = fft(lfilter(b_bp, a_bp, filter_impulse))
H_bs = fft(lfilter(b_bs, a_bs, filter_impulse))

plt.figure(figsize=(11, 4))
for response, name in zip([H_bp, H_bs], ["Band-pass", "Band-stop"]):
    magnitude = np.abs(response[:filter_half])
    gain_db = 20 * np.log10(np.maximum(magnitude, 1e-12))
    phase = np.angle(response[:filter_half])
    phase[magnitude < 1e-8] = np.nan
    plt.subplot(1, 2, 1)
    plt.plot(f_filter_positive, gain_db, label=name)
    plt.subplot(1, 2, 2)
    plt.plot(f_filter_positive, phase, label=name)

plt.subplot(1, 2, 1)
plt.title("Section 6: Band filters, 150-400 Hz")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplification (dB)")
plt.xlim(0, 750)
plt.ylim(-100, 3)
plt.legend()
plt.grid()
plt.subplot(1, 2, 2)
plt.title("Section 6: Band-filter phase shifts")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase shift (radians)")
plt.xlim(0, 750)
plt.ylim(-np.pi, np.pi)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(figure_folder / "section6_bandpass_bandstop.png", dpi=150)

# Basic checks of the frequency axis, settling and filter behaviour.
assert np.isclose(f_filter_positive[1], 2.5)
assert np.isclose(f_filter_positive[-1], 1247.5)
assert np.max(np.abs(h_b[-20:])) < 1e-8
assert np.max(np.abs(h_c1[-20:])) < 1e-8
index50 = np.argmin(np.abs(f_filter_positive - 50))
index100 = np.argmin(np.abs(f_filter_positive - 100))
index250 = np.argmin(np.abs(f_filter_positive - 250))
index300 = np.argmin(np.abs(f_filter_positive - 300))
index600 = np.argmin(np.abs(f_filter_positive - 600))
assert np.abs(H_b[index50]) > 0.9 and np.abs(H_b[index600]) < 0.01
assert np.abs(H_high[index50]) < 0.01 and np.abs(H_high[index600]) > 0.9
assert np.abs(H_350[index300]) > np.abs(H_b[index300])
assert np.abs(H_order7[index300]) < np.abs(H_order3[index300])
assert np.abs(H_bp[index250]) > 0.9
assert np.abs(H_bp[index50]) < 0.01 and np.abs(H_bp[index600]) < 0.1
assert np.abs(H_bs[index250]) < 0.01
assert np.abs(H_bs[index50]) > 0.9 and np.abs(H_bs[index600]) > 0.9

passband_magnitude = np.abs(H_c1[:filter_half])[f_filter_positive <= fc]
passband_db = 20 * np.log10(np.maximum(passband_magnitude, 1e-12))
assert np.min(passband_db) >= -Rp - 1e-6
assert np.max(passband_db) <= 1e-6
print("Section 6 sampling frequency and FFT spacing (Hz):", fs1, fs1/filter_samples)
print("Chebyshev passband minimum and maximum (dB):", passband_db.min(), passband_db.max())
print("Filter: amplification at 300 Hz (dB), phase at 100 Hz (radians)")
check_names = ["Butterworth LP 200 order 5", "Chebyshev LP 200 order 5",
               "Butterworth HP 200 order 5", "Butterworth LP 350 order 5",
               "Butterworth LP 200 order 3", "Butterworth LP 200 order 7"]
check_responses = [H_b, H_c1, H_high, H_350, H_order3, H_order7]
for name, response in zip(check_names, check_responses):
    print(name, 20*np.log10(np.abs(response[index300])), np.angle(response[index100]))
band_indices = [index50, index250, index600]
print("Band-pass amplification at 50, 250, 600 Hz (dB):",
      20*np.log10(np.maximum(np.abs(H_bp[band_indices]), 1e-12)))
print("Band-stop amplification at 50, 250, 600 Hz (dB):",
      20*np.log10(np.maximum(np.abs(H_bs[band_indices]), 1e-12)))

print("Checks passed. Twelve figures saved in:", figure_folder)

# Section 7: process each student's recording with the same calculations.
students = ["Jakob", "Obid"]
comparison_names = []
comparison_images = []
comparison_extents = []
comparison_sample_rates = []
for student in students:
    voice_path = Path(__file__).resolve().parent / (student.lower() + ".wav")
    if not voice_path.exists():
        print(student + " analysis pending: put the WAV recording at", voice_path)
        continue
    fs_voice, x_voice = wav.read(voice_path)
    # Average the channels if the recording is stereo, as in the example.
    if len(x_voice.shape) == 2:
        x_voice = np.mean(x_voice, axis=1)
        print(student + ": converted the recording to mono.")
    recording_duration = len(x_voice) / fs_voice
    print(student + " sampling frequency:", fs_voice, "Hz")
    print(f"{student} recording duration: {recording_duration:.6f} s")

    if len(x_voice) < 2048:
        print(student + ": record a longer WAV; the comparison needs at least 2048 samples.")
        continue
    window_lengths = [512, 1024, 2048]
    voice_power_db = []
    voice_frequencies = []
    voice_time_ends = []
    for k in window_lengths:
        # Split the recording into complete, non-overlapping parts.
        n = len(x_voice) // k
        xm_xvoice = x_voice[:n*k].reshape(n, k)
        # Compute the FFT and squared magnitude for each part.
        Xvoice = np.fft.fft(xm_xvoice, axis=1)
        power_spectrum = np.abs(Xvoice) ** 2
        # Keep 0 Hz through Nyquist, rather than the negative frequencies.
        positive_power = power_spectrum[:, :k//2 + 1]
        frequencies = np.fft.rfftfreq(k, d=1/fs_voice)
        voice_power_db.append(10 * np.log10(positive_power + 1e-12))
        voice_frequencies.append(frequencies)
        voice_time_ends.append(n*k / fs_voice)
        print(f"{student}, k = {k}: {k/fs_voice:.6f} s per part, {fs_voice/k:.3f} Hz per bin")

    # The middle result uses k = 1024, as in the teacher's example.
    k = 1024
    frequency_spacing = fs_voice / k
    frequencies = voice_frequencies[1]
    # Half-bin edges place the first and last row centres at 0 Hz and Nyquist.
    extent = [0, voice_time_ends[1], -frequency_spacing/2,
              frequencies[-1] + frequency_spacing/2]
    comparison_names.append(student)
    comparison_images.append(voice_power_db[1])
    comparison_extents.append(extent)
    comparison_sample_rates.append(fs_voice)
    plt.figure(figsize=(10, 4.5))
    plt.imshow(voice_power_db[1].T, origin="lower", aspect="auto",
               extent=extent, cmap="viridis")
    plt.ylim(0, fs_voice/2)
    plt.colorbar(label="Power (dB, raw FFT)")
    plt.title(f"Section 7: {student}'s spectrogram (k = 1024)")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency (Hz)")
    plt.tight_layout()
    plt.savefig(figure_folder / f"section7_{student.lower()}_spectrogram.png", dpi=150)

    # Show all three choices over the same time and frequency ranges.
    common_end = min(voice_time_ends)
    plt.figure(figsize=(10, 9))
    for i in range(len(window_lengths)):
        k = window_lengths[i]
        frequency_spacing = fs_voice / k
        frequencies = voice_frequencies[i]
        extent = [0, voice_time_ends[i], -frequency_spacing/2,
                  frequencies[-1] + frequency_spacing/2]
        plt.subplot(3, 1, i + 1)
        plt.imshow(voice_power_db[i].T, origin="lower", aspect="auto",
                   extent=extent, cmap="viridis")
        plt.xlim(0, common_end)
        plt.ylim(0, fs_voice/2)
        plt.colorbar(label="Power (dB, raw FFT)")
        plt.title(f"{student}, k = {k}: {1000*k/fs_voice:.2f} ms per part, {fs_voice/k:.2f} Hz per bin")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Frequency (Hz)")
    plt.tight_layout()
    plt.savefig(figure_folder / f"section7_{student.lower()}_window_comparison.png", dpi=150)
    print(student + ": two private spectrogram figures saved in", figure_folder)

# Plot Jakob on the left and Obid on the right when both are available.
if len(comparison_images) == 2:
    colour_min = min(comparison_images[0].min(), comparison_images[1].min())
    colour_max = max(comparison_images[0].max(), comparison_images[1].max())
    plt.figure(figsize=(12, 4.5))
    for i in range(2):
        plt.subplot(1, 2, i + 1)
        plt.imshow(comparison_images[i].T, origin="lower", aspect="auto",
                   extent=comparison_extents[i], cmap="viridis",
                   vmin=colour_min, vmax=colour_max)
        plt.ylim(0, comparison_sample_rates[i]/2)
        plt.colorbar(label="Power (dB, raw FFT)")
        plt.title(comparison_names[i] + " (k = 1024)")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Frequency (Hz)")
    plt.tight_layout()
    plt.savefig(figure_folder / "section7_jakob_obid_comparison.png", dpi=150)
    print("Private side-by-side comparison saved in", figure_folder)
else:
    print("Side-by-side comparison pending until both recordings can be analysed.")

plt.show()
