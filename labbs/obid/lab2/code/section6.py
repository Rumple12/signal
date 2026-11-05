"""Lab 2, Section 6: Butterworth and Chebyshev Type I filters."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.fft import fft, fftfreq


fs1 = 2500
fc = 200
N = 5
Rp = 3

impulse = np.zeros(150)
impulse[0] = 1
fft_points = 2500
f = fftfreq(fft_points, 1/fs1)
positive = f >= 0
index_300 = np.argmin(np.abs(f - 300))
index_100 = np.argmin(np.abs(f - 100))


# Use the teacher's impulse-response method for every filter.
def calculate_response(b, a):
    h = signal.lfilter(b, a, impulse)
    H = fft(h, n=fft_points)
    magnitude = np.abs(H)
    gain_db = 20 * np.log10(np.maximum(magnitude, 1e-12))
    phase = np.angle(H)
    # Leave gaps instead of showing phases at extremely small magnitudes.
    phase[magnitude < 0.000001 * np.max(magnitude)] = np.nan
    return gain_db, phase


# Q1: both filter families, using the same order and cutoff.
b_b_lp, a_b_lp = signal.butter(N, fc, btype="low", fs=fs1)
b_c_lp, a_c_lp = signal.cheby1(N, Rp, fc, btype="low", fs=fs1)
b_b_hp, a_b_hp = signal.butter(N, fc, btype="high", fs=fs1)
b_c_hp, a_c_hp = signal.cheby1(N, Rp, fc, btype="high", fs=fs1)

butter_lp = calculate_response(b_b_lp, a_b_lp)
cheby_lp = calculate_response(b_c_lp, a_c_lp)
butter_hp = calculate_response(b_b_hp, a_b_hp)
cheby_hp = calculate_response(b_c_hp, a_c_hp)
print(f"Butterworth LP, 200 Hz, order 5: gain at 300 Hz = {butter_lp[0][index_300]:.4f} dB")
print(f"Chebyshev I LP, 200 Hz, order 5: gain at 300 Hz = {cheby_lp[0][index_300]:.4f} dB")

# Q2: change only the requested Butterworth cutoff and order settings.
settings = [(200, 3), (200, 5), (200, 7), (400, 5)]
parameter_responses = []
parameter_labels = []
for cutoff, order in settings:
    b, a = signal.butter(order, cutoff, btype="low", fs=fs1)
    response = calculate_response(b, a)
    parameter_responses.append(response)
    parameter_labels.append(f"{cutoff} Hz, N={order}")
    print(f"Butterworth LP, {cutoff} Hz, order {order}: "
          f"gain at 300 Hz = {response[0][index_300]:.4f} dB; "
          f"phase at 100 Hz = {response[1][index_100]:.4f} rad")

# Q3: design the requested band-pass and band-stop filters.
band = [250, 500]
b_bp, a_bp = signal.butter(
    5, band, btype="bandpass", fs=2500)
b_bs, a_bs = signal.butter(
    5, band, btype="bandstop", fs=2500)

# One figure: low-pass, high-pass, then the cutoff/order comparison.
response_groups = [[butter_lp, cheby_lp], [butter_hp, cheby_hp], parameter_responses]
label_groups = [["Butterworth", "Chebyshev I"],
                ["Butterworth", "Chebyshev I"], parameter_labels]
titles = ["Low-pass: 200 Hz, order 5", "High-pass: 200 Hz, order 5",
          "Butterworth: cutoff and order"]
colours = ["#185c4b", "#b07130", "#435d99", "#895276"]
styles = ["-", "--", "-.", ":"]
plt.rcParams.update({"font.size": 11, "lines.linewidth": 1.3})
plt.figure(figsize=(9, 8.5))

for row in range(3):
    plt.subplot(3, 2, 2*row + 1)
    for label, (gain_db, phase), colour, style in zip(
            label_groups[row], response_groups[row], colours, styles):
        plt.plot(f[positive], gain_db[positive], color=colour,
                 linestyle=style, label=label)
    plt.title(titles[row])
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Gain (dB)")
    plt.xlim(0, fs1/2)
    plt.ylim(-80, 5)
    plt.grid(alpha=0.25)
    plt.legend(fontsize=9)

    plt.subplot(3, 2, 2*row + 2)
    for label, (gain_db, phase), colour, style in zip(
            label_groups[row], response_groups[row], colours, styles):
        plt.plot(f[positive], phase[positive], color=colour,
                 linestyle=style, label=label)
    plt.title(titles[row])
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (rad)")
    plt.xlim(0, fs1/2)
    plt.grid(alpha=0.25)
    plt.legend(fontsize=9)

plt.tight_layout()
figure_folder = Path(__file__).resolve().parent.parent / "figures"
figure_folder.mkdir(exist_ok=True)
plt.savefig(figure_folder / "section6_filter_comparison.png", dpi=180)
print("Saved section6_filter_comparison.png; band-pass and band-stop designs completed.")
plt.show()
