# OCR-AI-System  
### Document Processing and Classification using OCR & Machine Learning

OCR-AI-System is an AI-powered application that automates text extraction and document classification from corporate documents such as invoices, contracts, and reports. The system demonstrates the use of Vision Intelligence and Machine Learning to process unstructured documents with minimal human intervention.

This project was developed as part of the **TCS iON AIP-135 Industry Project**.

## Key Features

- OCR-based text extraction from scanned images and PDF documents.  
- Machine Learning–based document classification into:
  - Invoice
  - Contract
  - Report  
- Structured invoice data extraction and JSON output.
- Interactive frontend built using Streamlit for end-to-end demonstration.  

## Technologies Used

Python, Tesseract OCR, OpenCV, pdf2image, scikit-learn (TF-IDF and Logistic Regression), Streamlit

## Dataset and Evaluation

The system was evaluated using real-world corporate documents, including scanned invoice images, the IBM Federal Cloud Services Agreement (contract), and the IBM Annual Report 2024 (report). OCR-extracted text from these documents was used to train and validate the machine learning classifier.

Detailed OCR performance analysis and model evaluation are available in the evaluation_report folder.

## How to Run the Application

```bash
streamlit run app.py

```

## Limitations

- Invoice field extraction is rule-based and may not generalize to all invoice layouts

- OCR accuracy depends on the quality of the input document

- The machine learning classifier performs best on document categories represented in the training dataset

- Documents outside the defined classes may be misclassified

## Future Enhancements

- Integration of Large Language Models (LLMs) for semantic data extraction

- Expansion of the training dataset for improved classification accuracy

- Support for additional document categories

- Confidence scoring for classification results

- Batch document processing

## Conclusion

The OCR-AI-System successfully demonstrates automated document processing using OCR and Machine Learning. The project fulfills all objectives defined under the TCS iON AIP-135 program and provides a scalable foundation for intelligent document automation.
