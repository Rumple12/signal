"""DT081A Lab 2: Sections 1-4 only."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
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

print("Checks passed. Seven figures saved in:", figure_folder)
plt.show()
