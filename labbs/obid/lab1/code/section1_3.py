"""Lab 1, Section 1.3: sampling and aliasing."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# Keep the teacher's sampling function and both time vectors.
def generate_and_sample_signal(f, fs):
    t = np.linspace(0, 1, 1000)
    original = np.sin(2 * np.pi * f * t)
    t_sampled = np.arange(0, 1, 1/fs)
    sampled = np.sin(2 * np.pi * f * t_sampled)
    return t, original, t_sampled, sampled


figure_folder = Path(__file__).resolve().parent.parent / "figures"
figure_folder.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "lines.linewidth": 1.5,
                     "axes.prop_cycle": plt.cycler(
                         color=["#526d82", "#9a6848", "#4c7067"])})

# Q1-Q3: signal frequency, sampling frequency and matching sine frequency.
# In Q2 the matching frequency is the original 10 Hz: there is no aliasing.
cases = [(10, 15, -5), (10, 25, 10), (20, 30, -10)]
plt.figure(figsize=(8, 7))
for i, (f, fs, matching_frequency) in enumerate(cases):
    t, original, t_sampled, sampled = generate_and_sample_signal(f, fs)
    plt.subplot(3, 1, i + 1)
    plt.plot(t, original, label=f"Reference: {f} Hz")
    plt.stem(t_sampled, sampled, linefmt="C1-", markerfmt="C1o",
             basefmt=" ", label=f"Samples: {fs} Hz")
    plt.title(f"Q{i+1}: {f} Hz sine sampled at {fs} Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.xlim(0, 1)
    plt.ylim(-1.2, 1.2)
    plt.grid(axis="y", alpha=0.2)
    plt.legend(loc="upper right", fontsize=9)
    # Check that the stated matching sine agrees at every sample time.
    assert np.allclose(sampled, np.sin(2 * np.pi * matching_frequency * t_sampled))
    print(f"Q{i+1}: signal {f} Hz, sampling {fs} Hz, {len(sampled)} samples, "
          f"matching frequency {matching_frequency} Hz; Nyquist rate {2*f} Hz.")
plt.tight_layout()
plt.savefig(figure_folder / "section1_3_sampling_comparison.png", dpi=180)

# Q4: the same function demonstrates the wagon-wheel effect.
f, fs = 23, 8
t, original, t_sampled, sampled = generate_and_sample_signal(f, fs)
alias_frequency = -1
alias_wave = np.sin(2 * np.pi * alias_frequency * t)
assert np.allclose(sampled, np.sin(2 * np.pi * alias_frequency * t_sampled))

plt.figure(figsize=(8, 3.5))
plt.plot(t, original, color="#526d82", alpha=0.6, label="Reference: 23 Hz")
plt.plot(t, alias_wave, "--", color="#4c7067", label="Matching alias: -1 Hz")
plt.stem(t_sampled, sampled, linefmt="C1-", markerfmt="C1o",
         basefmt=" ", label="Samples: 8 Hz")
plt.title("Q4: 23 Hz sine sampled at 8 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.xlim(0, 1)
plt.ylim(-1.2, 1.2)
plt.grid(axis="y", alpha=0.2)
plt.legend(loc="upper right", fontsize=9)
plt.tight_layout()
plt.savefig(figure_folder / "section1_3_wagon_wheel.png", dpi=180)
print(f"Q4: signal {f} Hz, sampling {fs} Hz, {len(sampled)} samples, "
      f"matching alias {alias_frequency} Hz.")
print("Two Section 1.3 figures saved in", figure_folder)
plt.show()
