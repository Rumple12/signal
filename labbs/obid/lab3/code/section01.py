"""Lab 3, Section 1: gamma correction and intensity histograms."""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


def apply_gamma(image, gamma):
    normalized = image.astype(np.float32) / 255.0
    corrected_image = 255 * np.power(normalized, gamma)
    return np.uint8(corrected_image)


# Q1.1: apply gamma 2.0 to the three given intensities.
inputs = np.array([64, 128, 192], dtype=np.uint8)
outputs = apply_gamma(inputs, 2.0)
for input_value, output_value in zip(inputs, outputs):
    print(f"{input_value} -> {output_value}")

# Q1.2: compare the grayscale image before and after gamma correction.
lab_folder = Path(__file__).resolve().parent.parent
image_path = lab_folder / "assets" / "ManWoman.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read {image_path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
corrected = apply_gamma(gray, 2.2)
original_hist, _ = np.histogram(gray, bins=256, range=(0, 256))
corrected_hist, _ = np.histogram(corrected, bins=256, range=(0, 256))
print(f"Image size: {gray.shape[1]} x {gray.shape[0]} pixels")
print(f"Original mean: {gray.mean():.2f}; median: {np.median(gray):g}")
print(f"Corrected mean: {corrected.mean():.2f}; median: {np.median(corrected):g}")

# Use the same intensity and count scales in both columns.
fig, axes = plt.subplots(2, 2, figsize=(8.4, 5.6), layout="constrained")
intensities = np.arange(256)
max_count = max(original_hist.max(), corrected_hist.max())
for column, (pixels, histogram, title) in enumerate([
        (gray, original_hist, "Original grayscale"),
        (corrected, corrected_hist, "Gamma corrected (gamma = 2.2)")]):
    axes[0, column].imshow(pixels, cmap="gray", vmin=0, vmax=255)
    axes[0, column].set_title(title)
    axes[0, column].axis("off")

    axes[1, column].bar(intensities, histogram, width=1, color="#185c4b")
    axes[1, column].set_title("Original histogram" if column == 0 else "Corrected histogram")
    axes[1, column].set_xlabel("Intensity")
    axes[1, column].set_ylabel("Pixel count")
    axes[1, column].set_xlim(-0.5, 255.5)
    axes[1, column].set_ylim(0, 1.05 * max_count)

figure_path = lab_folder / "figures" / "section01_gamma_comparison.png"
fig.savefig(figure_path, dpi=180)
print(f"Saved {figure_path.name}")
