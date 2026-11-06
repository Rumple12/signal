"""Lab 3, Section 8: centred FFT and ideal frequency filtering."""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


def ideal_lowpass(shape, cutoff):
    rows, cols = shape
    row, col = np.indices(shape)
    distance_squared = (row - rows//2)**2 + (col - cols//2)**2
    return distance_squared < cutoff**2


lab_folder = Path(__file__).resolve().parent.parent
image_path = lab_folder / "assets" / "ManWoman.png"
image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError(f"Could not read {image_path}")
gray = image.astype(np.float64)

# Q8.1: move zero frequency to the centre for display and filtering.
F = np.fft.fft2(gray)
F_shift = np.fft.fftshift(F)
magnitude = np.log1p(np.abs(F_shift))
rows, cols = gray.shape
centre_row, centre_col = rows//2, cols//2

# Q8.2: keep only the bins inside the circular low-pass mask.
cutoff = 40
mask = ideal_lowpass(gray.shape, cutoff)
F_low = F_shift * mask
low_pass = np.fft.ifft2(np.fft.ifftshift(F_low)).real

# Q8.3: keep the signed difference and verify reconstruction.
high_pass = gray - low_pass
reconstructed = low_pass + high_pass
max_error = np.max(np.abs(gray - reconstructed))
print(f"Image shape: {rows} rows x {cols} columns")
print(f"FFT centre: row {centre_row}, column {centre_col}")
print(f"Low-pass cutoff: {cutoff} bins")
print(f"Low-pass mean: {low_pass.mean():.4f}")
print(f"High-pass mean: {high_pass.mean():.3e}")
print(f"Maximum reconstruction error: {max_error:.3e}")
print(f"Reconstruction matches: {np.allclose(gray, reconstructed, rtol=0, atol=1e-12)}")

fig, axes = plt.subplots(2, 2, figsize=(8.8, 5.8), layout="constrained")
axes[0, 0].imshow(gray, cmap="gray", vmin=0, vmax=255)
axes[0, 0].set_title("Original grayscale")
axes[0, 0].axis("off")

frequency_extent = (-centre_col - 0.5, cols - centre_col - 0.5,
                    -centre_row - 0.5, rows - centre_row - 0.5)
axes[0, 1].imshow(magnitude, cmap="magma", origin="lower",
                  extent=frequency_extent, interpolation="nearest")
axes[0, 1].set_title("Centred 2D FFT (log magnitude)")
axes[0, 1].set_xlabel("Horizontal frequency (bin)")
axes[0, 1].set_ylabel("Vertical frequency (bin)")

axes[1, 0].imshow(low_pass, cmap="gray", vmin=0, vmax=255)
axes[1, 0].set_title("Low-pass reconstruction (radius 40 bins)")
axes[1, 0].axis("off")

limit = np.max(np.abs(high_pass))
high_plot = axes[1, 1].imshow(high_pass, cmap="gray", vmin=-limit, vmax=limit)
axes[1, 1].set_title("High-pass (original minus low-pass)")
axes[1, 1].axis("off")
fig.colorbar(high_plot, ax=axes[1, 1], shrink=0.8, label="Signed intensity difference")

figure_path = lab_folder / "figures" / "section08_fft_filters.png"
fig.savefig(figure_path, dpi=180)
print(f"Saved {figure_path.name}")
