"""Lab 2, Section 2: compare rectangular, Hann and Hamming windows."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import windows


# Keep the teacher's 0.6-second time vector (the prose mentions 0.4 seconds).
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

# The unchanged signal has a rectangular window.
x_hann = x * windows.hann(len(x))
x_hamming = x * windows.hamming(len(x))

# Use raw FFT magnitudes, with no normalization.
A_rectangular = np.abs(fft(x))
A_hann = np.abs(fft(x_hann))
A_hamming = np.abs(fft(x_hamming))
f = fftfreq(len(x), 1/fs)
positive = f >= 0

names = ["Rectangular", "Hann", "Hamming"]
magnitudes = [A_rectangular, A_hann, A_hamming]

# Print the actual values at the two nearby frequency components.
print(f"Samples: {len(x)}; frequency spacing: {f[1] - f[0]:.4f} Hz")
for name, magnitude in zip(names, magnitudes):
    index_50 = np.argmin(np.abs(f - 50))
    index_55 = np.argmin(np.abs(f - 55))
    print(f"{name}: 50 Hz = {magnitude[index_50]:.4f}; "
          f"55 Hz = {magnitude[index_55]:.4f}")

# One figure with a full view and a closer view of the nearby peaks.
plt.rcParams.update({"font.size": 10, "lines.linewidth": 1.4})
plt.figure(figsize=(9, 6.6))
styles = ["-", "--", "-."]
colours = ["#185c4b", "#b07130", "#435d99"]
for panel, (limits, title) in enumerate([
        ((0, 125), "Window comparison: positive-frequency spectra"),
        ((43, 65), "Nearby components: 50 Hz and 55 Hz")], start=1):
    plt.subplot(2, 1, panel)
    for name, magnitude, style, colour in zip(names, magnitudes, styles, colours):
        plt.plot(f[positive], magnitude[positive], linestyle=style,
                 marker="o" if panel == 2 else None, markersize=3,
                 color=colour, label=name)
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Raw FFT magnitude")
    plt.xlim(*limits)
    plt.ylim(0, 80)
    if panel == 2:
        plt.xticks([45, 50, 55, 60, 65])
    plt.grid(alpha=0.25)
    plt.legend()

plt.tight_layout()
figure_folder = Path(__file__).resolve().parent.parent / "figures"
figure_folder.mkdir(exist_ok=True)
plt.savefig(figure_folder / "section2_window_comparison.png", dpi=180)
print("Saved section2_window_comparison.png")
plt.show()
