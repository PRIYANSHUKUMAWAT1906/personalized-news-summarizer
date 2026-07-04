import pandas as pd

df = pd.read_csv("data/processed/news_dataset.csv")
user_profile = {
    "interests": ["technology", "science"],
    "keywords": ["AI", "machine learning", "robotics"]
}
from datetime import datetime

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

    # Add recency score
    score += recency_score(
        row["publishedAt"]
    )

    return score
df["score"] = df.apply(score_row, axis=1)

recommended = df.sort_values(
    by="score",
    ascending=False
)

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

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

    return " ".join(
        str(sentence)
        for sentence in summary
    )


import re
def clean_text(text):
    text = str(text)

    text = re.sub(r"<.*?>", "", text)
    text = text.replace("nan", "")
    text = text.replace("[+2420 chars]", "")

    return text
top_articles = recommended.head(5)

for index, row in top_articles.iterrows():
   

    article_text = (
        str(row["title"]) + ". " +
        str(row["description"]) + ". " +
        str(row["content"])
    )

    summary = generate_summary(article_text)

    print("\n" + "=" * 60)

    print("TITLE:")
    print(row["title"])

    print("\nCATEGORY:")
    print(row["category"])

    print("\nSCORE:")
    print(row["score"])

    print("\nPUBLISHED:")
    print(row["publishedAt"])

    print("\nSUMMARY:")
    print(summary)

    print("\n" + "=" * 60)