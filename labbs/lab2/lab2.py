"""DT081A Lab 2: Sections 1 and 2 only."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, fftshift
from scipy.signal import windows

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
print("Checks passed. Four figures saved in:", figure_folder)
plt.show()
