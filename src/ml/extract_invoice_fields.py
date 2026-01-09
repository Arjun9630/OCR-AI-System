import re
import json
import os
from datetime import datetime


# ---------------- DATE NORMALIZATION ----------------
def normalize_date(raw):
    if not raw:
        return None

    raw = raw.split("\n")[0].strip()

    formats = [
        "%b %d, %Y",
        "%b%d, %Y",
        "%B %d, %Y",
        "%m/%d/%y",
        "%m/%d/%Y",
        "%d/%m/%Y",
        "%d.%m.%Y"
    ]

    for fmt in formats:
        try:
            return datetime.strptime(raw.replace(" ", ""), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue

    return raw


def clean_line(value):
    if not value:
        return None
    return value.split("\n")[0].strip()


# ---------------- MAIN EXTRACTION ----------------
def extract_invoice_fields(ocr_text: str) -> dict:
    data = {}
    text = ocr_text.replace("\r", "")

    # -------- DOCUMENT TYPE --------
    if re.search(r'PROFORMA\s+INVOICE', text, re.IGNORECASE):
        data["document_type"] = "Proforma Invoice"
    elif re.search(r'INVOICE', text, re.IGNORECASE):
        data["document_type"] = "Invoice"

    # -------- INVOICE NUMBER --------
    inv_no = re.search(
        r'Invoice\s*(No\.?|Number|#)\s*[:\-]?\s*([A-Z0-9\-]+)',
        text,
        re.IGNORECASE
    )
    if inv_no:
        data["invoice_number"] = inv_no.group(2)

    # -------- INVOICE DATE (Date OR Invoice Date) --------
    inv_date = re.search(
        r'(Invoice\s*Date|Date)\s*[:\-]?\s*([^\n]+)',
        text,
        re.IGNORECASE
    )
    if inv_date:
        data["invoice_date"] = normalize_date(inv_date.group(2))

    # -------- DUE DATE --------
    due_date = re.search(
        r'Due\s*Date\s*[:\-]?\s*([^\n]+)',
        text,
        re.IGNORECASE
    )
    if due_date:
        data["due_date"] = normalize_date(due_date.group(1))

    # -------- BILL TO --------
    bill_to = re.search(
        r'Bill\s*to\s*[:\-]?\s*([^\n]+)',
        text,
        re.IGNORECASE
    )
    if bill_to:
        data["bill_to"] = clean_line(bill_to.group(1))

    # -------- SUBTOTAL --------
    subtotal = re.search(
        r'Subtotal\s*[:\-]?\s*\$?\s*([\d,]+\.\d{2})',
        text,
        re.IGNORECASE
    )
    if subtotal:
        data["subtotal"] = subtotal.group(1)

    # -------- TAX (AMOUNT ONLY) --------
    tax = re.search(
        r'Tax\s*[:\-]?\s*\$?\s*([\d,]+\.\d{2})',
        text,
        re.IGNORECASE
    )
    if tax:
        data["tax"] = tax.group(1)

    # -------- TOTAL (HIGHEST PRIORITY) --------
    total = re.search(
        r'(Invoice\s*Total|Total|Balance\s*Due)\s*[:\-]?\s*\$?\s*([\d,]+\.\d{2})',
        text,
        re.IGNORECASE
    )
    if total:
        data["total_amount"] = total.group(2)

    return data


# ---------------- SAVE JSON ----------------
def save_to_json(data, output_path="outputs/extracted_json/invoice_data.json"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)
