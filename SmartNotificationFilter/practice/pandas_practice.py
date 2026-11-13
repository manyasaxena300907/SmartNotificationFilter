"""Day 1 practice - run with:  python practice/pandas_practice.py"""
import pandas as pd

data = {
    "message": [
        "Exam tomorrow at 9 AM in Hall B",
        "Good morning everyone!",
        "Last date to pay fees is 15th Oct",
    ],
    "label": [1, 0, 1],
}
df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df["label"].value_counts())
print(df[df["label"] == 1])
