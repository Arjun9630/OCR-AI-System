from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

from src.ml.extractor import load_documents


def train_classifier():
    texts, labels = load_documents()

    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000
    )

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    y_pred = model.predict(X_test_vec)

    print("\nMODEL EVALUATION:\n")
    print(classification_report(y_test, y_pred))

    # Save model & vectorizer
    joblib.dump(model, "src/ml/document_classifier.pkl")
    joblib.dump(vectorizer, "src/ml/tfidf_vectorizer.pkl")


def predict_document_type(ocr_text):
    model = joblib.load("src/ml/document_classifier.pkl")
    vectorizer = joblib.load("src/ml/tfidf_vectorizer.pkl")

    vec = vectorizer.transform([ocr_text])
    return model.predict(vec)[0]

if __name__ == "__main__":
    train_classifier()