"""Lab 1, Section 3: compare audio clips and demonstrate downsampling."""

from io import BytesIO
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import requests
from scipy.io import wavfile

folder = Path(__file__).resolve().parent
figures = folder / "figures"
figures.mkdir(exist_ok=True)
data_folder = folder / "data"
data_folder.mkdir(exist_ok=True)

sources = {
    "Piano": "https://raw.githubusercontent.com/parisjava/wav-piano-sound/master/wav/a1.wav",
    "Rain": "https://www.pacdv.com/sounds/ambience_sounds/rain_2.wav",
    "Speech": "https://www.pacdv.com/sounds/voices/can-you-keep-a-secret.wav",
}


def load_audio(name, url):
    path = data_folder / (name.lower() + ".wav")
    if not path.exists():
        response = requests.get(url, headers={"User-Agent": "DT081A-Lab1/1.0"}, timeout=30)
        response.raise_for_status()
        path.write_bytes(response.content)
    fs, data = wavfile.read(BytesIO(path.read_bytes()))
    data = data.astype(float)  # Safe arithmetic before averaging or normalizing.
    if data.ndim == 2:
        data = np.mean(data, axis=1)
    peak = np.max(np.abs(data))
    if peak > 0:
        data = data / peak
    return fs, data


def spectrum(data, fs):
    frequencies = np.fft.rfftfreq(len(data), 1 / fs)
    magnitude = np.abs(np.fft.rfft(data)) / len(data)
    magnitude[1:] *= 2
    if len(data) % 2 == 0:
        magnitude[-1] /= 2
    return frequencies, magnitude


clips = {}
plt.figure(figsize=(13, 9))
for column, (name, url) in enumerate(sources.items(), 1):
    fs, data = load_audio(name, url)
    clips[name] = (fs, data)
    time = np.arange(len(data)) / fs
    frequencies, magnitude = spectrum(data, fs)
    peak_index = np.argmax(magnitude[1:]) + 1
    # A declared visibility rule, not an exact physical upper frequency limit.
    visible = (frequencies > 0) & (magnitude >= 0.01 * magnitude[peak_index])
    highest_visible = frequencies[visible][-1]
    print(f"{name}: fs={fs} Hz, samples={len(data)}, full/analyzed duration={len(data)/fs:.6f} s, "
          f"strongest peak={frequencies[peak_index]:.6f} Hz, "
          f"highest bin at >=1% of peak={highest_visible:.6f} Hz")
    print("Source:", url)
    plt.subplot(3, 3, column)
    plt.plot(time, data, linewidth=0.5)
    plt.title(f"{name}: {len(data)/fs:.3f} s, {fs} Hz sampling")
    plt.xlabel("Time (s)")
    plt.ylabel("Normalized amplitude")
    plt.subplot(3, 3, column + 3)
    plt.plot(frequencies, magnitude, linewidth=0.7)
    plt.xlim(0, fs / 2)
    plt.title("Whole-clip spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.subplot(3, 3, column + 6)
    # Use the teacher's spectrogram, with the same colour limits for all clips.
    # Zero power means minus infinity dB, which is shown as the darkest colour.
    with np.errstate(divide="ignore"):
        plt.specgram(data, NFFT=1024, Fs=fs, noverlap=512,
                     vmin=-100, vmax=-20, cmap="viridis")
    plt.title("Spectrogram (-100 to -20 dB/Hz)", fontsize=10)
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
plt.tight_layout()
plt.savefig(figures / "audio_types.png", dpi=150)
plt.close()

# Compare full speech with its first half second using the same normalization.
fs, speech = clips["Speech"]
half_second = speech[:int(0.5 * fs)]
assert len(half_second) == int(0.5 * fs)
plt.figure(figsize=(11, 6))
for row, (data, title) in enumerate([(speech, "Full speech"),
                                    (half_second, "First 0.5 seconds")]):
    frequencies, magnitude = spectrum(data, fs)
    peak_index = np.argmax(magnitude[1:]) + 1
    print(f"Speech comparison: {title}, duration={len(data)/fs:.6f} s, "
          f"bin spacing={fs/len(data):.6f} Hz, strongest peak={frequencies[peak_index]:.6f} Hz")
    plt.subplot(2, 2, 2 * row + 1)
    plt.plot(np.arange(len(data)) / fs, data, linewidth=0.7)
    plt.ylim(-1, 1)
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Normalized amplitude")
    plt.subplot(2, 2, 2 * row + 2)
    plt.plot(frequencies, magnitude)
    plt.xlim(0, 6000)
    plt.ylim(0, 0.08)
    plt.title("Spectrum, detail from 0 to 6000 Hz")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
plt.tight_layout()
plt.savefig(figures / "audio_half_second.png", dpi=150)
plt.close()


# Deliberately omit a low-pass filter here so that aliasing can be observed.
def downsample(data, fs, factor):
    return data[::factor], fs / factor


tone_fs = 12000
tone_time = np.arange(0, 0.1, 1 / tone_fs)
tone = np.sin(2 * np.pi * 2500 * tone_time)
plt.figure(figsize=(13, 9))
for column, factor in enumerate([1, 2, 3, 6], 1):
    reduced, reduced_fs = downsample(speech, fs, factor)
    times = np.arange(len(reduced)) / reduced_fs
    frequencies, magnitude = spectrum(reduced, reduced_fs)
    plt.subplot(3, 4, column)
    plt.plot(times, reduced, ".-", markersize=2)
    plt.xlim(0.2, 0.225)
    plt.ylim(-0.7, 0.7)
    plt.title(f"Speech: fs={reduced_fs:g} Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.subplot(3, 4, column + 4)
    plt.plot(frequencies, magnitude)
    plt.xlim(0, 22050)
    plt.ylim(0, 0.04)
    plt.title(f"Nyquist: {reduced_fs/2:g} Hz")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    peak_index = np.argmax(magnitude[1:]) + 1
    print(f"Speech downsampling: factor={factor}, fs={reduced_fs:g}, "
          f"samples={len(reduced)}, Nyquist={reduced_fs/2:g}, "
          f"strongest peak={frequencies[peak_index]:.6f} Hz")

    reduced_tone, new_tone_fs = downsample(tone, tone_fs, factor)
    f, amplitude = spectrum(reduced_tone, new_tone_fs)
    measured = f[np.argmax(amplitude)]
    expected = abs((2500 + new_tone_fs / 2) % new_tone_fs - new_tone_fs / 2)
    assert np.isclose(measured, expected)
    plt.subplot(3, 4, column + 8)
    plt.plot(f, amplitude)
    plt.xlim(0, 6000)
    plt.ylim(0, 1.1)
    plt.title(f"2500 Hz tone: fs={new_tone_fs:g} Hz\nPeak {measured:g} Hz")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    print(f"Known tone: fs={new_tone_fs:g}, Nyquist={new_tone_fs/2:g}, "
          f"expected/measured alias={expected:g}/{measured:g} Hz")
plt.tight_layout()
plt.savefig(figures / "audio_downsampling.png", dpi=150)
plt.close()
print("Audio checks passed; three figures saved. No playback or listening test performed.")
