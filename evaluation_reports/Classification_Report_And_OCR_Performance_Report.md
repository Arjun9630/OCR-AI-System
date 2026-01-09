# OCR-AI-System  
## Evaluation Report & OCR Performance Analysis

---

## 1. Project Overview

This project implements an AI-powered document processing system that uses Optical Character Recognition (OCR) and Machine Learning to automate text extraction and document classification from corporate documents such as invoices, contracts, and reports.

The system is designed to reduce manual effort, improve accuracy, and demonstrate the application of Vision Intelligence and Machine Learning techniques in real-world document automation scenarios.

---

## 2. System Architecture

### Components:
1. **OCR Engine**
   - Converts scanned images and PDFs into machine-readable text.
   - Implemented using Tesseract OCR with image preprocessing.

2. **Preprocessing Module**
   - Enhances image quality by resizing, grayscale conversion, and noise reduction.
   - Improves OCR accuracy on low-quality documents.

3. **Structured Data Extraction**
   - Extracts key invoice fields (invoice number, date, total amount, tax, etc.) using rule-based logic.
   - Outputs structured data in JSON format.

4. **Machine Learning Classifier**
   - Classifies documents into:
     - Invoice
     - Contract
     - Report
   - Uses TF-IDF feature extraction and Logistic Regression.

5. **Frontend Interface**
   - Built using Streamlit.
   - Allows users to upload documents and view OCR output, document type, and extracted data.

---

## 3. Dataset Description

The system was evaluated using real-world corporate documents:

### Document Types Used:
- **Invoices**
  - Scanned invoice images (PNG)
- **Contracts**
  - IBM Federal Cloud Services Agreement (PDF)
- **Reports**
  - IBM Annual Report 2024 (PDF)

These documents represent realistic business use cases and varying document layouts.

---

## 4. OCR Performance Evaluation

### OCR Accuracy Observations:
- Clear scanned invoices showed **high text recognition accuracy**.
- Structured documents with tables and headings were processed correctly.
- Large PDF documents (e.g., annual reports) were partially OCR’d (first few pages) for efficiency.

### Performance Characteristics:
| Metric | Observation |
|------|------------|
| Accuracy | High for clear text and standard fonts |
| Processing Time | Increases with document length |
| CPU Usage | High during OCR (expected behavior) |
| Noise Sensitivity | Moderate for low-quality scans |

### Optimization Applied:
- DPI reduced for faster OCR
- OCR limited to first few pages for large documents
- Balanced preprocessing pipeline used instead of aggressive enhancement

---

## 5. Machine Learning Model Evaluation

### Model Used:
- **TF-IDF Vectorizer**
- **Logistic Regression Classifier**

### Evaluation Method:
- Train-test split on OCR-extracted text
- Manual validation using unseen documents

### Observed Results:
- High accuracy for documents similar to training data
- Correct classification for:
  - Invoices → Invoice
  - IBM FCSA → Contract
  - IBM Annual Report → Report

### Limitations:
- Documents outside trained categories (e.g., stock research PDFs) may be misclassified.
- Model performance depends on dataset diversity.

---

## 6. End-to-End System Evaluation

The complete pipeline was tested using the Streamlit frontend:

### Workflow:
1. Upload document (image or PDF)
2. OCR text extraction
3. Document classification using ML
4. Structured data extraction (for invoices)
5. Display of results in UI

### Outcome:
- System successfully processes documents end-to-end.
- Outputs are interpretable and suitable for business use cases.

---

## 7. Limitations

- Rule-based invoice extraction has limited flexibility across highly diverse layouts.
- OCR accuracy depends on input image quality.
- ML classifier is trained on a limited dataset for demonstration purposes.

---

## 8. Future Enhancements

- Integration of Large Language Models (LLMs) for semantic data extraction.
- Expansion of training dataset for improved classification accuracy.
- Support for additional document types.
- Confidence scoring for classification results.
- Batch processing for enterprise-scale deployment.

---

## 9. Conclusion

The OCR-AI-System successfully demonstrates the use of Vision Intelligence and Machine Learning for automated document processing and classification. The project fulfills all stated objectives and provides a scalable foundation for future enhancements in intelligent document automation.
