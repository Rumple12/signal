"""Lab 3, Section 7: elementary images and triangle approximation."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# Q7.1: use the teacher's basis vectors to build four images.
size = 16
ramp = np.linspace(0, 1, size)
step = np.heaviside(np.arange(size) - size/2, 1)
sine = np.sin(2 * np.pi * np.arange(size) / size)

e1 = np.outer(step, step)
e2 = np.outer(step, ramp)
e3 = np.outer(ramp, step)
e4 = np.outer(sine, sine)
titles = ["Step × Step", "Step × Ramp", "Ramp × Step", "Sine × Sine"]

# Q7.2: fit the lower-right triangle using only the first three images.
rows, cols = np.indices((16, 16))
target = ((rows >= 8) & (cols >= 8) & (cols <= rows)).astype(float)
A = np.column_stack([e1.ravel(), e2.ravel(), e3.ravel()])
weights = np.linalg.lstsq(A, target.ravel(), rcond=None)[0]
approximation = (A @ weights).reshape(16, 16)
error = target - approximation
mse = np.mean(error**2)

print(f"Target pixels with value 1: {np.count_nonzero(target)}")
for title, weight in zip(titles, weights):
    print(f"{title}: {weight:.6f}")
print(f"MSE: {mse:.7f}")

fig = plt.figure(figsize=(9, 4.7), layout="constrained")
grid = fig.add_gridspec(2, 1)
top = grid[0].subgridspec(1, 4)
bottom = grid[1].subgridspec(1, 3)

for column, (pixels, title) in enumerate(zip([e1, e2, e3, e4], titles)):
    ax = fig.add_subplot(top[0, column])
    ax.imshow(pixels, cmap="gray", vmin=-1, vmax=1, interpolation="nearest")
    ax.set_title(title)
    ax.axis("off")

# Keep the same limits for the target and approximation, including negatives.
lower = min(target.min(), approximation.min())
upper = max(target.max(), approximation.max())
comparison_axes = []
for column, (pixels, title) in enumerate(zip(
        [target, approximation], ["Target triangle", "Three-image approximation"])):
    ax = fig.add_subplot(bottom[0, column])
    comparison_axes.append(ax)
    intensity_plot = ax.imshow(pixels, cmap="gray", vmin=lower, vmax=upper,
                               interpolation="nearest")
    ax.set_title(title)
    ax.axis("off")
fig.colorbar(intensity_plot, ax=comparison_axes, shrink=0.8)

ax = fig.add_subplot(bottom[0, 2])
limit = np.max(np.abs(error))
error_plot = ax.imshow(error, cmap="RdBu_r", vmin=-limit, vmax=limit,
                       interpolation="nearest")
ax.set_title("Target minus approximation")
ax.axis("off")
fig.colorbar(error_plot, ax=ax, shrink=0.8)

lab_folder = Path(__file__).resolve().parent.parent
figure_path = lab_folder / "figures" / "section07_elementary_images.png"
fig.savefig(figure_path, dpi=180)
print(f"Saved {figure_path.name}")
