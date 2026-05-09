"""
Converts headshot.pdf (first page) → me.png:
  - Renders PDF at high resolution
  - Removes background (rembg)
  - Resizes to 400x400 with transparent padding to keep aspect ratio

Dependencies:
    pip install pymupdf rembg pillow
    (rembg will download its model ~170MB on first run)
"""

import sys
from pathlib import Path

try:
    import fitz  # pymupdf
    from rembg import remove
    from PIL import Image
    import io
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Run: pip install pymupdf rembg pillow")
    sys.exit(1)

INPUT_PDF = Path(__file__).parent / "headshot.pdf"
OUTPUT_PNG = Path(__file__).parent / "me.png"
TARGET_SIZE = 1600   # output image dimensions in pixels (increase for a larger file)
PADDING = -10        # transparent pixels to leave around the subject on each side


def pdf_first_page_to_image(pdf_path: Path, dpi: int = 300) -> Image.Image:
    doc = fitz.open(str(pdf_path))
    page = doc[0]
    zoom = dpi / 72  # 72 is the default PDF DPI
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    img_bytes = pix.tobytes("png")
    return Image.open(io.BytesIO(img_bytes)).convert("RGBA")


def remove_background(img: Image.Image) -> Image.Image:
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    result_bytes = remove(buf.getvalue())
    return Image.open(io.BytesIO(result_bytes)).convert("RGBA")


def resize_to_square(img: Image.Image, size: int) -> Image.Image:
    # Crop tight to the non-transparent subject so small subjects fill the frame
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)

    # Scale to fill (size - 2*PADDING)×(size - 2*PADDING), preserving aspect ratio
    inner = size - 2 * PADDING
    scale = inner / max(img.width, img.height)
    new_w = int(img.width * scale)
    new_h = int(img.height * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)

    # Center on a transparent square canvas
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    offset = ((size - img.width) // 2, (size - img.height) // 2)
    canvas.paste(img, offset, mask=img)
    return canvas


def main():
    print(f"Reading {INPUT_PDF} ...")
    img = pdf_first_page_to_image(INPUT_PDF)

    print("Removing background (first run downloads ~170MB model) ...")
    img = remove_background(img)

    print(f"Resizing to {TARGET_SIZE}×{TARGET_SIZE} ...")
    img = resize_to_square(img, TARGET_SIZE)

    img.save(OUTPUT_PNG, "PNG")
    print(f"Saved → {OUTPUT_PNG}")


if __name__ == "__main__":
    main()
