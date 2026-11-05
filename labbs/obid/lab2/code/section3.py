"""Lab 2, Section 3: FIR and IIR impulse responses."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter


# System 1: use the same 150-sample input length as Section 1.
fs = 250
t = np.arange(0, 0.6, 1/fs)
h = [1, 0.5, 0.3, 0.1, -0.1, -0.4, -0.2, 0.1]
impulse_fir = np.zeros(len(t))
impulse_fir[0] = 1
y_fir = np.convolve(h, impulse_fir)

print(f"System 1: unit impulse length = {len(impulse_fir)}")
print("First eight output samples:", y_fir[:8])
print("Remaining output samples are zero:", np.all(y_fir[8:] == 0))
assert np.allclose(y_fir[:8], h)
assert np.all(y_fir[8:] == 0)

# System 2: use 100 samples for both simulations.
b = [1, 0.3]
a = [1, 0.6, -0.35]
impulse = np.zeros(100)
impulse[0] = 1
y_loop = np.zeros(100)

# The printed equation repeats y[n-1]; the coefficients require y[n-2].
# The conditions below make all negative-index values zero.
for n in range(len(impulse)):
    y_loop[n] = impulse[n]
    if n >= 1:
        y_loop[n] += 0.3 * impulse[n-1] - 0.6 * y_loop[n-1]
    if n >= 2:
        y_loop[n] += 0.35 * y_loop[n-2]

y_filter = lfilter(b, a, impulse)
maximum_difference = np.max(np.abs(y_loop - y_filter))
print("System 2 first five output samples:", y_loop[:5])
print(f"Maximum loop/lfilter difference: {maximum_difference:.17g}")
assert np.allclose(y_loop[:5], [1, -0.3, 0.53, -0.423, 0.4393])
assert np.allclose(y_loop, y_filter)

# One figure: show the short FIR response and all 100 IIR samples.
plt.rcParams.update({"font.size": 10, "lines.linewidth": 1.2})
plt.figure(figsize=(9, 6))
plt.subplot(2, 1, 1)
plt.stem(np.arange(16), y_fir[:16],
         linefmt="C2-", markerfmt="C2o", basefmt="k-")
plt.title("System 1: FIR impulse response (first 16 samples)")
plt.xlabel("Sample index n")
plt.ylabel("Amplitude")
plt.xticks(np.arange(16))
plt.xlim(-0.5, 15.5)
plt.grid(alpha=0.25)

plt.subplot(2, 1, 2)
plt.plot(np.arange(100), y_loop, "o-", color="#185c4b",
         markersize=3, label="Loop")
plt.plot(np.arange(100), y_filter, "x--", color="#b07130",
         markersize=4, label="lfilter")
plt.title("System 2: IIR impulse response")
plt.xlabel("Sample index n")
plt.ylabel("Amplitude")
plt.xlim(0, 99)
plt.grid(alpha=0.25)
plt.legend()

plt.tight_layout()
figure_folder = Path(__file__).resolve().parent.parent / "figures"
figure_folder.mkdir(exist_ok=True)
plt.savefig(figure_folder / "section3_lti_systems.png", dpi=180)
print("Saved section3_lti_systems.png")
plt.show()
