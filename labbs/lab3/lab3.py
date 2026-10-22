"""DT081A Lab 3: Sections 1 and 2 only."""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


def apply_gama(image, gamma):
    # Use the lab's exponent gamma on intensities between 0 and 1.
    image_float = image.astype(np.float32) / 255.0
    corrected_image = 255.0 * np.power(image_float, gamma)
    return np.uint8(corrected_image)


folder = Path(__file__).resolve().parent
image_path = (folder.parent / "DT081A_Labs-main" / "DT081A_Labs-main"
              / "images" / "peppers.tiff")
image = cv2.imread(str(image_path))
if image is None:
    raise FileNotFoundError(f"Test image not found: {image_path}")

figure_folder = folder / "figures"
figure_folder.mkdir(exist_ok=True)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width = image.shape[:2]
print("Image:", image_path)
print(f"Size: {width} x {height} pixels")

# Section 1.1: test the three intensities with gamma = 2.0.
input_values = np.array([64, 128, 192], dtype=np.uint8)
output_values = apply_gama(input_values, 2.0)
print("\nGamma = 2.0")
print("Input | Output (uint8)")
for i in range(len(input_values)):
    print(f"{input_values[i]:5d} | {output_values[i]:5d}")

# Section 1.2: use grayscale so each pixel has one intensity value.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
corrected = apply_gama(gray, 2.2)
hist_original, edges = np.histogram(gray, bins=256, range=(0, 256))
hist_corrected, edges = np.histogram(corrected, bins=256, range=(0, 256))
print(f"\nMean grayscale intensity: {gray.mean():.2f} -> {corrected.mean():.2f}")

images = [gray, corrected]
histograms = [hist_original, hist_corrected]
titles = ["Original grayscale", "Gamma = 2.2"]
histogram_max = max(hist_original.max(), hist_corrected.max())
plt.figure(figsize=(10, 8))
for i in range(2):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap="gray", vmin=0, vmax=255)
    plt.title(titles[i])
    plt.axis("off")

    plt.subplot(2, 2, i + 3)
    plt.bar(np.arange(256), histograms[i], width=1, color="gray")
    plt.xlim(0, 255)
    plt.ylim(0, histogram_max * 1.05)
    plt.title(titles[i] + " histogram")
    plt.xlabel("Intensity (0-255)")
    plt.ylabel("Pixel count")
plt.tight_layout()
plt.savefig(figure_folder / "section1_gamma_histograms.png", dpi=150)

# Section 2.1: OpenCV reads BGR and stores YCrCb in the order Y, Cr, Cb.
r, g, b = cv2.split(image_rgb)
ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(ycrcb)
channels = [y, r, g, b]
channel_names = ["Y (brightness)", "R (red)", "G (green)", "B (blue)"]
colours = ["black", "red", "green", "blue"]
print("\nChannel | Minimum | Maximum | Standard deviation")
plt.figure(figsize=(11, 7))
for i in range(len(channels)):
    channel = channels[i]
    counts, edges = np.histogram(channel, bins=256, range=(0, 256))
    print(f"{channel_names[i]:14s} | {channel.min():7d} | {channel.max():7d} | {channel.std():.2f}")
    plt.subplot(2, 2, i + 1)
    plt.bar(np.arange(256), counts, width=1, color=colours[i])
    plt.xlim(0, 255)
    plt.title(channel_names[i])
    plt.xlabel("Intensity (0-255)")
    plt.ylabel("Pixel count")
plt.tight_layout()
plt.savefig(figure_folder / "section2_channel_histograms.png", dpi=150)

# Section 2.2: reduce both dimensions of Cb and Cr, keeping Y unchanged.
factors = [1, 2, 4, 8]
original_samples = image.size
crop_top = height // 4
crop_left = width // 4
crop_height = height // 4
crop_width = width // 4
print("\nFactor | Chroma width x height | Stored channel samples | Saving (%)")
plt.figure(figsize=(14, 7))
for i in range(len(factors)):
    factor = factors[i]
    if factor == 1:
        cb_small = cb
        cr_small = cr
        reconstructed = image_rgb
        title = "Original"
    else:
        small_size = (width // factor, height // factor)
        cb_small = cv2.resize(cb, small_size, interpolation=cv2.INTER_AREA)
        cr_small = cv2.resize(cr, small_size, interpolation=cv2.INTER_AREA)
        # Restore their size to display the colours together with the original Y.
        cb_full = cv2.resize(cb_small, (width, height), interpolation=cv2.INTER_LINEAR)
        cr_full = cv2.resize(cr_small, (width, height), interpolation=cv2.INTER_LINEAR)
        reconstructed_ycrcb = cv2.merge([y, cr_full, cb_full])
        reconstructed = cv2.cvtColor(reconstructed_ycrcb, cv2.COLOR_YCrCb2RGB)
        title = f"Factor {factor}"

    # Count the stored channels before resizing back for display.
    stored_samples = y.size + cb_small.size + cr_small.size
    saving = 100 * (1 - stored_samples / original_samples)
    print(f"{factor:6d} | {cb_small.shape[1]:5d} x {cb_small.shape[0]:5d}      | {stored_samples:22d} | {saving:10.3f}")

    plt.subplot(2, 4, i + 1)
    plt.imshow(reconstructed, interpolation="nearest")
    plt.title(title)
    plt.axis("off")
    # Enlarge the same small region to make colour changes easier to compare.
    crop = reconstructed[crop_top:crop_top + crop_height,
                         crop_left:crop_left + crop_width]
    plt.subplot(2, 4, i + 5)
    plt.imshow(crop, interpolation="nearest")
    plt.title(title + ": same crop")
    plt.axis("off")
plt.suptitle("Chroma subsampling: Y unchanged; full images above, enlarged crops below")
plt.tight_layout()
plt.savefig(figure_folder / "section2_chroma_subsampling.png", dpi=150)

print("\nThree figures saved in:", figure_folder)
plt.show()
