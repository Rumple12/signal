"""Lab 1, Section 1.1: signal generation and visualization."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Keep the teacher's time vector and original signals.
t = np.linspace(0, 1, 1000)
sine_wave = np.sin(2 * np.pi * 10 * t)
square_wave = np.sign(np.sin(2 * np.pi * 5 * t))

# Q1: remove whole cycles to make a ramp that repeats five times.
sawtooth_wave = 2 * (5 * t - np.floor(5 * t)) - 1

# Q2: change only the sine frequency.
sine_wave_20 = np.sin(2 * np.pi * 20 * t)

# Q3: use the teacher's exact replacement and compare every sample.
square_wave_ceil = np.ceil(np.sin(2 * np.pi * 5 * t)) * 2 - 1
different_samples = np.flatnonzero(square_wave != square_wave_ceil)
print("Number of samples:", len(t))
print("Original square values:", np.unique(square_wave))
print("Replacement square values:", np.unique(square_wave_ceil))
print("Different sample indices:", different_samples)
print("Times of different samples (s):", t[different_samples])
print("Original values there:", square_wave[different_samples])
print("Replacement values there:", square_wave_ceil[different_samples])
print("Samples with value -3:", np.count_nonzero(square_wave_ceil == -3))

# Q4: add the original 10 Hz sine and 5 Hz square.
composite_signal = sine_wave + square_wave
print("Composite minimum and maximum:", composite_signal.min(), composite_signal.max())

# Save the figures in this student's own folder.
figure_folder = Path(__file__).resolve().parent.parent / "figures"
figure_folder.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "lines.linewidth": 1.5})

plt.figure(figsize=(8, 2.3))
plt.plot(t, sawtooth_wave, color="#4c7067")
plt.title("5 Hz sawtooth wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.xlim(0, 1)
plt.ylim(-1.2, 1.2)
plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(figure_folder / "q1_sawtooth.png", dpi=180)

# Use separate panels with the same axes for the frequency comparison.
plt.figure(figsize=(8, 3.4))
plt.subplot(2, 1, 1)
plt.plot(t, sine_wave, color="#526d82")
plt.title("Original sine: 10 Hz")
plt.ylabel("Amplitude")
plt.xlim(0, 1)
plt.ylim(-1.2, 1.2)
plt.grid(axis="y", alpha=0.2)
plt.subplot(2, 1, 2)
plt.plot(t, sine_wave_20, color="#9a6848")
plt.title("Changed sine: 20 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.xlim(0, 1)
plt.ylim(-1.2, 1.2)
plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(figure_folder / "q2_sine_frequencies.png", dpi=180)

plt.figure(figsize=(8, 2.6))
plt.plot(t, composite_signal, color="#72627f")
plt.title("10 Hz sine + 5 Hz square")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.xlim(0, 1)
plt.ylim(-2.3, 2.3)
plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(figure_folder / "q4_composite.png", dpi=180)

# Basic checks for the teacher's parameters and the Q3 result.
assert len(t) == 1000 and t[0] == 0 and t[-1] == 1
assert np.allclose(np.diff(t), 1 / 999)
assert np.all(np.abs(sine_wave) <= 1)
assert np.all(np.abs(sine_wave_20) <= 1)
assert np.all((sawtooth_wave >= -1) & (sawtooth_wave < 1))
assert np.array_equal(different_samples, [0])
assert square_wave[0] == 0 and square_wave_ceil[0] == -1
assert np.allclose(composite_signal - sine_wave, square_wave)
print("Basic Section 1.1 checks passed.")
print("Three figures saved in", figure_folder)
plt.show()
