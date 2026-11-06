"""Lab 3, Section 6: logarithmic intensity mapping and lookup tables."""

import time
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


def log_transform(values, strength):
    r = values.astype(np.float64)
    u = (r - 127.5) / 127.5
    return 127.5 * (
        1 + np.sign(u) * np.log1p(strength * np.abs(u)) / np.log1p(strength)
    )


def direct_computation_T(values, strength=3.0):
    output = log_transform(values, strength)
    return np.uint8(np.clip(output, 0, 255))


def create_lookup_table(strength=3.0):
    levels = np.arange(256, dtype=np.uint8)
    return direct_computation_T(levels, strength)


lab_folder = Path(__file__).resolve().parent.parent
image_path = lab_folder / "assets" / "ManWoman.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read {image_path}")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Q6.1: build the table once and time its construction separately.
start = time.time()
lut = create_lookup_table()
build_ms = (time.time() - start) * 1000

direct_computation_T(gray)  # Warm up the direct method.
start = time.time()
for _ in range(20):
    direct_result = direct_computation_T(gray)
direct_ms = (time.time() - start) * 1000 / 20

lookup_result = lut[gray]  # Warm up the lookup method.
start = time.time()
for _ in range(20):
    lookup_result = lut[gray]
lookup_ms = (time.time() - start) * 1000 / 20

print(f"Direct NumPy average: {direct_ms:.2f} ms")
print(f"Lookup application average: {lookup_ms:.2f} ms")
print(f"Lookup table construction: {build_ms:.3f} ms")
print(f"Direct-to-lookup time ratio: {direct_ms / lookup_ms:.2f}")
print(f"Outputs match: {np.array_equal(direct_result, lookup_result)}")

# Q6.2: verify the integer values and plot the continuous transfer function.
inputs = np.array([0, 32, 64, 112, 128, 144, 192, 224, 255], dtype=np.uint8)
outputs = direct_computation_T(inputs)
print(f"Test mappings: {list(zip(inputs.tolist(), outputs.tolist()))}")

levels = np.linspace(0, 255, 511)
fig, ax = plt.subplots(figsize=(6.4, 3.8), layout="constrained")
ax.plot(levels, log_transform(levels, 3.0), color="#185c4b",
        label="Logarithmic (strength = 3)")
ax.plot(levels, levels, "--", color="#666666", label="Linear (y = x)")
ax.set_xlabel("Input intensity")
ax.set_ylabel("Output intensity")
ax.set_xlim(0, 255)
ax.set_ylim(0, 255)
ax.grid(alpha=0.25)
ax.legend(fontsize=9)

figure_path = lab_folder / "figures" / "section06_log_transform.png"
fig.savefig(figure_path, dpi=180)
print(f"Saved {figure_path.name}")
