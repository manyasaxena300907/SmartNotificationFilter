"""train.py - Load data, TF-IDF, train Naive Bayes, save model (Days 4-5)."""
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from src.config import (DATA_PATH, MODEL_PATH, VECTORIZER_PATH,
                        TEST_SIZE, RANDOM_STATE)
from src.preprocess import clean_text


def train_model():
    # TODO (Day 4): df = pd.read_csv(DATA_PATH); df["clean"] = df["message"].apply(clean_text)
    # TODO (Day 4): split with train_test_split (use stratify=df["label"])
    # TODO (Day 4): vectorizer = TfidfVectorizer(); fit on TRAIN only, then transform train and test
    # TODO (Day 5): model = MultinomialNB(); model.fit(X_train, y_train)
    # TODO (Day 5): joblib.dump(model, MODEL_PATH); joblib.dump(vectorizer, VECTORIZER_PATH)
    # TODO: return model, vectorizer, X_test, y_test
    pass
