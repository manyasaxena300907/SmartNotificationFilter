# Smart Notification Filter

A small NLP project that classifies a typed or pasted message as **important** or **not important**.
Important messages trigger an alert. Everything else is saved in a history log.

- Domain: Artificial Intelligence (NLP, text classification)
- Model: TF-IDF + Multinomial Naive Bayes (compared with Logistic Regression)
- Interface: Streamlit web app

## Project flow
Training:   data/messages.csv -> preprocess -> TF-IDF (fit) -> Naive Bayes (train) -> evaluate -> save with joblib
Prediction: message -> same preprocess -> TF-IDF (transform) -> Naive Bayes -> alert or history log

## Folder guide
| Path | What it is |
|---|---|
| main.py | Runs the full training pipeline |
| app.py | Streamlit interface |
| data/messages.csv | Labeled dataset (message, label: 1 = important, 0 = not) |
| data/labeling_rules.md | Rules used to decide labels |
| data/history.csv | Non-important messages saved by the app |
| models/ | Saved model.joblib and vectorizer.joblib |
| src/config.py | File paths and settings in one place |
| src/preprocess.py | Text cleaning (used by training AND the app) |
| src/train.py | TF-IDF + Naive Bayes training |
| src/evaluate.py | Accuracy, precision, recall, F1, confusion matrix |
| src/predict.py | Load the saved model and predict one message |
| src/history.py | Save and read the history log |
| practice/ | Learning scripts (not part of the final project) |
| reports/ | Confusion matrix image, screenshots |
| docs/ | Report outline and viva questions |
| tests/ | Small tests |

## How to run
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. python main.py          (trains and saves the model)
5. streamlit run app.py    (opens the interface)

## Future scope
Telegram or email input, dashboard, DistilBERT, OCR-based screen reading.
