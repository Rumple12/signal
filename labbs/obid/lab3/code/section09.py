"""Lab 3, Section 9: histograms and histogram equalization."""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


def compute_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return hist / hist.sum()


def cumulative_histogram(hist):
    return np.cumsum(hist)


lab_folder = Path(__file__).resolve().parent.parent
image_path = lab_folder / "assets" / "ManWoman.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read {image_path}")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Q9.1: calculate the relative frequency and cumulative fraction of pixels.
hist = compute_histogram(gray)
cdf = cumulative_histogram(hist)
print(f"Image size: {gray.shape[1]} x {gray.shape[0]}, {gray.size} pixels")
print(f"Histogram peak: {np.argmax(hist)}")
print(f"Mean intensity: {gray.mean():.2f}")
print(f"CDF at 127: {cdf[127]:.2%}")
print(f"CDF at 191: {cdf[191]:.2%}")

# Q9.2: reduce contrast, then map the intensities using the CDF.
contrast = 0.60
reduced = np.clip(
    np.rint(128 + contrast * (gray.astype(float) - 128)), 0, 255
).astype(np.uint8)
hist_reduced = compute_histogram(reduced)
cdf_reduced = cumulative_histogram(hist_reduced)
lut = np.floor(255 * cdf_reduced)
lut = np.clip(lut, 0, 255).astype(np.uint8)
equalized = lut[reduced]
opencv_equalized = cv2.equalizeHist(reduced)

# Subtract signed values so differences cannot wrap around at zero.
difference = np.abs(equalized.astype(np.int16) - opencv_equalized.astype(np.int16))
print(f"Reduced-contrast range: {reduced.min()}–{reduced.max()}")
print(f"CDF-equalized range: {equalized.min()}–{equalized.max()}")
print(f"Maximum absolute difference from OpenCV: {difference.max()}")
print(f"Mean absolute difference from OpenCV: {difference.mean():.4f}")

fig = plt.figure(figsize=(9, 4.5), layout="constrained")
grid = fig.add_gridspec(2, 4, height_ratios=(1.3, 1))
levels = np.arange(256)

ax = fig.add_subplot(grid[0, :2])
ax.bar(levels, hist.ravel(), width=1, color="#185c4b")
ax.set_title("Original normalized histogram")
ax.set_xlabel("Intensity")
ax.set_ylabel("Fraction of pixels")
ax.set_xlim(0, 255)

ax = fig.add_subplot(grid[0, 2:])
ax.plot(levels, cdf, color="#185c4b")
ax.set_title("Original cumulative histogram")
ax.set_xlabel("Intensity")
ax.set_ylabel("Cumulative fraction")
ax.set_xlim(0, 255)
ax.set_ylim(0, 1)

pictures = [gray, reduced, equalized, opencv_equalized]
titles = ["Original grayscale", "Reduced contrast", "CDF equalization", "OpenCV equalization"]
for column, (pixels, title) in enumerate(zip(pictures, titles)):
    ax = fig.add_subplot(grid[1, column])
    ax.imshow(pixels, cmap="gray", vmin=0, vmax=255)
    ax.set_title(title)
    ax.axis("off")

figure_path = lab_folder / "figures" / "section09_histogram_equalization.png"
fig.savefig(figure_path, dpi=180)
print(f"Saved {figure_path.name}")
