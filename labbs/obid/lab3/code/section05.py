"""Lab 3, Section 5: vector operations and convolution matrix storage."""

import time
from pathlib import Path

import cv2
import numpy as np


brightness = 15
contrast = 1.15
centre = 128


def adjust_vector(image):
    pixels = image.reshape(-1, 1).astype(float)
    adjusted = contrast * (pixels - centre) + centre + brightness
    return np.clip(adjusted, 0, 255).astype(np.uint8).reshape(image.shape)


def adjust_loops(image):
    height, width = image.shape
    result = np.empty_like(image)
    for row in range(height):
        for column in range(width):
            pixel = float(image[row, column])
            adjusted = contrast * (pixel - centre) + centre + brightness
            result[row, column] = int(min(max(adjusted, 0), 255))
    return result


def measure(adjust, image):
    adjust(image)  # One warm-up before timing.
    times = []
    for _ in range(3):
        start = time.perf_counter()
        result = adjust(image)
        times.append((time.perf_counter() - start) * 1000)
    return result, np.median(times)


lab_folder = Path(__file__).resolve().parent.parent
image_path = lab_folder / "assets" / "ManWoman.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read {image_path}")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Q5.1: time the same adjustment, including output creation and conversion.
vector_result, vector_ms = measure(adjust_vector, gray)
loop_result, loop_ms = measure(adjust_loops, gray)
print(f"Vectorized NumPy median: {vector_ms:.2f} ms")
print(f"Nested loops median: {loop_ms:.2f} ms")
print(f"Loop-to-vector time ratio: {loop_ms / vector_ms:.2f}")
print(f"Outputs match: {np.array_equal(vector_result, loop_result)}")

# Q5.2: calculate the storage for H without allocating the matrix.
pixels = 512 * 512
elements = pixels ** 2
float32_gib = elements * 4 / (1024 ** 3)
float64_gib = elements * 8 / (1024 ** 3)
print(f"H dimensions: {pixels} x {pixels}")
print(f"H elements: {elements}")
print(f"float32: {float32_gib:g} GiB")
print(f"float64: {float64_gib:g} GiB")
