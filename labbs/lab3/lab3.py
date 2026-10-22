"""DT081A Lab 3: Sections 1-3 only."""

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

# Section 3.1: group each colour channel into 16 possible levels.
step_4bit = 256 // 16
quantized_4bit = image_rgb // step_4bit
# Use the lower value of each range for display, as in the teacher's example.
display_4bit = quantized_4bit * step_4bit
print("\n4-bit quantization: 16 possible levels per colour channel")
for i, name in enumerate(["R", "G", "B"]):
    print(name, "levels used:", len(np.unique(quantized_4bit[:, :, i])))

original_bits = image_rgb.size * 8
quantized_bits = image_rgb.size * 4
compression_ratio = original_bits / quantized_bits
storage_saving = 100 * (1 - quantized_bits / original_bits)
print(f"Theoretical compression ratio: {compression_ratio:.0f}:1")
print(f"Theoretical storage saving: {storage_saving:.0f}%")
print("Theoretical packed 4-bit storage:", quantized_bits // 8, "bytes")
print("Actual original uint8 array:", image_rgb.nbytes, "bytes")
print("Actual quantized uint8 array:", quantized_4bit.nbytes, "bytes")

plt.figure(figsize=(11, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original: 8 bits per channel")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(display_4bit)
plt.title("4 bits per channel: 16 possible levels")
plt.axis("off")
plt.tight_layout()
plt.savefig(figure_folder / "section3_4bit_quantization.png", dpi=150)

# Section 3.2: reuse the original grayscale image, before gamma correction.
step_3bit = 256 // 8
quantized_3bit = gray // step_3bit
display_3bit = quantized_3bit * step_3bit
hist_3bit, edges_3bit = np.histogram(quantized_3bit, bins=8, range=(0, 8))
print("\n3-bit grayscale levels used:", np.unique(quantized_3bit))
print("Displayed grayscale intensities:", np.unique(display_3bit))
print("Pixel counts at levels 0-7:", hist_3bit)
print("Original histogram pixel count:", hist_original.sum())
print("3-bit histogram pixel count:", hist_3bit.sum())

plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.imshow(gray, cmap="gray", vmin=0, vmax=255)
plt.title("Original grayscale: 8 bits")
plt.axis("off")
plt.subplot(2, 2, 2)
plt.imshow(display_3bit, cmap="gray", vmin=0, vmax=255)
plt.title("3-bit grayscale: 8 possible levels")
plt.axis("off")
plt.subplot(2, 2, 3)
plt.bar(np.arange(256), hist_original, width=1, color="gray")
plt.xlim(0, 255)
plt.title("Original intensity histogram")
plt.xlabel("Intensity (0-255)")
plt.ylabel("Pixel count")
plt.subplot(2, 2, 4)
plt.bar(np.arange(8), hist_3bit, color="gray")
plt.xticks(np.arange(8))
plt.xlim(-0.5, 7.5)
plt.title("3-bit level histogram")
plt.xlabel("Quantized level (0-7)")
plt.ylabel("Pixel count")
plt.tight_layout()
plt.savefig(figure_folder / "section3_3bit_histograms.png", dpi=150)

print("\nFive figures saved in:", figure_folder)
plt.show()
