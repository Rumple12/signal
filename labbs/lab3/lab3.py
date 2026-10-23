"""DT081A Lab 3: Sections 1-8 only."""

import time
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

# Section 4.1: compare equivalent 2D and separable Gaussian filters.
kernel_sizes = [5, 11, 21]
sigma = 1.0
repeats = 30
times_2d = []
times_separable = []
gaussian_differences = []
print("\nGaussian filtering: average of", repeats, "runs, sigma =", sigma)
print("Size | Ordinary 2D (ms) | Separable (ms) | Largest output difference")
for kernel_size in kernel_sizes:
    kernel_1d = cv2.getGaussianKernel(kernel_size, sigma)
    kernel_2d = np.outer(kernel_1d, kernel_1d)

    # Run each method once before timing, so its first call is not measured.
    cv2.filter2D(gray, cv2.CV_64F, kernel_2d, borderType=cv2.BORDER_REFLECT_101)
    cv2.sepFilter2D(gray, cv2.CV_64F, kernel_1d, kernel_1d,
                    borderType=cv2.BORDER_REFLECT_101)
    start = time.time()
    for repeat in range(repeats):
        gaussian_2d = cv2.filter2D(gray, cv2.CV_64F, kernel_2d,
                                   borderType=cv2.BORDER_REFLECT_101)
    time_2d = 1000 * (time.time() - start) / repeats

    start = time.time()
    for repeat in range(repeats):
        gaussian_separable = cv2.sepFilter2D(gray, cv2.CV_64F, kernel_1d, kernel_1d,
                                             borderType=cv2.BORDER_REFLECT_101)
    time_separable = 1000 * (time.time() - start) / repeats
    max_difference = np.max(np.abs(gaussian_2d - gaussian_separable))
    times_2d.append(time_2d)
    times_separable.append(time_separable)
    gaussian_differences.append(max_difference)
    print(f"{kernel_size:4d} | {time_2d:16.3f} | {time_separable:14.3f} | {max_difference:.3e}")

    # Save the teacher's 5 x 5 example for the image comparison.
    if kernel_size == 5:
        gaussian_2d_example = gaussian_2d
        gaussian_separable_example = gaussian_separable

plt.figure(figsize=(12, 4.5))
gaussian_images = [gray, gaussian_2d_example, gaussian_separable_example]
gaussian_titles = ["Original grayscale", "Ordinary 2D: 5 x 5, sigma = 1",
                   "Separable: 5 x 5, sigma = 1"]
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(gaussian_images[i], cmap="gray", vmin=0, vmax=255)
    plt.title(gaussian_titles[i])
    plt.axis("off")
plt.tight_layout()
plt.savefig(figure_folder / "section4_gaussian_comparison.png", dpi=150)

# Section 4.2: horizontal edges come from brightness changes along y.
def detect_horizontal_edges(image):
    return cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3,
                     borderType=cv2.BORDER_REFLECT_101)


sobel_y = detect_horizontal_edges(gray)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3,
                    borderType=cv2.BORDER_REFLECT_101)
horizontal_strength = np.abs(sobel_y)
vertical_strength = np.abs(sobel_x)
edge_max = max(horizontal_strength.max(), vertical_strength.max())

plt.figure(figsize=(12, 4.5))
plt.subplot(1, 3, 1)
plt.imshow(gray, cmap="gray", vmin=0, vmax=255)
plt.title("Original grayscale")
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(horizontal_strength, cmap="gray", vmin=0, vmax=edge_max)
plt.title("Horizontal edges: absolute Sobel y")
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(vertical_strength, cmap="gray", vmin=0, vmax=edge_max)
plt.title("Vertical edges: absolute Sobel x")
plt.axis("off")
plt.tight_layout()
plt.savefig(figure_folder / "section4_sobel_edges.png", dpi=150)

# Section 4.3: combine both signed derivatives before normalizing for display.
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
magnitude_display = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap="gray", vmin=0, vmax=255)
plt.title("Original grayscale")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(magnitude_display, cmap="gray", vmin=0, vmax=255)
plt.title("Sobel gradient magnitude")
plt.axis("off")
plt.tight_layout()
plt.savefig(figure_folder / "section4_gradient_magnitude.png", dpi=150)

# Section 5.1: apply the same brightness and contrast formula in two ways.
brightness = 20
contrast = 1.2
adjustment_repeats = 5

start = time.time()
for repeat in range(adjustment_repeats):
    # Stack pixels into a column and use floats to avoid uint8 overflow.
    img_vector = gray.reshape(-1, 1).astype(np.float64)
    adjusted_vector = contrast * (img_vector - 128) + 128 + brightness
    adjusted_vector = np.clip(adjusted_vector, 0, 255).astype(np.uint8)
    adjusted_numpy = adjusted_vector.reshape(gray.shape)
time_vector = 1000 * (time.time() - start) / adjustment_repeats

start = time.time()
for repeat in range(adjustment_repeats):
    adjusted_loop = np.empty_like(gray)
    for row in range(height):
        for column in range(width):
            value = contrast * (float(gray[row, column]) - 128) + 128 + brightness
            value = max(0, min(255, value))
            adjusted_loop[row, column] = int(value)
time_loop = 1000 * (time.time() - start) / adjustment_repeats

speedup = time_loop / time_vector
images_equal = np.array_equal(adjusted_numpy, adjusted_loop)
print("\nBrightness +20, contrast 1.2 around 128: average of", adjustment_repeats, "runs")
print(f"NumPy vectorized: {time_vector:.3f} ms")
print(f"Nested Python loops: {time_loop:.3f} ms")
print(f"Loop time / NumPy time: {speedup:.2f}")
print("Identical adjusted images:", images_equal)
print("Adjusted intensity range:", adjusted_numpy.min(), "to", adjusted_numpy.max())

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap="gray", vmin=0, vmax=255)
plt.title("Original grayscale")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(adjusted_numpy, cmap="gray", vmin=0, vmax=255)
plt.title("Contrast 1.2 around 128; brightness +20")
plt.axis("off")
plt.tight_layout()
plt.savefig(figure_folder / "section5_brightness_contrast.png", dpi=150)

# Section 5.2: calculate storage for H using integers only; do not create H.
N = 512 * 512
matrix_elements = N * N
float32_bytes = matrix_elements * 4
float64_bytes = matrix_elements * 8
float32_gib = float32_bytes / 1024**3
float64_gib = float64_bytes / 1024**3
print(f"\nH dimensions: {N:,} x {N:,}")
print(f"H elements: {matrix_elements:,}")
print(f"Float32 storage: {float32_bytes:,} bytes = {float32_gib:.0f} GiB")
print(f"Float64 storage: {float64_bytes:,} bytes = {float64_gib:.0f} GiB")
print("Only these memory numbers were calculated; H was not allocated.")

# Section 6: use the same log transformation directly and in a lookup table.
def log_middle_contrast(values, strength):
    normalized = values.astype(np.float64) / 255.0
    centered = 2 * normalized - 1
    # log1p(x) means log(1+x). The sign puts each half on its side of the middle.
    log_distance = np.log1p(strength * np.abs(centered)) / np.log1p(strength)
    output = 127.5 * (1 + np.sign(centered) * log_distance)
    return np.clip(output, 0, 255).astype(np.uint8)


# Section 6.1: create the 256-entry table once, then compare per-image times.
log_strength = 4.0
log_input_levels = np.arange(256, dtype=np.uint8)
start = time.time()
lookup_table = log_middle_contrast(log_input_levels, log_strength)
table_build_time = 1000 * (time.time() - start)

# Run each method once before timing its repeated applications.
direct_log = log_middle_contrast(gray, log_strength)
lookup_log = lookup_table[gray]
processing_repeats = 30
start = time.time()
for repeat in range(processing_repeats):
    direct_log = log_middle_contrast(gray, log_strength)
direct_log_time = 1000 * (time.time() - start) / processing_repeats

start = time.time()
for repeat in range(processing_repeats):
    lookup_log = lookup_table[gray]
lookup_log_time = 1000 * (time.time() - start) / processing_repeats
lookup_speedup = direct_log_time / lookup_log_time
log_results_equal = np.array_equal(direct_log, lookup_log)
print("\nLog transformation: average of", processing_repeats, "runs")
print(f"Lookup table creation: {table_build_time:.3f} ms")
print(f"Vectorized direct computation: {direct_log_time:.3f} ms")
print(f"Lookup table application: {lookup_log_time:.3f} ms")
print(f"Direct time / lookup time: {lookup_speedup:.2f}")
print("Identical log results:", log_results_equal)
print("Log output range:", lookup_log.min(), "to", lookup_log.max())

# Section 6.2: show the result and the steeper middle of the transfer curve.
plt.figure(figsize=(13, 4.5))
plt.subplot(1, 3, 1)
plt.imshow(gray, cmap="gray", vmin=0, vmax=255)
plt.title("Original grayscale")
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(lookup_log, cmap="gray", vmin=0, vmax=255)
plt.title("Log transformation: strength = 4")
plt.axis("off")
plt.subplot(1, 3, 3)
plt.plot(log_input_levels, log_input_levels, "--", label="Unchanged intensity")
plt.plot(log_input_levels, lookup_table, label="Log transformation")
plt.xlim(0, 255)
plt.ylim(0, 255)
plt.xlabel("Input intensity")
plt.ylabel("Output intensity")
plt.title("Transfer function")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(figure_folder / "section6_log_transformation.png", dpi=150)

# Section 7.1: form four 16 x 16 images using the teacher's basis vectors.
size = 16
ramp = np.linspace(0, 1, size)
step = np.heaviside(np.arange(size) - size/2, 1)
sine = np.sin(2 * np.pi * np.arange(size) / size)
ramp_ramp = np.outer(ramp, ramp)
step_ramp = np.outer(step, ramp)
step_step = np.outer(step, step)
step_sine = np.outer(step, sine)
elementary_images = [ramp_ramp, step_ramp, step_step, step_sine]
elementary_titles = ["Ramp x Ramp", "Step x Ramp", "Step x Step", "Step x Sine"]

plt.figure(figsize=(9, 8))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    # A shared scale includes negative sine values; zero appears middle gray.
    plt.imshow(elementary_images[i], cmap="gray", vmin=-1, vmax=1,
               interpolation="nearest")
    plt.colorbar(label="Value")
    plt.title(elementary_titles[i])
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.xticks([0, 8, 15])
    plt.yticks([0, 8, 15])
plt.tight_layout()
plt.savefig(figure_folder / "section7_elementary_images.png", dpi=150)

# Section 7.2: approximate a lower, horizontally centred square with three images.
target = np.zeros((size, size))
target[8:16, 4:12] = 1
A = np.column_stack([step_ramp.ravel(), step_step.ravel(), step_sine.ravel()])
target_vector = target.ravel()
weights = np.linalg.lstsq(A, target_vector, rcond=None)[0]
approximation = (weights[0] * step_ramp + weights[1] * step_step
                 + weights[2] * step_sine)
difference = target - approximation
mse = np.mean(difference**2)
print("\nSection 7: three-image square approximation")
print(f"Step x Ramp weight: {weights[0]:.6f}")
print(f"Step x Step weight: {weights[1]:.6f}")
print(f"Step x Sine weight: {weights[2]:.6f}")
print(f"Mean squared error: {mse:.6f}")
print(f"Unclipped approximation range: {approximation.min():.6f} to {approximation.max():.6f}")

# Keep the fit unchanged for the error calculation and for display.
plt.figure(figsize=(12, 4.5))
shape_images = [target, approximation, np.abs(difference)]
shape_titles = ["Target: 8 x 8 white square", "Three-image approximation", "Absolute error"]
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(shape_images[i], cmap="gray", vmin=0, vmax=1,
               interpolation="nearest")
    plt.colorbar(label="Value")
    plt.title(shape_titles[i])
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.xticks([0, 8, 15])
    plt.yticks([0, 8, 15])
plt.tight_layout()
plt.savefig(figure_folder / "section7_shape_approximation.png", dpi=150)

# Section 8.1: transform the original grayscale image using the teacher's FFT example.
f = np.fft.fft2(gray)
fshift = np.fft.fftshift(f)
magnitude = np.log1p(np.abs(fshift))

plt.figure(figsize=(11, 5))
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap="gray", vmin=0, vmax=255)
plt.title("Original grayscale")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(magnitude, cmap="gray")
plt.title("FFT: logarithmic magnitude")
plt.xlabel("Horizontal frequency bin")
plt.ylabel("Vertical frequency bin")
plt.xticks([0, width//2, width-1], [-width//2, 0, width//2-1])
plt.yticks([0, height//2, height-1], [-height//2, 0, height//2-1])
plt.colorbar(label="log(1 + magnitude)")
plt.tight_layout()
plt.savefig(figure_folder / "section8_fft_spectrum.png", dpi=150)

# Section 8.2: keep frequencies inside a circle, following the teacher's mask.
rows, cols = gray.shape
crow, ccol = rows//2, cols//2
cutoff = 40
lowpass_mask = np.zeros((rows, cols))
for i in range(rows):
    for j in range(cols):
        if np.sqrt((i-crow)**2 + (j-ccol)**2) < cutoff:
            lowpass_mask[i, j] = 1

filtered_fft = fshift * lowpass_mask
lowpass_complex = np.fft.ifft2(np.fft.ifftshift(filtered_fft))
lowpass = lowpass_complex.real

# Section 8.3: subtract the smooth image, keeping positive and negative values.
highpass = gray.astype(np.float64) - lowpass
reconstruction_error = np.max(np.abs(gray - (lowpass + highpass)))
print("\nSection 8: frequency filtering")
print("Low-pass cutoff radius:", cutoff, "frequency bins")
print(f"Low-pass range: {lowpass.min():.6f} to {lowpass.max():.6f}")
print(f"High-pass range: {highpass.min():.6f} to {highpass.max():.6f}")
print(f"Maximum imaginary part after inverse FFT: {np.max(np.abs(lowpass_complex.imag)):.3e}")
print(f"Maximum reconstruction error: {reconstruction_error:.3e}")

# Display the signed result around zero without changing the underlying arrays.
highpass_limit = np.max(np.abs(highpass))
filter_images = [gray, lowpass, highpass]
filter_titles = ["Original grayscale", "Low-pass: radius < 40 bins",
                 "High-pass: original - low-pass"]
plt.figure(figsize=(14, 5))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    if i < 2:
        plt.imshow(filter_images[i], cmap="gray", vmin=0, vmax=255)
        plt.colorbar(label="Intensity")
    else:
        plt.imshow(highpass, cmap="gray", vmin=-highpass_limit, vmax=highpass_limit)
        plt.colorbar(label="Signed difference (zero = middle gray)")
    plt.title(filter_titles[i])
    plt.axis("off")
plt.tight_layout()
plt.savefig(figure_folder / "section8_frequency_filtering.png", dpi=150)

print("\nFourteen figures saved in:", figure_folder)
plt.show()
