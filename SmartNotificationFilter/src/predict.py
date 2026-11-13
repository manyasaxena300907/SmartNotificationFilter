"""predict.py - Load the saved model and classify ONE message (Day 7)."""
import joblib

from src.config import MODEL_PATH, VECTORIZER_PATH
from src.preprocess import clean_text


def predict_message(message: str) -> int:
    """Return 1 (important) or 0 (not important)."""
    # TODO (Day 7):
    # 1. model = joblib.load(MODEL_PATH); vectorizer = joblib.load(VECTORIZER_PATH)
    # 2. cleaned = clean_text(message)
    # 3. features = vectorizer.transform([cleaned])      # transform, NOT fit
    # 4. return int(model.predict(features)[0])
    pass
