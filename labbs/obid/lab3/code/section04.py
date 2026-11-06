"""Lab 3, Section 4: Gaussian filtering and Sobel edges."""

import time
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


def measure_filter(method, image, *kernels):
    border = cv2.BORDER_REFLECT_101
    method(image, cv2.CV_64F, *kernels, borderType=border)  # Warm up once.
    times = []
    for _ in range(20):
        start = time.perf_counter()
        result = method(image, cv2.CV_64F, *kernels, borderType=border)
        times.append((time.perf_counter() - start) * 1000)
    return result, np.median(times)


def detect_horizontal_edges(gray):
    gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    return gx, gy


lab_folder = Path(__file__).resolve().parent.parent
image_path = lab_folder / "assets" / "ManWoman.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read {image_path}")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_float = gray.astype(np.float64)

# Q4.1: use equivalent kernels and the same input and border handling.
print("Kernel   Ordinary 2D (ms)   Separable (ms)   Faster         Outputs match")
for size in [5, 11, 21]:
    kernel_1d = cv2.getGaussianKernel(size, 1.0)
    kernel_2d = kernel_1d @ kernel_1d.T
    ordinary, ordinary_ms = measure_filter(cv2.filter2D, gray_float, kernel_2d)
    separable, separable_ms = measure_filter(cv2.sepFilter2D, gray_float, kernel_1d, kernel_1d)
    faster = "Separable" if separable_ms < ordinary_ms else "Ordinary 2D"
    matches = np.allclose(ordinary, separable)
    print(f"{size:2d} x {size:<2d} {ordinary_ms:17.3f} {separable_ms:16.3f}   "
          f"{faster:<14} {matches}")

# Q4.2 and Q4.3: keep the signed derivatives for the magnitude calculation.
gx, gy = detect_horizontal_edges(gray)
horizontal = np.abs(gy)
vertical = np.abs(gx)
edge_max = max(horizontal.max(), vertical.max())
magnitude = np.sqrt(gx**2 + gy**2)
magnitude_display = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

fig, axes = plt.subplots(2, 2, figsize=(8.4, 5.6), layout="constrained")
panels = [
    (gray, "Original grayscale", 255),
    (horizontal, "Horizontal Sobel edges |gy|", edge_max),
    (vertical, "Vertical Sobel edges |gx|", edge_max),
    (magnitude_display, "Gradient magnitude (normalized 0–255)", 255),
]
for ax, (pixels, title, upper_limit) in zip(axes.flat, panels):
    ax.imshow(pixels, cmap="gray", vmin=0, vmax=upper_limit)
    ax.set_title(title)
    ax.axis("off")

figure_path = lab_folder / "figures" / "section04_sobel_comparison.png"
fig.savefig(figure_path, dpi=180)
print(f"Saved {figure_path.name}")
