"""Lab 3, Section 2: channel histograms and chroma subsampling."""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


lab_folder = Path(__file__).resolve().parent.parent
image_path = lab_folder / "assets" / "ManWoman.png"
figure_folder = lab_folder / "figures"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read {image_path}")

# OpenCV loads BGR and stores the converted channels in Y, Cr, Cb order.
ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(ycrcb)
b, g, r = cv2.split(image)

# Q2.1: use the same 256 bins and count scale for all four histograms.
channels = [y, r, g, b]
names = ["Y", "R", "G", "B"]
colors = ["#4f4f4f", "#b74b4b", "#328363", "#3b6a9e"]
histograms = [np.histogram(channel, bins=256, range=(0, 256))[0]
              for channel in channels]
max_count = max(histogram.max() for histogram in histograms)
fig, axes = plt.subplots(2, 2, figsize=(8.4, 4.8), layout="constrained")
for ax, channel, name, color, histogram in zip(
        axes.flat, channels, names, colors, histograms):
    print(f"{name} standard deviation: {channel.std():.2f}")
    ax.bar(np.arange(256), histogram, width=1, color=color)
    ax.set_title(f"{name} channel")
    ax.set_xlabel("Intensity")
    ax.set_ylabel("Pixel count")
    ax.set_xlim(-0.5, 255.5)
    ax.set_ylim(0, 1.05 * max_count)

fig.savefig(figure_folder / "section02_channel_histograms.png", dpi=180)

# Q2.2: count bytes before enlarging the chroma channels for display.
height, width = y.shape
original_bytes = y.nbytes + cr.nbytes + cb.nbytes
print(f"Factor 1: {original_bytes} bytes, 0.00% saving")
comparison = [image]
titles = ["Original", "Factor 2", "Factor 4", "Factor 8"]
for factor in [2, 4, 8]:
    reduced_size = (width // factor, height // factor)
    cr_small = cv2.resize(cr, reduced_size, interpolation=cv2.INTER_AREA)
    cb_small = cv2.resize(cb, reduced_size, interpolation=cv2.INTER_AREA)
    stored_bytes = y.nbytes + cr_small.nbytes + cb_small.nbytes
    saving = 100 * (1 - stored_bytes / original_bytes)
    print(f"Factor {factor}: {stored_bytes} bytes, {saving:.2f}% saving")

    cr_full = cv2.resize(cr_small, (width, height), interpolation=cv2.INTER_LINEAR)
    cb_full = cv2.resize(cb_small, (width, height), interpolation=cv2.INTER_LINEAR)
    reconstructed = cv2.merge((y, cr_full, cb_full))
    comparison.append(cv2.cvtColor(reconstructed, cv2.COLOR_YCrCb2BGR))

# Use one crop around a strong chroma change in the factor-8 result.
crop_size = 96
chroma_change = cv2.absdiff(cr, cr_full).astype(float) + cv2.absdiff(cb, cb_full)
crop_score = cv2.blur(chroma_change, (crop_size, crop_size))
row, column = np.unravel_index(np.argmax(crop_score), crop_score.shape)
top = int(np.clip(row - crop_size // 2, 0, height - crop_size))
left = int(np.clip(column - crop_size // 2, 0, width - crop_size))

fig, axes = plt.subplots(2, 4, figsize=(9.5, 4.4), layout="constrained")
for column, (picture, title) in enumerate(zip(comparison, titles)):
    rgb = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    crop = rgb[top:top + crop_size, left:left + crop_size]
    axes[0, column].imshow(rgb)
    axes[0, column].set_title(title)
    axes[0, column].axis("off")
    axes[1, column].imshow(crop, interpolation="nearest")
    axes[1, column].axis("off")

fig.supxlabel("Bottom row: matching enlarged crops", fontsize=10)
fig.savefig(figure_folder / "section02_chroma_subsampling.png", dpi=180)
print("Saved Figures 2 and 3.")
