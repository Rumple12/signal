"""Render the requested calculator graph without editing any exam sources."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tmp" / "q03c-python"))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

OUTPUT = ROOT / "Q03c_frequency_response_384.png"

def magnitude(omega):
    return 1.0 / np.sqrt(1.89 - 0.2 * np.cos(omega) - 1.6 * np.cos(2 * omega))

omega = np.linspace(0.0, 2.0 * np.pi, 20001)
response = magnitude(omega)
complex_response = np.abs(1.0 / (1.0 - 0.5 * np.exp(-1j * omega)
                                  - 0.8 * np.exp(-2j * omega)))
np.testing.assert_allclose(response, complex_response, rtol=1e-13, atol=1e-13)

reference_x = np.arange(5) * np.pi / 2
reference_y = magnitude(reference_x)
np.testing.assert_allclose(reference_y, [10/3, 1/np.sqrt(3.49), 10/7,
                                        1/np.sqrt(3.49), 10/3], atol=1e-12)
minimum_x = np.array([np.arccos(-1/32), 2*np.pi - np.arccos(-1/32)])
minimum_y = magnitude(minimum_x)
np.testing.assert_allclose(minimum_y, 1/np.sqrt(3.493125), atol=1e-12)
assert np.all(np.abs(minimum_y - 0.535) < 0.001)

plt.rcParams.update({
    "font.family": "STIXGeneral",
    "mathtext.fontset": "cm",
    "font.size": 10.5,
    "axes.labelsize": 12,
    "axes.linewidth": 0.8,
    "text.color": "black",
    "axes.edgecolor": "black",
    "axes.labelcolor": "black",
    "xtick.color": "black",
    "ytick.color": "black",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})

# Render directly at the final pixel dimensions; never shrink the labels later.
fig = plt.figure(figsize=(3.84, 3.00), dpi=100)
ax = fig.add_axes([0.155, 0.175, 0.800, 0.705])
fig.text(0.5, 0.955, "Q3(c)  Frequency response", ha="center", va="top",
         fontsize=11.5, fontweight="bold")
ax.plot(omega, response, color="#111111", linewidth=1.8, zorder=3)
ax.plot(reference_x, reference_y, linestyle="none", marker="o",
        markersize=4.2, markerfacecolor="black", markeredgecolor="black",
        clip_on=False, zorder=4)

ax.set_xlim(0.0, 2*np.pi)
ax.set_ylim(0.0, 3.6)
ax.set_xticks(reference_x,
              [r"$0$", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
ax.set_yticks(np.arange(0.0, 3.51, 0.5),
              ["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5"])
ax.set_xlabel(r"$\Omega$", labelpad=3)
ax.set_ylabel(r"$|H(e^{j\Omega})|$", labelpad=5)
ax.spines[["top", "right"]].set_visible(False)
ax.tick_params(direction="out", length=3, width=0.8, pad=4)
ax.set_axisbelow(True)
ax.grid(axis="y", color="#dddddd", linewidth=0.45)

for index, (x, y) in enumerate(zip(reference_x, reference_y)):
    if index == 0:
        offset, ha, va = (7, -1), "left", "top"
    elif index == 4:
        offset, ha, va = (-7, -1), "right", "top"
    elif index == 2:
        offset, ha, va = (0, 6), "center", "bottom"
    else:
        offset, ha, va = (0, -8), "center", "top"
    ax.annotate(f"{y:.3f}", (x, y), xytext=offset,
                textcoords="offset points", ha=ha, va=va, fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.3},
                zorder=5)

fig.canvas.draw()
renderer = fig.canvas.get_renderer()
visible_text = [ax.xaxis.label, ax.yaxis.label,
                *ax.get_xticklabels(), *ax.get_yticklabels(),
                *ax.texts, *fig.texts]
for artist in visible_text:
    box = artist.get_window_extent(renderer)
    assert box.x0 >= 1 and box.y0 >= 1, (artist.get_text(), box)
    assert box.x1 <= 383 and box.y1 <= 299, (artist.get_text(), box)

fig.savefig(OUTPUT, dpi=100, facecolor="white", transparent=False)
plt.close(fig)
with Image.open(OUTPUT) as result:
    assert result.size == (384, 300), result.size
    assert result.getpixel((0, 0))[:3] == (255, 255, 255)

print(f"Saved: {OUTPUT}")
print("Dimensions: 384 x 300 pixels; 20,001 frequency samples")
print("Reference magnitudes: " + ", ".join(f"{v:.9f}" for v in reference_y))
print("Minimum frequencies/pi: " + ", ".join(f"{v/np.pi:.9f}" for v in minimum_x))
print("Minimum magnitudes: " + ", ".join(f"{v:.9f}" for v in minimum_y))
print("Verified: complex expression agrees, all text stays inside the canvas.")
