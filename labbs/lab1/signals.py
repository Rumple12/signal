"""Lab 1, Section 1: signal generation, FFT, and sampling."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # Save figures without opening plot windows.
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

folder = Path(__file__).resolve().parent
figures = folder / "figures"
figures.mkdir(exist_ok=True)
rng = np.random.default_rng(2026)

# 1.1: Use the teacher's time vector and basic waveforms.
t = np.linspace(0, 1, 1000)
sine10 = np.sin(2 * np.pi * 10 * t)
sine20 = np.sin(2 * np.pi * 20 * t)
square = np.sign(np.sin(2 * np.pi * 5 * t))
sawtooth = 2 * ((5 * t) % 1) - 1
ceil_square = 2 * np.ceil(np.sin(2 * np.pi * 5 * t)) - 1
composite = sine10 + square

plt.figure(figsize=(11, 8))
examples = [
    (sine10, "10 Hz sine"),
    (square, "5 Hz square"),
    (sawtooth, "5 Hz sawtooth"),
    (composite, "10 Hz sine + 5 Hz square"),
]
for position, (wave, title) in enumerate(examples, 1):
    plt.subplot(3, 2, position)
    plt.plot(t, wave)
    plt.xlim(0, 0.4)
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
plt.subplot(3, 2, 5)
plt.plot(t, sine10, label="10 Hz")
plt.plot(t, sine20, label="20 Hz")
plt.xlim(0, 0.2)
plt.title("Doubling the sine frequency")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.subplot(3, 2, 6)
plt.plot(t, square, label="sign", linewidth=3)
plt.plot(t, ceil_square, "--", label="ceil expression")
plt.xlim(0, 0.4)
plt.title("Almost identical on this time grid")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.tight_layout()
plt.savefig(figures / "signal_examples.png", dpi=150)
plt.close()

print("1.1: different sign/ceil samples:", np.count_nonzero(square != ceil_square))
print("Positive samples, sign/ceil:", np.count_nonzero(square > 0),
      np.count_nonzero(ceil_square > 0))
print(f"Composite range: {composite.min():.6f} to {composite.max():.6f}")

# 1.2: Calculate positive-frequency FFT magnitudes.
def spectrum(wave, sample_rate):
    frequencies = np.fft.rfftfreq(len(wave), 1 / sample_rate)
    magnitude = np.abs(np.fft.rfft(wave)) / len(wave)
    magnitude[1:] *= 2
    if len(wave) % 2 == 0:
        magnitude[-1] /= 2  # The Nyquist bin has no negative-frequency partner.
    return frequencies, magnitude


def generate_signal(time, amplitude30=0):
    return (np.sin(2 * np.pi * 10 * time) + 0.5 * np.sin(2 * np.pi * 20 * time)
            + amplitude30 * np.sin(2 * np.pi * 30 * time))


sample_rate = 1 / (t[1] - t[0])
two_tones = generate_signal(t)
three_tones = generate_signal(t, amplitude30=0.25)
noisy_tones = two_tones + rng.normal(0, 0.2, len(t))

plt.figure(figsize=(11, 8))
for row, (wave, title) in enumerate([
    (two_tones, "10 and 20 Hz"),
    (three_tones, "Added 30 Hz, amplitude 0.25"),
    (noisy_tones, "Added noise, standard deviation 0.2"),
]):
    frequencies, magnitude = spectrum(wave, sample_rate)
    plt.subplot(3, 2, 2 * row + 1)
    plt.plot(t, wave)
    plt.xlim(0, 0.4)
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.subplot(3, 2, 2 * row + 2)
    plt.plot(frequencies, magnitude)
    plt.xlim(0, 80)
    plt.ylim(0, 1.1)
    plt.title("Positive-frequency amplitude spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    if row < 2:
        for expected in ([10, 20] if row == 0 else [10, 20, 30]):
            nearby = np.abs(frequencies - expected) < 1
            peak = frequencies[nearby][np.argmax(magnitude[nearby])]
            assert abs(peak - expected) < 0.1
            print(f"FFT: expected {expected} Hz, measured bin {peak:.3f} Hz")
plt.tight_layout()
plt.savefig(figures / "fft_comparison.png", dpi=150)
plt.close()


# Chirp phase is the integral of a frequency increasing linearly with time.
def make_chirp(time, start_frequency, end_frequency, duration):
    slope = (end_frequency - start_frequency) / duration
    phase = 2 * np.pi * (start_frequency * time + 0.5 * slope * time**2)
    return np.sin(phase)


duration = 1
chirp = make_chirp(t, 10, 50, duration)
instantaneous_frequency = 10 + (50 - 10) * t / duration
assert np.allclose(instantaneous_frequency[[0, -1]], [10, 50])
# Also check the frequency from changes in the actual phase formula.
phase = 2 * np.pi * (10 * t + 0.5 * 40 * t**2)
assert np.allclose(chirp, np.sin(phase))
phase_frequency = np.diff(phase) / (2 * np.pi * np.diff(t))
assert np.allclose(phase_frequency, 10 + 40 * (t[:-1] + t[1:]) / 2)
frequencies, magnitude = spectrum(chirp, sample_rate)
f, times, stft = signal.stft(chirp, fs=sample_rate, nperseg=256)
power_db = 10 * np.log10(np.maximum(np.abs(stft)**2, 1e-12))

plt.figure(figsize=(11, 7))
plt.subplot(2, 2, 1)
plt.plot(t, chirp)
plt.title("Chirp: 10 to 50 Hz in 1 s")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.subplot(2, 2, 2)
plt.plot(frequencies, magnitude)
plt.xlim(0, 80)
plt.title("FFT over the whole chirp")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.subplot(2, 2, 3)
plt.pcolormesh(times, f, power_db, shading="auto", vmin=-60, vmax=0)
plt.ylim(0, 80)
plt.title("Frequency changes with time")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.colorbar(label="STFT power (dB, reference 1)")
plt.subplot(2, 2, 4)
plt.plot(t, instantaneous_frequency)
plt.title("Frequency calculated from the phase")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.tight_layout()
plt.savefig(figures / "chirp.png", dpi=150)
plt.close()
print("Chirp endpoints (Hz):", instantaneous_frequency[[0, -1]])
print("Chirp phase-difference endpoints (Hz):", phase_frequency[[0, -1]])


# 1.3: The folded frequency lies between -fs/2 and fs/2.
def sample_sine(frequency, sample_rate):
    sample_times = np.arange(0, 1, 1 / sample_rate)
    samples = np.sin(2 * np.pi * frequency * sample_times)
    return sample_times, samples


plt.figure(figsize=(11, 7))
for position, (frequency, fs) in enumerate([(10, 15), (10, 25), (20, 30), (10, 11)], 1):
    dense_time = np.linspace(0, 1, 5000)
    sample_times, samples = sample_sine(frequency, fs)
    alias = (frequency + fs / 2) % fs - fs / 2
    assert np.allclose(samples, np.sin(2 * np.pi * alias * sample_times))
    plt.subplot(2, 2, position)
    plt.plot(dense_time, np.sin(2 * np.pi * frequency * dense_time),
             label=f"Reference {frequency} Hz", alpha=0.6)
    plt.stem(sample_times, samples, linefmt="C1-", markerfmt="C1o", basefmt=" ")
    if alias != frequency:
        plt.plot(dense_time, np.sin(2 * np.pi * alias * dense_time), "--",
                 label=f"Matching alias: {alias:g} Hz")
    plt.title(f"{frequency} Hz sampled at {fs} Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend(fontsize=8)
    print(f"Sampling: f={frequency}, fs={fs}, Nyquist rate={2*frequency}, "
          f"Nyquist frequency={fs/2:g}, signed alias={alias:g} Hz")
plt.tight_layout()
plt.savefig(figures / "sampling_aliasing.png", dpi=150)
plt.close()
print("Signal checks passed; four figures saved.")
