import os


def load_documents(base_path="test_documents"):
    """
    Loads OCR text files and assigns labels based on folder name.
    Folder structure:
    test_documents/
        invoices/
        contracts/
        reports/
    """

    texts = []
    labels = []

    for doc_type in ["invoices", "contracts", "reports"]:
        folder = os.path.join(base_path, doc_type)

        if not os.path.exists(folder):
            continue

        for file in os.listdir(folder):
            if file.endswith(".txt"):
                with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                    texts.append(f.read())
                    labels.append(doc_type[:-1])  # invoice, contract, report

    return texts, labels
