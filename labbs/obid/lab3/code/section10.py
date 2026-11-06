"""Lab 3, Section 10: noise reduction and PSNR comparisons."""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


lab_folder = Path(__file__).resolve().parent.parent
image_path = lab_folder / "assets" / "ManWoman.png"
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Could not read {image_path}")

rng = np.random.default_rng(42)
noise_pattern = rng.standard_normal(image.shape)


def add_gaussian_noise(image, sigma):
    # Add signed noise before converting to uint8 to avoid wraparound.
    noisy = image.astype(np.float64) + sigma * noise_pattern
    return np.clip(np.rint(noisy), 0, 255).astype(np.uint8)


# Q10.1: compare the filters at the supplied noise levels.
median_result = cv2.medianBlur(add_gaussian_noise(image, 18.75), 3)
bilateral_result = cv2.bilateralFilter(add_gaussian_noise(image, 27.0), 9, 75, 75)
median_psnr = cv2.PSNR(image, median_result)
bilateral_psnr = cv2.PSNR(image, bilateral_result)
print(f"Median, sigma 18.75: {median_psnr:.4f} dB")
print(f"Bilateral, sigma 27.00: {bilateral_psnr:.4f} dB")
print(f"Filtered-output PSNR difference: {abs(median_psnr - bilateral_psnr):.4f} dB")

# Q10.2: use the same noisy image for both filters in each comparison.
noisy_gaussian = add_gaussian_noise(image, 25)
sp_rng = np.random.default_rng(123)
noisy_sp = image.copy()
pepper = sp_rng.random(image.shape[:2]) < 0.02
noisy_sp[pepper] = [0, 0, 0]
salt = sp_rng.random(image.shape[:2]) < 0.02
noisy_sp[salt] = [255, 255, 255]

fig, axes = plt.subplots(2, 3, figsize=(9, 5.2), layout="constrained")
for row, (noise_name, noisy) in enumerate([
        ("Gaussian noise (sigma = 25)", noisy_gaussian),
        ("Salt-and-pepper noise", noisy_sp)]):
    mean_result = cv2.blur(noisy, (3, 3))
    median_result = cv2.medianBlur(noisy, 3)
    pictures = [noisy, mean_result, median_result]
    psnr = [cv2.PSNR(image, picture) for picture in pictures]
    print(f"{noise_name}: before {psnr[0]:.2f}, mean {psnr[1]:.2f}, median {psnr[2]:.2f} dB")

    titles = [noise_name, "Mean filter", "Median filter"]
    for ax, picture, title, value in zip(axes[row], pictures, titles, psnr):
        ax.imshow(cv2.cvtColor(picture, cv2.COLOR_BGR2RGB))
        ax.set_title(f"{title}\n{value:.2f} dB")
        ax.axis("off")

figure_path = lab_folder / "figures" / "section10_noise_comparison.png"
fig.savefig(figure_path, dpi=180)
print(f"Saved {figure_path.name}")
