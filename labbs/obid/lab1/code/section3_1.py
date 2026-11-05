"""Lab 1, Section 3.1: audio waveforms, FFTs, spectrograms and aliasing."""

from pathlib import Path
from urllib.request import Request, urlopen

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile


# Download each source once, then keep using the local WAV file.
def load_audio(url, path):
    if not path.exists():
        request = Request(url, headers={"User-Agent": "DT081A-Lab1/1.0"})
        with urlopen(request, timeout=30) as response:
            path.write_bytes(response.read())
    sample_rate, data = wavfile.read(path)
    data = data.astype(float)
    if data.ndim == 2:
        data = np.mean(data, axis=1)
    # Normalize each recording to its own peak, as in the teacher's example.
    data = data / np.max(np.abs(data))
    return sample_rate, data


# Divide by the number of samples to compare recordings of different lengths.
def calculate_spectrum(data, sample_rate):
    frequencies = np.fft.rfftfreq(len(data), 1 / sample_rate)
    magnitude = np.abs(np.fft.rfft(data)) / len(data)
    return frequencies, magnitude


def downsample(data, sample_rate, factor):
    # Keep every factor-th sample without an anti-aliasing filter.
    return data[::factor], sample_rate / factor


lab_folder = Path(__file__).resolve().parent.parent
audio_folder = lab_folder / "audio"
figure_folder = lab_folder / "figures"
audio_folder.mkdir(exist_ok=True)
figure_folder.mkdir(exist_ok=True)

# Direct download of the teacher's github.com/parisjava/.../raw/master/wav/a1.wav.
piano_url = "https://raw.githubusercontent.com/parisjava/wav-piano-sound/master/wav/a1.wav"
thunder_url = "https://raw.githubusercontent.com/karolpiczak/ESC-50/master/audio/1-101296-A-19.wav"
piano_rate, piano = load_audio(piano_url, audio_folder / "a1.wav")
thunder_rate, thunder = load_audio(thunder_url, audio_folder / "1-101296-A-19.wav")

# Calculate both waveforms and spectra separately using their own sample rates.
names = ["Piano", "Thunderstorm"]
recordings = [piano, thunder]
sample_rates = [piano_rate, thunder_rate]
times = []
spectra = []
for name, data, sample_rate, url in zip(
        names, recordings, sample_rates, [piano_url, thunder_url]):
    times.append(np.arange(len(data)) / sample_rate)
    frequencies, magnitude = calculate_spectrum(data, sample_rate)
    spectra.append((frequencies, magnitude))
    peak_index = np.argmax(magnitude[1:]) + 1  # Skip the DC bin at 0 Hz.
    threshold = 0.01 * magnitude[peak_index]
    significant = (frequencies > 0) & (magnitude >= threshold)
    highest = frequencies[significant][-1]
    print(f"{name} source: {url}")
    print(f"{name}: sample rate = {sample_rate} Hz; samples = {len(data)}; "
          f"duration = {len(data) / sample_rate:.6f} s")
    print(f"  Strongest non-DC FFT peak = {frequencies[peak_index]:.4f} Hz")
    print(f"  Highest frequency above the 1% magnitude threshold = {highest:.4f} Hz")
    print(f"  FFT spacing = {sample_rate / len(data):.6f} Hz")

# Compare the first half second with the full piano recording.
short_piano = piano[:int(0.5 * piano_rate)]
short_frequencies, short_magnitude = calculate_spectrum(short_piano, piano_rate)
print(f"First 0.5 s of piano: samples = {len(short_piano)}; "
      f"FFT spacing = {piano_rate / len(short_piano):.6f} Hz")
short_peak = np.argmax(short_magnitude[1:]) + 1
print(f"  Strongest non-DC FFT peak = {short_frequencies[short_peak]:.4f} Hz")

# Save the downsampled piano clips for later listening; do not play them here.
for factor in [2, 4, 8]:
    reduced, reduced_rate = downsample(piano, piano_rate, factor)
    frequencies, magnitude = calculate_spectrum(reduced, reduced_rate)
    peak_index = np.argmax(magnitude[1:]) + 1
    # WAV headers require an integer rate (factor 8 gives 5512.5 Hz).
    wav_rate = round(reduced_rate)
    output = np.round(np.clip(reduced, -1, 1) * 32767).astype(np.int16)
    wavfile.write(audio_folder / f"piano_downsample_factor{factor}.wav", wav_rate, output)
    print(f"Piano factor {factor}: nominal rate = {reduced_rate:g} Hz; "
          f"WAV rate = {wav_rate} Hz; samples = {len(reduced)}; "
          f"FFT peak at nominal rate = {frequencies[peak_index]:.4f} Hz")
    if wav_rate != reduced_rate:
        print("  The saved WAV plays at the rounded rate; FFT analysis uses the exact nominal rate.")

# A one-second test tone makes the aliases easy to measure.
tone_rate = 12000
tone_time = np.arange(tone_rate) / tone_rate
tone = np.sin(2 * np.pi * 1800 * tone_time)
tone_spectra = []
for factor in [2, 4, 6]:
    reduced, reduced_rate = downsample(tone, tone_rate, factor)
    frequencies, magnitude = calculate_spectrum(reduced, reduced_rate)
    peak_index = np.argmax(magnitude[1:]) + 1
    tone_spectra.append((reduced_rate, frequencies, magnitude))
    print(f"1800 Hz tone at {reduced_rate:g} Hz sampling: "
          f"measured FFT peak = {frequencies[peak_index]:.4f} Hz")

plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "lines.linewidth": 1.5})
colours = ["#526d82", "#4c7067"]

# Figure 17: the teacher's waveform, FFT and spectrogram layout.
plt.figure(figsize=(9, 9))
plt.subplot(3, 1, 1)
plt.plot(times[0], piano, color=colours[0])
plt.title("Piano waveform")
plt.xlabel("Time (s)")
plt.ylabel("Normalized amplitude")
plt.subplot(3, 1, 2)
plt.plot(*spectra[0], color=colours[0])
plt.title("Piano frequency spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("FFT magnitude / N")
plt.subplot(3, 1, 3)
plt.specgram(piano, Fs=piano_rate, NFFT=1024, noverlap=512,
             cmap="viridis", vmin=-110, vmax=-20)
plt.title("Piano spectrogram")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.colorbar(label="PSD (dB/Hz)")
plt.tight_layout()
plt.savefig(figure_folder / "section3_1_piano_analysis.png", dpi=180)

# Figure 18: use the same scales and FFT normalization for both lengths.
plt.figure(figsize=(9, 5))
for panel, (title, spectrum) in enumerate(zip(
        ["Full piano recording", "First 0.5 seconds"],
        [spectra[0], (short_frequencies, short_magnitude)]), start=1):
    plt.subplot(2, 1, panel)
    plt.plot(*spectrum, color=colours[0])
    plt.title(title)
    plt.xlim(0, 2000)
    plt.ylim(0, 1.05 * max(spectra[0][1].max(), short_magnitude.max()))
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("FFT magnitude / N")
    plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(figure_folder / "section3_1_full_short_fft.png", dpi=180)

# Figure 19: compare all three representations without making extra figures.
plt.figure(figsize=(12, 10))
for column, (name, data, sample_rate, time, spectrum, colour) in enumerate(
        zip(names, recordings, sample_rates, times, spectra, colours), start=1):
    plt.subplot(3, 2, column)
    plt.plot(time, data, color=colour)
    plt.title(f"{name}: waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Normalized amplitude")
    plt.ylim(-1.05, 1.05)
    plt.subplot(3, 2, column + 2)
    plt.plot(*spectrum, color=colour)
    plt.title(f"{name}: FFT")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("FFT magnitude / N")
    plt.xlim(0, sample_rate / 2)
    plt.subplot(3, 2, column + 4)
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512,
                 cmap="viridis", vmin=-110, vmax=-20)
    plt.title(f"{name}: spectrogram")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.colorbar(label="PSD (dB/Hz)")
plt.tight_layout()
plt.savefig(figure_folder / "section3_1_audio_comparison.png", dpi=180)

# Figure 20: three actual FFTs of the downsampled 1800 Hz test tone.
plt.figure(figsize=(9, 7))
for panel, (sample_rate, frequencies, magnitude) in enumerate(tone_spectra, start=1):
    peak_index = np.argmax(magnitude[1:]) + 1
    plt.subplot(3, 1, panel)
    plt.plot(frequencies, magnitude, color=colours[0])
    plt.title(f"Sampling: {sample_rate:g} Hz; measured peak: {frequencies[peak_index]:g} Hz")
    plt.xlim(0, 3000)
    plt.ylim(0, 0.55)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("FFT magnitude / N")
    plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(figure_folder / "section3_1_tone_aliasing.png", dpi=180)
print("Figures 17--20 and three downsampled piano WAVs saved.")
plt.show()
