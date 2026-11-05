"""Lab 1, Section 1.2: Fourier analysis."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# Add an optional 30 Hz wave to the teacher's original signal.
def generate_signal(t, amplitude_30=0):
    return (
        np.sin(2 * np.pi * 10 * t)
        + 0.5 * np.sin(2 * np.pi * 20 * t)
        + amplitude_30 * np.sin(2 * np.pi * 30 * t)
    )


# A linear sweep starts at 15 Hz and ends at 65 Hz after one second.
def generate_chirp(t):
    start_frequency = 15
    end_frequency = 65
    duration = 1
    slope = (end_frequency - start_frequency) / duration
    phase = 2 * np.pi * (start_frequency * t + 0.5 * slope * t**2)
    return np.sin(phase)


# Q1: keep the teacher's time vector and calculate its FFT.
t = np.linspace(0, 1, 1000)
signal = generate_signal(t)
fft_result = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(t), t[1] - t[0])
half = len(t) // 2
positive_frequencies = freqs[:half]
original_magnitude = np.abs(fft_result)[:half]

# Q2: add a 30 Hz sine with amplitude 0.3.
amplitude_30 = 0.3
modified_signal = generate_signal(t, amplitude_30)
modified_fft = np.fft.fft(modified_signal)
modified_magnitude = np.abs(modified_fft)[:half]

# Q3: add repeatable Gaussian noise to the ORIGINAL signal.
noise_std = 0.18
noise_seed = 1729
rng = np.random.default_rng(noise_seed)
noise = rng.normal(0, noise_std, len(t))
noisy_signal = signal + noise
noisy_fft = np.fft.fft(noisy_signal)
noisy_magnitude = np.abs(noisy_fft)[:half]

# Q4: generate the chirp and calculate its whole-signal FFT.
chirp_signal = generate_chirp(t)
chirp_fft = np.fft.fft(chirp_signal)
chirp_magnitude = np.abs(chirp_fft)[:half]

# Read the two largest original peaks and the three largest modified peaks.
original_peak_indices = np.sort(np.argsort(original_magnitude)[-2:])
modified_peak_indices = np.sort(np.argsort(modified_magnitude)[-3:])
noisy_peak_indices = np.sort(np.argsort(noisy_magnitude)[-2:])
print("Samples:", len(t))
print("Time step (s):", t[1] - t[0])
print("FFT bin spacing (Hz):", freqs[1] - freqs[0])
print("Original peak frequencies (Hz):", positive_frequencies[original_peak_indices])
print("Original raw FFT magnitudes:", original_magnitude[original_peak_indices])
print("Added 30 Hz amplitude:", amplitude_30)
print("Modified peak frequencies (Hz):", positive_frequencies[modified_peak_indices])
print("Modified raw FFT magnitudes:", modified_magnitude[modified_peak_indices])
print("Noise standard deviation and seed:", noise_std, noise_seed)
print("Noisy peak frequencies (Hz):", positive_frequencies[noisy_peak_indices])
print("Noisy raw FFT magnitudes:", noisy_magnitude[noisy_peak_indices])
print("Chirp: 15 Hz to 65 Hz over one second.")

# Use the same clean presentation as Section 1.1.
figure_folder = Path(__file__).resolve().parent.parent / "figures"
figure_folder.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "lines.linewidth": 1.5})

plt.figure(figsize=(8, 4.8))
plt.subplot(2, 1, 1)
plt.plot(t, signal, color="#526d82")
plt.title("Original signal: 10 Hz + 20 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.xlim(0, 1)
plt.ylim(-1.6, 1.6)
plt.grid(axis="y", alpha=0.2)
plt.subplot(2, 1, 2)
plt.plot(positive_frequencies, original_magnitude, color="#526d82")
plt.title("Original FFT: 0 to 80 Hz shown")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Raw FFT magnitude")
plt.xlim(0, 80)
plt.ylim(0, 550)
plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(figure_folder / "section1_2_original_fft.png", dpi=180)

# All three spectra use the same axes, without separate rescaling.
spectra = [original_magnitude, modified_magnitude, noisy_magnitude]
titles = ["Original: 10 Hz + 20 Hz", "Modified: added 30 Hz, amplitude 0.3",
          "Noisy original: standard deviation 0.18, seed 1729"]
colours = ["#526d82", "#4c7067", "#9a6848"]
plt.figure(figsize=(8, 6))
for i in range(3):
    plt.subplot(3, 1, i + 1)
    plt.plot(positive_frequencies, spectra[i], color=colours[i])
    plt.title(titles[i])
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Raw FFT magnitude")
    plt.xlim(0, 80)
    plt.ylim(0, 550)
    plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(figure_folder / "section1_2_spectra_comparison.png", dpi=180)

plt.figure(figsize=(8, 4.8))
plt.subplot(2, 1, 1)
plt.plot(t, chirp_signal, color="#72627f")
plt.title("Chirp: 15 Hz to 65 Hz in one second")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.xlim(0, 1)
plt.ylim(-1.2, 1.2)
plt.grid(axis="y", alpha=0.2)
plt.subplot(2, 1, 2)
plt.plot(positive_frequencies, chirp_magnitude, color="#72627f")
plt.title("Chirp FFT: 0 to 100 Hz shown")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Raw FFT magnitude")
plt.xlim(0, 100)
plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(figure_folder / "section1_2_chirp_fft.png", dpi=180)

# Basic checks for the fixed parameters and expected frequency bins.
assert len(t) == 1000 and t[0] == 0 and t[-1] == 1
assert np.allclose(signal, np.sin(2*np.pi*10*t) + 0.5*np.sin(2*np.pi*20*t))
assert np.allclose(modified_signal - signal, amplitude_30 * np.sin(2*np.pi*30*t))
assert np.allclose(positive_frequencies[original_peak_indices], [9.99, 19.98])
assert np.allclose(positive_frequencies[modified_peak_indices], [9.99, 19.98, 29.97])
assert np.allclose(positive_frequencies[noisy_peak_indices], [9.99, 19.98])
assert np.allclose(noisy_signal - signal, noise)
assert np.all(np.abs(chirp_signal) <= 1)
print("Basic Section 1.2 checks passed.")
print("Three figures saved in", figure_folder)
plt.show()
