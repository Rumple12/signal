"""Lab 1, Section 2.3: Gaussian noise and PSNR."""

from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter


# Load the same grayscale Lenna image as in Sections 2.1 and 2.2.
def load_image(url):
    request = Request(url, headers={"User-Agent": "DT081A-Lab1/1.0"})
    with urlopen(request, timeout=30) as response:
        return np.array(Image.open(BytesIO(response.read())).convert("L"))


# Calculate pixel errors using floats so uint8 values do not wrap around.
def calculate_psnr(original, processed):
    error = original.astype(float) - processed.astype(float)
    mse = np.mean(error**2)
    if mse == 0:
        return float("inf")
    return 10 * np.log10(255**2 / mse)


# A fixed seed gives the same noise when the script is run again.
rng = np.random.default_rng(31415)


def add_noise(image, std_dev):
    noise = rng.normal(0, std_dev, image.shape)
    return np.clip(image.astype(float) + noise, 0, 255).astype(np.uint8)


image_url = "https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png"
original = load_image(image_url)

# Test the teacher's 20 noise levels from 0 to 50.
noise_levels = np.linspace(0, 50, 20)
psnr_values = []
for std_dev in noise_levels:
    noisy = add_noise(original, std_dev)
    psnr = calculate_psnr(original, noisy)
    psnr_values.append(psnr)
    print(f"Noise sigma = {std_dev:.4f}: PSNR = {psnr:.4f} dB")

# Keep these images for the separate visual comparison.
visual_levels = [5, 20, 50, 150, 500]
visual_images = []
visual_psnr = []
for std_dev in visual_levels:
    noisy = add_noise(original, std_dev)
    psnr = calculate_psnr(original, noisy)
    visual_images.append(noisy)
    visual_psnr.append(psnr)
    print(f"Visual comparison sigma = {std_dev}: PSNR = {psnr:.4f} dB")

# Filter one noisy image, using floats to keep the filtering accurate.
noisy_25 = add_noise(original, 25)
filtered = gaussian_filter(noisy_25.astype(float), sigma=1)
noisy_psnr = calculate_psnr(original, noisy_25)
filtered_psnr = calculate_psnr(original, filtered)
print(f"Before filtering, noise sigma = 25: PSNR = {noisy_psnr:.4f} dB")
print(f"After Gaussian filtering, spatial sigma = 1: PSNR = {filtered_psnr:.4f} dB")

figure_folder = Path(__file__).resolve().parent.parent / "figures"
figure_folder.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "lines.linewidth": 1.5})

# Figure 14: the unchanged image has infinite PSNR, so omit that point.
finite = np.isfinite(psnr_values)
plt.figure(figsize=(8, 4))
plt.plot(noise_levels[finite], np.array(psnr_values)[finite],
         "o-", color="#526d82")
plt.title("Noise and PSNR")
plt.xlabel("Noise standard deviation (gray levels)")
plt.ylabel("PSNR (dB)")
plt.xlim(0, 50)
plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(figure_folder / "section2_3_noise_psnr.png", dpi=180)

# Figure 15: use the same gray scale for all six panels.
plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1)
plt.imshow(original, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
plt.title("Original")
plt.axis("off")
for panel, (std_dev, noisy, psnr) in enumerate(
        zip(visual_levels, visual_images, visual_psnr), start=2):
    plt.subplot(2, 3, panel)
    plt.imshow(noisy, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
    plt.title(f"Noise sigma = {std_dev}\nPSNR = {psnr:.4f} dB")
    plt.axis("off")
plt.tight_layout()
plt.savefig(figure_folder / "section2_3_increasing_noise.png", dpi=180)

# Figure 16: compare the same noisy input before and after filtering.
plt.figure(figsize=(12, 4))
titles = ["Original", f"Noise sigma = 25\nPSNR = {noisy_psnr:.4f} dB",
          f"Gaussian filter, spatial sigma = 1\nPSNR = {filtered_psnr:.4f} dB"]
for panel, (image, title) in enumerate(
        zip([original, noisy_25, filtered], titles), start=1):
    plt.subplot(1, 3, panel)
    plt.imshow(image, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
    plt.title(title)
    plt.axis("off")
plt.tight_layout()
plt.savefig(figure_folder / "section2_3_noise_reduction.png", dpi=180)
print("Figures 14, 15 and 16 saved in", figure_folder)
plt.show()
