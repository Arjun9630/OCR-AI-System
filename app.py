import sys
from pathlib import Path
import tempfile
import streamlit as st
from src.ocr.ocr_engine import ocr_image, ocr_pdf
from src.ml.classifier import predict_document_type
from src.ml.extract_invoice_fields import extract_invoice_fields

# Add project root
ROOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(ROOT_DIR))

st.set_page_config(page_title="OCR AI System", layout="wide")

st.title("📄 OCR-Based Document Processing & Classification System")

uploaded_file = st.file_uploader(
    "Upload a document (Invoice / Contract / Report)",
    type=["png", "jpg", "jpeg", "pdf"]
)

if uploaded_file:
    st.success("File uploaded successfully")

    # Save uploaded file temporarily
    suffix = Path(uploaded_file.name).suffix
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    # OCR
    with st.spinner("Running OCR..."):
        if suffix.lower() == ".pdf":
            ocr_text = ocr_pdf(temp_path)
        else:
            ocr_text = ocr_image(temp_path)

    st.subheader("📄 OCR Extracted Text")
    st.text_area("OCR Output", ocr_text, height=250)

    # Document Classification
    doc_type = predict_document_type(ocr_text)

    st.subheader("🧠 Document Classification")
    st.success(f"Predicted Document Type: **{doc_type.upper()}**")

    # Structured Extraction for Invoice
    if doc_type == "invoice":
        st.subheader("📊 Structured Invoice Data (JSON)")
        extracted_data = extract_invoice_fields(ocr_text)
        st.json(extracted_data)

    st.info("Processing completed successfully.")