"""Lab 1, Section 2: image sampling, quality measurements, and noise."""

from pathlib import Path
from time import perf_counter

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import requests
from scipy.ndimage import gaussian_filter
from skimage.metrics import structural_similarity

folder = Path(__file__).resolve().parent
figures = folder / "figures"
figures.mkdir(exist_ok=True)
data_folder = folder / "data"
data_folder.mkdir(exist_ok=True)

# Download the teacher's image once. Downloaded inputs are ignored by Git.
image_path = data_folder / "lenna.png"
if not image_path.exists():
    url = "https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png"
    response = requests.get(url, headers={"User-Agent": "DT081A-Lab1/1.0"}, timeout=30)
    response.raise_for_status()
    image_path.write_bytes(response.content)
original = np.array(Image.open(image_path).convert("L"))


# These two operations follow the teacher's examples.
def resample(image, factor):
    small = image[::factor, ::factor]
    return np.repeat(np.repeat(small, factor, axis=0), factor, axis=1)


def requantize(image, bits):
    step = 256 / 2**bits
    return np.floor(image / step) * step


def combine_operations(image, factor, bits):
    return requantize(resample(image, factor), bits)


def bicubic(image, factor):
    height, width = image.shape
    small = Image.fromarray(image).resize((width // factor, height // factor),
                                          Image.Resampling.BICUBIC)
    return np.array(small.resize((width, height), Image.Resampling.BICUBIC))


def psnr(clean, processed):
    # Convert BEFORE subtracting so uint8 arithmetic cannot wrap around.
    error = clean.astype(float) - processed.astype(float)
    mse = np.mean(error**2)
    if mse == 0:
        return float("inf")
    return 10 * np.log10(255**2 / mse)


# Known errors give known PSNR values, including the largest uint8 difference.
zeros = np.zeros((8, 8), dtype=np.uint8)
assert np.isinf(psnr(zeros, zeros))
assert np.isclose(psnr(zeros, np.full_like(zeros, 255)), 0)
assert np.isclose(psnr(zeros, np.full_like(zeros, 10)), 20 * np.log10(25.5))

# 2.1: Several factors, bit depths, and combined settings in one figure.
plt.figure(figsize=(13, 10))
for column, factor in enumerate([1, 2, 4, 8], 1):
    plt.subplot(3, 4, column)
    plt.imshow(resample(original, factor), cmap="gray", vmin=0, vmax=255)
    plt.title(f"Resampling factor {factor}")
    plt.axis("off")
for column, bits in enumerate([8, 6, 4, 2], 1):
    plt.subplot(3, 4, column + 4)
    plt.imshow(requantize(original, bits), cmap="gray", vmin=0, vmax=255)
    plt.title(f"{bits} bpp: {2**bits} possible levels")
    plt.axis("off")
for column, (factor, bits) in enumerate([(2, 6), (2, 4), (4, 6), (4, 4)], 1):
    processed = combine_operations(original, factor, bits)
    ratio = 8 * factor**2 / bits
    plt.subplot(3, 4, column + 8)
    plt.imshow(processed, cmap="gray", vmin=0, vmax=255)
    plt.title(f"Factor {factor}, {bits} bpp\nIdeal reduction {ratio:.2f}x")
    plt.axis("off")
    print(f"Combined: factor={factor}, bpp={bits}, ideal ratio={ratio:.4f}x, "
          f"PSNR={psnr(original, processed):.4f} dB")
plt.tight_layout()
plt.savefig(figures / "image_sampling_quantization.png", dpi=150)
plt.close()

# Bicubic and simple results both reconstruct to the original dimensions.
start = perf_counter()
simple = resample(original, 4)
simple_time = perf_counter() - start
start = perf_counter()
cubic = bicubic(original, 4)
cubic_time = perf_counter() - start
assert simple.shape == cubic.shape == original.shape
print(f"Same-size comparison: {simple.shape}; single-run times "
      f"simple={simple_time*1000:.3f} ms, bicubic={cubic_time*1000:.3f} ms")
print(f"Bicubic factor 4: PSNR={psnr(original, cubic):.4f} dB")

asset_folder = folder.parent / "DT081A_Labs-main" / "DT081A_Labs-main" / "images"
image_names = ["male_portrait.tiff", "grass_texture.tiff",
               "sandiego_aerial.tiff", "peppers.tiff"]
plt.figure(figsize=(12, 12))
for row, name in enumerate(image_names):
    image = np.array(Image.open(asset_folder / name).convert("L"))
    views = [image, resample(image, 4), bicubic(image, 4), requantize(image, 4)]
    assert views[0].shape == views[1].shape == views[2].shape
    for column, (view, title) in enumerate(zip(views, ["Original", "Simple, factor 4",
                                                     "Bicubic, factor 4", "4 bpp"])):
        plt.subplot(4, 4, 4 * row + column + 1)
        plt.imshow(view, cmap="gray", vmin=0, vmax=255)
        plt.title(f"{name.replace('.tiff', '').replace('_', ' ')}\n{title}", fontsize=9)
        plt.axis("off")
    print("Image type:", name, image.shape)
plt.tight_layout()
plt.savefig(figures / "image_types_bicubic.png", dpi=150)
plt.close()

# 2.2: Compare the same clean image against both processing results.
requantized = requantize(original, 4)
for name, image in [("Resampled factor 4", simple), ("Requantized 4 bpp", requantized)]:
    score = structural_similarity(original, image, data_range=255)
    print(f"{name}: PSNR={psnr(original, image):.6f} dB, SSIM={score:.6f}")

bits_values = list(range(1, 9))
plt.figure(figsize=(11, 4))
for factor in [1, 2, 4, 8]:
    psnr_values = []
    ssim_values = []
    for bits in bits_values:
        image = combine_operations(original, factor, bits)
        p = psnr(original, image)
        s = structural_similarity(original, image, data_range=255)
        psnr_values.append(p)
        ssim_values.append(s)
        print(f"Metrics: factor={factor}, bpp={bits}, PSNR={p:.6f}, SSIM={s:.6f}")
    plt.subplot(1, 2, 1)
    plt.plot(bits_values, psnr_values, "o-", label=f"Factor {factor}")
    plt.subplot(1, 2, 2)
    plt.plot(bits_values, ssim_values, "o-", label=f"Factor {factor}")
for position, label in [(1, "PSNR (dB)"), (2, "SSIM")]:
    plt.subplot(1, 2, position)
    plt.xlabel("Bits per pixel")
    plt.ylabel(label)
    plt.title(label + " against the original image")
    plt.legend()
    plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(figures / "image_metrics.png", dpi=150)
plt.close()

# 2.3: Keep the random sequence fixed and compare the SAME noisy image.
rng = np.random.default_rng(2026)


def add_noise(image, standard_deviation):
    noise = rng.normal(0, standard_deviation, image.shape)
    return np.clip(image.astype(float) + noise, 0, 255).astype(np.uint8)


noise_images = {}
for deviation in [0, 2, 5, 10, 15, 20, 30, 50, 75, 150, 500]:
    noise_images[deviation] = add_noise(original, deviation)
    print(f"Noise: sd={deviation}, PSNR={psnr(original, noise_images[deviation]):.6f} dB")
blurred = gaussian_filter(noise_images[20].astype(float), sigma=1)
print(f"Denoising sd=20, Gaussian sigma=1: before={psnr(original, noise_images[20]):.6f}, "
      f"after={psnr(original, blurred):.6f} dB")

plt.figure(figsize=(13, 7))
views = [("Original", original), ("Noise sd=5", noise_images[5]),
         ("Noise sd=20", noise_images[20]), ("sd=20, Gaussian sigma=1", blurred),
         ("Noise sd=50", noise_images[50]), ("Noise sd=150", noise_images[150]),
         ("Noise sd=500", noise_images[500])]
for position, (title, image) in enumerate(views, 1):
    plt.subplot(2, 4, position)
    plt.imshow(image, cmap="gray", vmin=0, vmax=255)
    plt.title(f"{title}\nPSNR={psnr(original, image):.2f} dB", fontsize=10)
    plt.axis("off")
plt.subplot(2, 4, 8)
deviations = [2, 5, 10, 15, 20, 30, 50]
plt.plot(deviations, [psnr(original, noise_images[d]) for d in deviations], "o-")
plt.title("Noise strength and PSNR")
plt.xlabel("Added noise standard deviation")
plt.ylabel("PSNR (dB)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(figures / "noise_filtering.png", dpi=150)
plt.close()
print("Image checks passed; four figures saved. SSIM data_range=255; random seed=2026.")
