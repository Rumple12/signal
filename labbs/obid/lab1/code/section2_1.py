"""Lab 1, Section 2.1: image sampling and quantization."""

from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# Load the teacher's image. urllib avoids an extra requests dependency.
def load_image(url):
    request = Request(url, headers={"User-Agent": "DT081A-Lab1/1.0"})
    with urlopen(request, timeout=30) as response:
        return np.array(Image.open(BytesIO(response.read())).convert("L"))


# Teacher's simple method: keep every factor-th pixel, then repeat it.
def resample_image(image, factor):
    small = image[::factor, ::factor]
    return np.repeat(np.repeat(small, factor, axis=0), factor, axis=1)


# Teacher's requantization method: group intensities into fewer levels.
def requantize_image(image, bpp):
    levels = 2**bpp
    return np.floor(image / (256/levels)) * (256/levels)


# Apply spatial reduction first, then reduce the gray levels.
def combine_methods(image, factor, bpp):
    return requantize_image(resample_image(image, factor), bpp)


# Reduce and restore the image dimensions using bicubic interpolation.
def bicubic_resample(image, factor):
    height, width = image.shape
    small = Image.fromarray(image).resize(
        (width // factor, height // factor), Image.Resampling.BICUBIC)
    return np.array(small.resize((width, height), Image.Resampling.BICUBIC))


image_url = "https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png"
portrait_image = load_image(image_url)
labbs_folder = Path(__file__).resolve().parents[3]
texture_path = (labbs_folder / "DT081A_Labs-main" / "DT081A_Labs-main"
                / "images" / "grass_texture.tiff")
texture_image = np.array(Image.open(texture_path).convert("L"))

# Calculate the requested factors and bit depths for both image types.
resampling_factors = [2, 4, 8]
bit_depths = [6, 4, 2]
portrait_resampled = {}
texture_resampled = {}
portrait_requantized = {}
texture_requantized = {}
for factor in resampling_factors:
    portrait_resampled[factor] = resample_image(portrait_image, factor)
    texture_resampled[factor] = resample_image(texture_image, factor)
for bpp in bit_depths:
    portrait_requantized[bpp] = requantize_image(portrait_image, bpp)
    texture_requantized[bpp] = requantize_image(texture_image, bpp)

combined_settings = [(2, 6), (2, 4), (4, 4), (4, 2)]
combined_images = []
for factor, bpp in combined_settings:
    combined_images.append(combine_methods(portrait_image, factor, bpp))
texture_combined = combine_methods(texture_image, 4, 4)
bicubic_image = bicubic_resample(portrait_image, 4)

figure_folder = Path(__file__).resolve().parent.parent / "figures"
figure_folder.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "lines.linewidth": 1.5})

# Figure 9: all panels use the same grayscale range.
plt.figure(figsize=(10, 3.8))
images = [portrait_image, portrait_resampled[4], portrait_requantized[4]]
titles = ["Original Lenna", "Simple resampling: factor 4", "Requantization: 4 bpp"]
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap="gray", vmin=0, vmax=255, interpolation="nearest")
    plt.title(titles[i])
    plt.axis("off")
plt.tight_layout()
plt.savefig(figure_folder / "section2_1_basic_comparison.png", dpi=180)

# Figure 10: the four requested combinations on Lenna.
plt.figure(figsize=(8, 7.2))
for i, (factor, bpp) in enumerate(combined_settings):
    plt.subplot(2, 2, i + 1)
    plt.imshow(combined_images[i], cmap="gray", vmin=0, vmax=255,
               interpolation="nearest")
    plt.title(f"Factor {factor}, {bpp} bpp")
    plt.axis("off")
plt.tight_layout()
plt.savefig(figure_folder / "section2_1_combined_settings.png", dpi=180)

# Figure 11: compare the same processing on a portrait and a texture.
plt.figure(figsize=(8, 7.2))
images = [portrait_image, combined_images[2], texture_image, texture_combined]
titles = ["Portrait: original", "Portrait: factor 4, 4 bpp",
          "Grass texture: original", "Grass texture: factor 4, 4 bpp"]
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap="gray", vmin=0, vmax=255, interpolation="nearest")
    plt.title(titles[i])
    plt.axis("off")
plt.tight_layout()
plt.savefig(figure_folder / "section2_1_image_types.png", dpi=180)

# Figure 12: both methods reduce each dimension by four, then restore it.
plt.figure(figsize=(8, 4))
images = [portrait_resampled[4], bicubic_image]
titles = ["Simple resampling: factor 4", "Bicubic resampling: factor 4"]
for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(images[i], cmap="gray", vmin=0, vmax=255, interpolation="nearest")
    plt.title(titles[i])
    plt.axis("off")
plt.tight_layout()
plt.savefig(figure_folder / "section2_1_bicubic_comparison.png", dpi=180)

print("Grayscale Lenna dimensions:", portrait_image.shape)
print("Grayscale grass texture dimensions:", texture_image.shape)
print("Resampling factors:", resampling_factors)
print("Bits per pixel:", bit_depths)
print("Combined settings:", combined_settings)
print("Four Section 2.1 figures saved in", figure_folder)
plt.show()
