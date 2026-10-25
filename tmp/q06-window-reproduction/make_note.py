"""Trace the exam scan; do not assume analytical window functions."""
from pathlib import Path
import sys

WORK = Path(__file__).resolve().parent
ROOT = WORK.parent.parent
sys.path.insert(0, str(ROOT / "tmp" / "q03c-python"))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from PIL import Image, ImageChops

OUTPUT = ROOT / "Q06_window_spectra_answer_384.png"
source = np.asarray(Image.open(WORK / "four-plots-source.png").convert("RGB"), dtype=float)

# Pixel coordinates of the four plot frames in the rendered exam scan.
# The vertical scales are read from the original axes. These numbers calibrate
# the scan only; they are not window coefficients or analytical curve models.
frames = {
    "i": (80, 445, 61, 352, -5, 25),
    "ii": (541, 919, 49, 350, 0, 10),
    "iii": (83, 446, 431, 727, -10, 40),
    "iv": (538, 917, 431, 729, -0.5, 10),
}

def smooth_interpolation(x, y, target):
    """Shape-preserving cubic interpolation of digitized samples."""
    dx = np.diff(x)
    secant = np.diff(y) / dx
    slope = np.zeros_like(y)
    slope[0], slope[-1] = secant[0], secant[-1]
    for k in range(1, len(y)-1):
        if secant[k-1] * secant[k] > 0:
            w1, w2 = 2*dx[k]+dx[k-1], dx[k]+2*dx[k-1]
            slope[k] = (w1+w2)/(w1/secant[k-1]+w2/secant[k])
    k = np.searchsorted(x, target, side="right")-1
    k = np.clip(k, 0, len(x)-2)
    width = x[k+1]-x[k]
    t = (target-x[k])/width
    values = ((2*t**3-3*t**2+1)*y[k]
              + (t**3-2*t**2+t)*width*slope[k]
              + (-2*t**3+3*t**2)*y[k+1]
              + (t**3-t**2)*width*slope[k+1])
    return values

def trace(frame):
    x0, x1, y0, y1, lower, upper = frame
    crop = source[y0+2:y1-1, x0+2:x1-1]
    red = crop[:, :, 0]-crop[:, :, 1]
    red_blue = crop[:, :, 0]-crop[:, :, 2]
    mask = (red > 8) & (red_blue > 5)
    xx, yy = [], []
    for column in range(crop.shape[1]):
        weights = np.where(mask[:, column], red[:, column]**2, 0)
        if weights.sum() > 0:
            xx.append(column+x0+2)
            yy.append(np.dot(weights, np.arange(len(weights))+y0+2)/weights.sum())
    xx = np.asarray(xx, dtype=float)
    yy = upper-(np.asarray(yy)-y0)/(y1-y0)*(upper-lower)
    # Suppress single-pixel scan noise without flattening oscillating lobes.
    yy = np.convolve(np.pad(yy, (1, 1), mode="edge"), [0.25, 0.5, 0.25], mode="valid")
    center = xx[np.argmax(yy)]
    # Correct the scan's small centering/skew error so the central peak is at 0.
    frequencies = np.where(xx <= center,
                           (xx-center)/(center-x0)*np.pi,
                           (xx-center)/(x1-center)*np.pi)
    frequencies = np.r_[-np.pi, frequencies, np.pi]
    yy = np.r_[yy[0], yy, yy[-1]]
    samples = np.linspace(-np.pi, np.pi, 8001)
    curve = smooth_interpolation(frequencies, yy, samples)
    return samples, curve

curves = {name: trace(frame) for name, frame in frames.items()}
metrics = {}
for name, (omega, values) in curves.items():
    half_peak = np.flatnonzero(values >= values.max()/2)
    width = (omega[half_peak[-1]]-omega[half_peak[0]])/np.pi
    outer_level = np.max(np.abs(values[np.abs(omega) >= 0.35*np.pi]))/values.max()
    metrics[name] = {"peak": float(values.max()), "minimum": float(values.min()),
                     "half_height_width_over_pi": float(width),
                     "outer_level_relative_to_peak": float(outer_level)}
    np.savetxt(WORK / f"traced-{name}.csv", np.column_stack([omega, values]),
               delimiter=",", header="Omega,digitized_signed_spectrum", comments="")
assert metrics["iv"]["half_height_width_over_pi"] > max(
    metrics[name]["half_height_width_over_pi"] for name in ("i", "ii", "iii"))
assert metrics["iii"]["half_height_width_over_pi"] < metrics["i"]["half_height_width_over_pi"]
assert metrics["iv"]["outer_level_relative_to_peak"] < min(
    metrics[name]["outer_level_relative_to_peak"] for name in ("i", "ii", "iii"))
assert metrics["i"]["minimum"] < -3 and metrics["iii"]["minimum"] < -5

plt.rcParams.update({
    "font.family": "STIXGeneral", "mathtext.fontset": "cm",
    "font.size": 10.8, "axes.labelsize": 12,
    "axes.linewidth": 0.8, "figure.facecolor": "white",
    "axes.facecolor": "white", "text.color": "black",
    "axes.edgecolor": "black", "axes.labelcolor": "black",
    "xtick.color": "black", "ytick.color": "black",
})

# Measure wrapping in final output pixels, instead of shrinking a large page.
measure_fig = plt.figure(figsize=(3.84, 1), dpi=100)
measure_fig.canvas.draw()
renderer = measure_fig.canvas.get_renderer()

def wrapped(text, size=11, weight="normal", available=368):
    properties = FontProperties(family="STIXGeneral", size=size, weight=weight)
    lines, current = [], ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        width = renderer.get_text_width_height_descent(candidate, properties, False)[0]
        if width > available and current:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return "\n".join(lines), len(lines)

text_items = []
def add_text(top, text, size=11, weight="normal", indent=8, spacing=1.18):
    content, count = wrapped(text, size, weight, 384-indent-8)
    text_items.append((top, indent, content, size, weight, spacing))
    return top+count*size*100/72*spacing

cursor = add_text(8, "Question 6 – Window spectra", 12.5, "bold")
cursor = add_text(cursor+3, "Approximate redraws from the exam figure.", 10.5)
plots_top = int(np.ceil(cursor+13))
block_height = 239
cursor = plots_top+4*block_height+3

cursor = add_text(cursor, "(a) Best time resolution: iv", 11.8, "bold")
cursor = add_text(cursor+3, "Reason:", 11, "bold")
cursor = add_text(cursor+4,
    "Window iv has the widest main lobe. "
    "A wider main lobe corresponds to a shorter time window, "
    "which gives better time resolution.")
cursor = add_text(cursor+12, "(b) Least spectral leakage: iv", 11.8, "bold")
cursor = add_text(cursor+3, "Reason:", 11, "bold")
cursor = add_text(cursor+4,
    "Window iv has the smallest side lobes. "
    "Smaller side lobes mean less spectral leakage.")
cursor = add_text(cursor+12, "Reminder", 11.8, "bold")
for reminder in [
    "Wide main lobe → better time resolution",
    "Narrow main lobe → better frequency resolution",
    "Small side lobes → less spectral leakage",
]:
    cursor = add_text(cursor+3, reminder)
height = int(np.ceil(cursor+7))
plt.close(measure_fig)

fig = plt.figure(figsize=(3.84, height/100), dpi=100)
all_text = []
for top, left, text, size, weight, spacing in text_items:
    all_text.append(fig.text(left/384, 1-top/height, text, fontsize=size,
                             weight=weight, ha="left", va="top", linespacing=spacing))

axis_limits = {"i": (-5.5, 25), "ii": (-0.2, 10.5),
               "iii": (-10, 40), "iv": (-0.5, 10)}
tick_values = {"i": [-5, 0, 5, 10, 15, 20, 25], "ii": [0, 2, 4, 6, 8, 10],
               "iii": [-10, 0, 10, 20, 30, 40], "iv": [0, 2, 4, 6, 8, 10]}
axes = []
for index, name in enumerate(frames):
    top = plots_top+index*block_height
    all_text.append(fig.text(8/384, 1-top/height, f"{name})", fontsize=11.8,
                             weight="bold", ha="left", va="top"))
    axis_top, axis_height = top+24, 171
    ax = fig.add_axes([43/384, 1-(axis_top+axis_height)/height, 326/384, axis_height/height])
    omega, values = curves[name]
    ax.plot(omega, values, color="#b31d32", linewidth=1.4, zorder=3)
    ax.axhline(0, color="#777777", linewidth=0.6, zorder=1)
    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(*axis_limits[name])
    ax.set_xticks([-np.pi, 0, np.pi], [r"$-\pi$", r"$0$", r"$\pi$"])
    ax.set_yticks(tick_values[name])
    ax.set_xlabel(r"$\Omega$", labelpad=1)
    ax.tick_params(direction="out", length=3, width=0.7, pad=3)
    axes.append(ax)
    all_text.extend([ax.xaxis.label, *ax.get_xticklabels(), *ax.get_yticklabels()])

fig.canvas.draw()
renderer = fig.canvas.get_renderer()
for artist in all_text:
    box = artist.get_window_extent(renderer)
    assert box.x0 >= 2 and box.y0 >= 2, (artist.get_text(), box)
    assert box.x1 <= 382 and box.y1 <= height-2, (artist.get_text(), box)
assert len(axes) == 4
fig.savefig(OUTPUT, dpi=100, facecolor="white", transparent=False)
plt.close(fig)

with Image.open(OUTPUT) as result:
    assert result.size == (384, height)
    assert result.getpixel((0, 0))[:3] == (255, 255, 255)
    for index, top in enumerate(range(0, height, 720), start=1):
        result.crop((0, top, 384, min(top+720, height))).save(WORK / f"review-{index}.png")

print(f"Saved: {OUTPUT}")
print(f"Dimensions: 384 x {height} pixels; four vertical plots included")
for name, values in metrics.items():
    print(name, values)
print("Verified: iv is broadest and has the smallest outer lobes; signed negative lobes retained.")
print("Verified: all axes, graph labels, and answer text remain inside the image.")
