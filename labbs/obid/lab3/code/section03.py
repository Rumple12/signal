"""Lab 3, Section 3: colour and grayscale quantization."""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


def quantize(image, bits):
    levels = 2**bits
    step = 256 / levels
    level_indices = (image.astype(np.float32) / step).astype(np.uint8)
    return (level_indices * step).astype(np.uint8)


lab_folder = Path(__file__).resolve().parent.parent
image_path = lab_folder / "assets" / "ManWoman.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read {image_path}")

# Q3.1: quantize each colour channel and compare packed bit depths.
colour_4bit = quantize(image, 4)
height, width, channels = image.shape
original_bits = channels * 8
packed_bits = channels * 4
ratio = original_bits / packed_bits
saving = 100 * (1 - packed_bits / original_bits)
print(f"Image size: {width} x {height} pixels")
print(f"Packed colour depth: {original_bits} -> {packed_bits} bits/pixel")
print(f"Theoretical compression ratio: {ratio:g}:1, saving {saving:g}%")
print(f"Original and quantized uint8 arrays: {image.nbytes} and {colour_4bit.nbytes} bytes")
print(f"4-bit colour levels used: {np.unique(colour_4bit).tolist()}")

# Q3.2: count grayscale pixels before and after mapping to eight levels.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_3bit = quantize(gray, 3)
original_hist, _ = np.histogram(gray, bins=256, range=(0, 256))
quantized_hist, bin_edges = np.histogram(gray_3bit, bins=8, range=(0, 256))
levels = bin_edges[:-1].astype(int)
occupied_levels = levels[quantized_hist > 0]
print(f"Grayscale pixels: {gray.size}")
print(f"Occupied grayscale levels ({len(occupied_levels)}): {occupied_levels.tolist()}")

fig, axes = plt.subplots(2, 2, figsize=(8.4, 5.6), layout="constrained")
for ax, picture, title in zip(axes[0], [image, colour_4bit],
                              ["Original colour", "4 bits per colour channel"]):
    ax.imshow(cv2.cvtColor(picture, cv2.COLOR_BGR2RGB), interpolation="nearest")
    ax.set_title(title)
    ax.axis("off")

axes[1, 0].bar(np.arange(256), original_hist, width=1, color="#185c4b")
axes[1, 0].set_title("Original grayscale (256 bins)")
axes[1, 0].set_xlabel("Intensity")
axes[1, 0].set_ylabel("Pixels per bin")
axes[1, 0].set_xlim(-0.5, 255.5)

axes[1, 1].bar(levels.astype(str), quantized_hist, color="#185c4b")
axes[1, 1].set_title("3-bit grayscale (8 levels)")
axes[1, 1].set_xlabel("Quantized intensity level")
axes[1, 1].set_ylabel("Pixels per level")

figure_path = lab_folder / "figures" / "section03_quantization.png"
fig.savefig(figure_path, dpi=180)
print(f"Saved {figure_path.name}")
