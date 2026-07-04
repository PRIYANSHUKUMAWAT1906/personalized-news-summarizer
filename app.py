import streamlit as st
import pandas as pd
import re

from datetime import datetime
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Load dataset
df = pd.read_csv("data/processed/news_dataset.csv")

# ---------------- Functions ---------------- #

def recency_score(date):
    try:
        published = datetime.fromisoformat(
            date.replace("Z", "+00:00")
        )

        age = (
            datetime.now(published.tzinfo)
            - published
        ).days

        if age <= 1:
            return 5
        elif age <= 7:
            return 3
        else:
            return 1

    except:
        return 0


def clean_text(text):
    text = str(text)

    text = re.sub(r"<.*?>", "", text)
    text = text.replace("nan", "")
    text = re.sub(r"\[\+\d+\schars\]", "", text)

    return text


def generate_summary(text):

    parser = PlaintextParser.from_string(
        text,
        Tokenizer("english")
    )

    summarizer = TextRankSummarizer()

    summary = summarizer(
        parser.document,
        2
    )

    return " ".join(str(sentence) for sentence in summary)


# ---------------- UI ---------------- #

st.title("📰 Personalized News Summarizer")

interests = st.multiselect(
    "Select Categories",
    [
        "technology",
        "science",
        "sports",
        "health",
        "business",
        "entertainment"
    ]
)

if st.button("Get Recommendations"):

    user_profile = {
        "interests": interests,
        "keywords": ["AI", "machine learning", "robotics"]
    }

    def score_row(row):

        score = 0

        if row["category"] in user_profile["interests"]:
            score += 10

        text = (
            str(row["title"]) + " " +
            str(row["content"])
        ).lower()

        for keyword in user_profile["keywords"]:
            if keyword.lower() in text:
                score += 5

        score += recency_score(
            row["publishedAt"]
        )

        return score

    temp_df = df.copy()

    temp_df["score"] = temp_df.apply(
        score_row,
        axis=1
    )

    recommended = temp_df.sort_values(
        by="score",
        ascending=False
    )

    top_articles = recommended.head(5)

    for _, row in top_articles.iterrows():

        article_text = (
            clean_text(row["title"]) + ". " +
            clean_text(row["description"]) + ". " +
            clean_text(row["content"])
        )

        summary = generate_summary(article_text)

        st.subheader(row["title"])

        st.write(f"📂 Category: {row['category']}")
        st.write(f"⭐ Score: {row['score']}")
        st.write(f"📅 Published: {row['publishedAt']}")

        st.write("### Summary")
        st.write(summary)

        st.divider()