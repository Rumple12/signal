"""Lab 2, Section 4: recover cosine amplitudes and phases from the FFT."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq


# Regenerate the teacher's exact signal from Section 1.
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

X = fft(x)
A_x = np.abs(X)
phase_x = np.angle(X)
f = fftfreq(len(x), 1/fs)
positive = f >= 0

# Recover each cosine amplitude from its positive-frequency FFT peak.
amplitudes = 2 * A_x / len(x)
peak_indices = []
for frequency, amplitude, phase in zip(
        [f1, f2, f3], [A1, A2, A3], [ph1, ph2, ph3]):
    index = np.argmin(np.abs(f - frequency))
    peak_indices.append(index)
    print(f"{f[index]:g} Hz: raw FFT = {A_x[index]:.4f}; "
          f"amplitude = {amplitudes[index]:.4f}; phase = {phase_x[index]:.4f} rad")
    assert np.isclose(amplitudes[index], amplitude)
    assert np.isclose(phase_x[index], phase)
print("All amplitudes and phases matched the original signal.")

# Hide unreliable phases where the FFT magnitude is close to zero.
significant = positive & (A_x > 0.000001 * np.max(A_x))

plt.rcParams.update({"font.size": 10, "lines.linewidth": 1.2})
plt.figure(figsize=(9, 3.5))
plt.subplot(1, 2, 1)
plt.plot(f[positive], A_x[positive], color="#185c4b")
plt.plot(f[peak_indices], A_x[peak_indices], "o", color="#185c4b", markersize=4)
for index in peak_indices:
    offset = (-38, 7) if f[index] == 120 else (5, 7)
    plt.annotate(f"{f[index]:g} Hz", (f[index], A_x[index]),
                 xytext=offset, textcoords="offset points")
plt.title("Amplitude spectrum (raw FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Raw FFT magnitude")
plt.xlim(0, 125)
plt.ylim(0, 85)
plt.grid(alpha=0.25)

plt.subplot(1, 2, 2)
plt.plot(f[significant], phase_x[significant], "o", color="#b07130")
for index in peak_indices:
    offset = (-38, 7) if f[index] == 120 else (5, 7)
    plt.annotate(f"{f[index]:g} Hz", (f[index], phase_x[index]),
                 xytext=offset, textcoords="offset points")
plt.title("Phase spectrum (significant bins)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (rad)")
plt.xlim(0, 125)
plt.ylim(-0.2, 1.9)
plt.yticks([0, np.pi/4, np.pi/2], ["0", r"$\pi/4$", r"$\pi/2$"])
plt.grid(alpha=0.25)

plt.tight_layout()
figure_folder = Path(__file__).resolve().parent.parent / "figures"
figure_folder.mkdir(exist_ok=True)
plt.savefig(figure_folder / "section4_amplitude_phase.png", dpi=180)
print("Saved section4_amplitude_phase.png")
plt.show()
