import pytesseract
import os
from pdf2image import convert_from_path
from PIL import Image
from src.preprocessing.preprocess import preprocess_image

# Explicit Tesseract path (Windows-safe)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def ocr_image(image_path: str) -> str:
    processed_img = preprocess_image(image_path)

    custom_config = r'--oem 3 --psm 4 -c preserve_interword_spaces=1'
    text = pytesseract.image_to_string(
        processed_img,
        lang="eng",
        config=custom_config
    )
    return text

def ocr_pdf(pdf_path: str, temp_dir: str = "temp_pages") -> str:
    """
    Perform OCR on a PDF document by converting pages to images.
    """
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    pages = convert_from_path(pdf_path, dpi=300)
    full_text = ""

    for idx, page in enumerate(pages):
        img_path = os.path.join(temp_dir, f"page_{idx+1}.png")
        page.save(img_path, "PNG")

        page_text = ocr_image(img_path)
        full_text += f"\n--- Page {idx+1} ---\n{page_text}"

    return full_text


if __name__ == "__main__":
    test_image = "sample_invoice.png"
    if os.path.exists(test_image):
        print("\nOCR OUTPUT:\n")
        print(ocr_image(test_image))
