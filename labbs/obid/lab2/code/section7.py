"""Lab 2, Section 7: Obid's voice with three FFT segment lengths."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile


lab_folder = Path(__file__).resolve().parent.parent
audio_path = lab_folder / "obid.wav"
if not audio_path.exists():
    raise SystemExit(f"Missing recording: {audio_path}")

# Read the original file without changing it; average stereo channels if needed.
fs, x_voice = wavfile.read(audio_path)
x_voice = x_voice.astype(float)
if x_voice.ndim == 2:
    x_voice = np.mean(x_voice, axis=1)

duration = len(x_voice) / fs
print(f"Sampling rate: {fs} Hz")
print(f"Recording duration: {duration:.6f} s")

# Each row is one complete, non-overlapping segment, as in the teacher's code.
segment_lengths = [512, 1024, 2048]
results = {}
for k in segment_lengths:
    n = len(x_voice) // k
    if n == 0:
        raise ValueError(f"The recording is too short for k = {k}.")
    segments = x_voice[:n*k].reshape(n, k)
    X_voice = np.fft.rfft(segments, axis=1)
    power = np.abs(X_voice)**2
    frequencies = np.fft.rfftfreq(k, d=1/fs)
    segment_time = k / fs
    frequency_spacing = fs / k

    # Cell edges give exact segment times and center the FFT frequency bins.
    time_edges = np.arange(n + 1) * segment_time
    frequency_edges = np.append(frequencies - frequency_spacing/2,
                                frequencies[-1] + frequency_spacing/2)
    # Dividing by k squared makes the power scales comparable across lengths.
    results[k] = (time_edges, frequency_edges, power / k**2)
    print(f"k = {k}: time per segment = {segment_time:.6f} s; "
          f"frequency spacing = {frequency_spacing:.4f} Hz; "
          f"complete segments = {n}; duration = {duration:.6f} s")

# Use one shared reference and colour range for all three panels.
reference_power = max(result[2].max() for result in results.values())
if reference_power == 0:
    raise ValueError("The recording contains no signal power to display.")

plt.rcParams.update({"font.size": 10})
figure = plt.figure(figsize=(9, 6), layout="constrained")
axes = []
for position, k in zip([(1, 2), 3, 4], [1024, 512, 2048]):
    axes.append(plt.subplot(2, 2, position))
    time_edges, frequency_edges, power = results[k]
    power_db = 10 * np.log10(np.maximum(power / reference_power, 1e-12))
    mesh = plt.pcolormesh(time_edges, frequency_edges, power_db.T,
                          shading="flat", cmap="viridis", vmin=-60, vmax=0)
    plt.title(f"k = {k}" + (" (main experiment)" if k == 1024 else ""))
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.xlim(0, duration)
    plt.ylim(0, min(6000, fs/2))

figure.colorbar(mesh, ax=axes,
               label=r"Power (dB re shared max of $|\mathrm{FFT}/k|^2$)")
figure_folder = lab_folder / "figures"
figure_folder.mkdir(exist_ok=True)
plt.savefig(figure_folder / "section7_voice_spectrogram.png", dpi=180)
print("Saved section7_voice_spectrogram.png")
plt.show()
