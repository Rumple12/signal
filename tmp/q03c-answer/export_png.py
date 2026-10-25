from pathlib import Path
import math
import pypdfium2 as pdfium
from pypdf import PdfReader
from PIL import Image, ImageChops

WORK = Path(__file__).resolve().parent
ROOT = WORK.parent.parent
OUTPUT = ROOT / "Q03c_answer_384.png"

document = pdfium.PdfDocument(WORK / "main.pdf")
assert len(document) == 1
page = document[0]
width, height = page.get_size()
scale = 384 / width
target_height = round(height * scale)
bitmap = page.render(scale=scale * 3)
image = bitmap.to_pil().convert("RGB")
image = image.resize((384, target_height), Image.Resampling.LANCZOS)
image.save(OUTPUT)

# Confirm the complete text stays inside the page, rather than merely trusting
# the absence of overfull-box warnings in TeX.
textpage = page.get_textpage()
for index in range(textpage.count_rects()):
    left, bottom, right, top = textpage.get_rect(index)
    assert left >= 0 and bottom >= 0 and right <= width and top <= height

reader = PdfReader(WORK / "main.pdf")
text = reader.pages[0].extract_text()
for phrase in ["Question 3(c)", "We are given", "Step 1:", "Step 2:",
               "Step 3:", "Step 4:", "Key values:", "Sketch", "Final answer:",
               "the numerator does not affect the magnitude", "and the sketch has:"]:
    assert phrase in text, phrase
images = list(reader.pages[0].images)
assert len(images) == 1
assert images[0].image.size == (384, 300)

with Image.open(OUTPUT) as result:
    assert result.width == 384
    assert result.mode == "RGB"
    background = Image.new("RGB", result.size, "white")
    bounds = ImageChops.difference(result, background).getbbox()
    assert bounds[0] >= 2 and bounds[1] >= 2
    assert bounds[2] <= result.width-2 and bounds[3] <= result.height-2
    # Actual-size sections for visual quality checks; these are intermediate.
    for index, top in enumerate(range(0, result.height, 760), start=1):
        result.crop((0, top, 384, min(top+760, result.height))).save(
            WORK / f"check-{index}.png")

print(f"Saved: {OUTPUT}")
print(f"Dimensions: 384 x {target_height} pixels")
print(f"Included plotted sketch: {images[0].image.size[0]} x {images[0].image.size[1]} source pixels")
print(f"Non-white content bounds: {bounds}")
print("Verified: all text is within the page; all four steps and final answer are present.")
