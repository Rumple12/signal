"""Lab 2, Section 1: three cosine waves and their FFT."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, fftshift


# Use the teacher's sampling settings and cosine waves.
fs = 250
t = np.arange(0, 0.6, 1/fs)

A1, A2, A3 = 1, 0.1, 0.3
f1, f2, f3 = 50, 55, 120
ph1, ph2, ph3 = 0, np.pi/4, np.pi/2

x = (
    A1 * np.cos(2*np.pi*f1*t + ph1)
    + A2 * np.cos(2*np.pi*f2*t + ph2)
    + A3 * np.cos(2*np.pi*f3*t + ph3)
)

# Keep the raw FFT magnitude, without amplitude normalization.
X = fft(x)
A_x = np.abs(X)
f = fftfreq(len(x), 1/fs)
positive = f >= 0

# Check the sample count and the expected positive and negative peaks.
print(f"Samples: {len(x)}")
print(f"Frequency spacing: {f[1] - f[0]:.4f} Hz")
assert len(x) == 150
for frequency, expected in zip([50, 55, 120], [75, 7.5, 22.5]):
    positive_index = np.argmin(np.abs(f - frequency))
    negative_index = np.argmin(np.abs(f + frequency))
    print(f"{f[positive_index]:g} Hz: {A_x[positive_index]:.4f}; "
          f"{f[negative_index]:g} Hz: {A_x[negative_index]:.4f}")
    assert np.isclose(A_x[positive_index], expected)
    assert np.isclose(A_x[negative_index], expected)
print("All numerical checks matched.")

# One figure: the signal spans the top, with two FFT views below it.
plt.rcParams.update({"font.size": 10, "lines.linewidth": 1.2})
plt.figure(figsize=(9, 5.7))
plt.subplot(2, 2, (1, 2))
plt.plot(t, x, color="#185c4b")
plt.title("(a) Composite signal")
plt.xlabel("Time (s)")
plt.ylabel("Signal amplitude")
plt.xlim(0, 0.6)
plt.grid(alpha=0.25)

# fftshift puts negative and positive frequencies in ascending order.
plt.subplot(2, 2, 3)
plt.plot(fftshift(f), fftshift(A_x), color="#b07130")
plt.title("(b) Two-sided FFT magnitude")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Raw FFT magnitude")
plt.xlim(-fs/2, fs/2)
plt.ylim(0, 80)
plt.grid(alpha=0.25)

plt.subplot(2, 2, 4)
plt.plot(f[positive], A_x[positive], color="#b07130")
plt.title("(c) Positive-frequency FFT magnitude")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Raw FFT magnitude")
plt.xlim(0, fs/2)
plt.ylim(0, 80)
plt.grid(alpha=0.25)

plt.tight_layout()
figure_folder = Path(__file__).resolve().parent.parent / "figures"
figure_folder.mkdir(exist_ok=True)
plt.savefig(figure_folder / "section1_signal_fft.png", dpi=180)
print("Saved section1_signal_fft.png")
plt.show()
