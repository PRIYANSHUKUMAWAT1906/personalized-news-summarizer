import pandas as pd
import joblib

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Load model and vectorizer
model = joblib.load("models/news_classifier.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Load dataset
df = pd.read_csv("data/processed/news_dataset.csv")

# Pick an article
article = df.iloc[0]

title = str(article["title"])
description = str(article["description"])
content = str(article["content"])

# ---------- Classification ----------

text_for_classification = (
    title + " " +
    description + " " +
    content
)

text_vector = vectorizer.transform([text_for_classification])

predicted_category = model.predict(text_vector)[0]

# ---------- Summarization ----------

text_for_summary = (
    title + ". " +
    description + ". " +
    content
)

parser = PlaintextParser.from_string(
    text_for_summary,
    Tokenizer("english")
)

summarizer = TextRankSummarizer()

summary = summarizer(parser.document, 3)

# ---------- Output ----------

print("\n" + "=" * 50)

print("\nTITLE:")
print(title)

print("\nPREDICTED CATEGORY:")
print(predicted_category)

print("\nSUMMARY:")

for sentence in summary:
    print("-", sentence)

print("\n" + "=" * 50)