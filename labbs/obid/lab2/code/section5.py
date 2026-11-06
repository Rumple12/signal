"""Lab 2, Section 5: System 2 frequency response and a 50 Hz input."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import lfilter


fs = 250
t = np.arange(0, 0.6, 1/fs)
b = [1, 0.3]
a = [1, 0.6, -0.35]

# Obtain the system response from a 150-sample impulse response.
impulse = np.zeros(len(t))
impulse[0] = 1
h = lfilter(b, a, impulse)
H = fft(h)
f = fftfreq(len(t), 1/fs)
positive = f >= 0
gain = np.abs(H)
phase_shift = np.angle(H)

# Send the teacher's 50 Hz cosine through System 2.
x2 = np.cos(2*np.pi*50*t)
y3 = lfilter(b, a, x2)
X2 = fft(x2)
Y3 = fft(y3)
input_amplitudes = 2 * np.abs(X2) / len(t)
output_amplitudes = 2 * np.abs(Y3) / len(t)
input_phases = np.angle(X2)
output_phases = np.angle(Y3)

# Compare the prediction with the measured FFT at the 50 Hz bin.
index_50 = np.argmin(np.abs(f - 50))
predicted_Y = H[index_50] * X2[index_50]
predicted_amplitude = 2 * np.abs(predicted_Y) / len(t)
predicted_phase = np.angle(predicted_Y)
measured_amplitude = output_amplitudes[index_50]
measured_phase = output_phases[index_50]
difference_percent = abs(measured_amplitude - predicted_amplitude) / predicted_amplitude * 100

print(f"Input amplitude: {input_amplitudes[index_50]:.4f}")
print(f"Input phase: {input_phases[index_50]:.4f} rad")
print(f"System gain at 50 Hz: {gain[index_50]:.4f}")
print(f"System phase shift at 50 Hz: {phase_shift[index_50]:.4f} rad")
print(f"Predicted output amplitude: {predicted_amplitude:.4f}")
print(f"Predicted output phase: {predicted_phase:.4f} rad")
print(f"Measured output amplitude: {measured_amplitude:.4f}")
print(f"Measured output phase: {measured_phase:.4f} rad")
print(f"Output amplitude difference: {difference_percent:.4f}%")
# Finite records include startup and truncation effects; do not force equality.

plt.rcParams.update({"font.size": 10, "lines.linewidth": 1.2})
plt.figure(figsize=(9, 6.5))
plt.subplot(2, 2, 1)
plt.plot(f[positive], gain[positive], color="#185c4b")
plt.title("System 2 amplification")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain")
plt.xlim(0, 125)
plt.grid(alpha=0.25)

plt.subplot(2, 2, 2)
plt.plot(f[positive], phase_shift[positive], color="#185c4b")
plt.title("System 2 phase shift")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase shift (rad)")
plt.xlim(0, 125)
plt.grid(alpha=0.25)

plt.subplot(2, 2, 3)
plt.plot(f[positive], input_amplitudes[positive], "-",
         color="#185c4b", label="Input")
plt.plot(f[positive], output_amplitudes[positive], "--",
         color="#b07130", label="Output")
plt.title("Input and output amplitude spectra")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (2|FFT|/N)")
plt.xlim(0, 125)
plt.grid(alpha=0.25)
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(f[positive], input_phases[positive], "-",
         color="#185c4b", label="Input")
plt.plot(f[positive], output_phases[positive], "--",
         color="#b07130", label="Output")
plt.title("Input and output phase spectra")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (rad)")
plt.xlim(0, fs / 2)
plt.grid(True)
plt.legend()

plt.tight_layout()
figure_folder = Path(__file__).resolve().parent.parent / "figures"
figure_folder.mkdir(exist_ok=True)
plt.savefig(figure_folder / "section5_system_response.png", dpi=180)
print("Saved section5_system_response.png")
plt.show()
