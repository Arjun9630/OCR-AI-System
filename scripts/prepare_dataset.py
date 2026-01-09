import sys
from pathlib import Path
import os

# Add project root to PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.ocr.ocr_engine import ocr_image, ocr_pdf
from src.ml.extract_invoice_fields import extract_invoice_fields, save_to_json


BASE_DIR = "test_documents"


def process_file(file_path: Path):
    print(f"Processing: {file_path}")

    # OCR
    if file_path.suffix.lower() in [".png", ".jpg", ".jpeg"]:
        text = ocr_image(str(file_path))

    elif file_path.suffix.lower() == ".pdf":
        text = ocr_pdf(str(file_path))

    else:
        return

    # Save OCR text
    txt_path = file_path.with_suffix(".txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Saved OCR text: {txt_path}")

    # Extract structured data ONLY for invoices
    if "invoice" in file_path.parent.name.lower():
        data = extract_invoice_fields(text)
        json_path = file_path.with_suffix(".json")
        save_to_json(data, str(json_path))
        print(f"Saved extracted JSON: {json_path}")


def main():
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith((".png", ".jpg", ".jpeg", ".pdf")):
                process_file(Path(root) / file)


if __name__ == "__main__":
    main()
