"""Lab 3, Section 11: morphological object counting and edge detection."""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


lab_folder = Path(__file__).resolve().parent.parent

# Q11.1: draw three separate objects and four isolated pixels.
binary = np.zeros((180, 260), dtype=np.uint8)
cv2.circle(binary, (45, 58), 22, 255, thickness=-1)
cv2.rectangle(binary, (98, 34), (145, 85), 255, thickness=-1)
triangle = np.array([(185, 87), (228, 87), (208, 28)], dtype=np.int32)
cv2.fillPoly(binary, [triangle], 255)
for x, y in [(18, 135), (80, 145), (160, 144), (243, 150)]:
    binary[y, x] = 255

cross_kernel = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
], dtype=np.uint8)
disk_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, cross_kernel)
cleaned = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, disk_kernel)
before, _ = cv2.connectedComponents(binary, connectivity=8)
n, labels, stats, centroids = cv2.connectedComponentsWithStats(
    cleaned, connectivity=8
)
object_count = n - 1  # Label zero is the background.

# Check an interior pixel of each known shape for a separate foreground label.
shape_labels = {labels[58, 45], labels[60, 121], labels[67, 208]}
shapes_preserved = len(shape_labels) == 3 and 0 not in shape_labels
print(f"Foreground components before filtering: {before - 1}")
print(f"Foreground components after filtering: {object_count}")
print(f"Circle, rectangle and triangle preserved as separate objects: {shapes_preserved}")

# Q11.2: compare dilation minus erosion with Sobel magnitude.
image_path = lab_folder / "assets" / "ManWoman.png"
gray = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
if gray is None:
    raise FileNotFoundError(f"Could not read {image_path}")

dilated = cv2.dilate(gray, cross_kernel)
eroded = cv2.erode(gray, cross_kernel)
morph_gradient = cv2.subtract(dilated, eroded)

gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_gradient = np.sqrt(gx**2 + gy**2)
sobel_display = cv2.normalize(sobel_gradient, None, 0, 255, cv2.NORM_MINMAX)

fig, axes = plt.subplots(2, 3, figsize=(9, 4.9), layout="constrained")
panels = [
    (binary, "Original binary image"),
    (cleaned, "After opening and closing"),
    (cleaned, "Detected objects"),
    (gray, "Original grayscale"),
    (morph_gradient, "Morphological gradient\nRaw difference (0–255)"),
    (sobel_display, "Sobel gradient magnitude\nNormalized display (0–255)"),
]
for ax, (pixels, title) in zip(axes.flat, panels):
    ax.imshow(pixels, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
    ax.set_title(title)
    ax.axis("off")

for label, (x, y) in enumerate(centroids[1:], start=1):
    axes[0, 2].text(x, y, str(label), ha="center", va="center",
                    color="black", fontweight="bold")

figure_path = lab_folder / "figures" / "section11_morphology.png"
fig.savefig(figure_path, dpi=180)
print(f"Saved {figure_path.name}")
