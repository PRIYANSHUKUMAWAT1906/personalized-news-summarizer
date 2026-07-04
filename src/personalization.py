import pandas as pd

df = pd.read_csv("data/processed/clean_news_dataset.csv")

user_profile = {
    "interests": ["technology", "science"],
    "keywords": ["AI", "machine learning", "robotics"]
}
def score_row(row):
    score = 0

    if row["category"] in user_profile["interests"]:
        score += 10

    text = (
        str(row["title"]) + " " +
        str(row["text"])
    ).lower()

    for keyword in user_profile["keywords"]:
        if keyword.lower() in text:
            score += 5

    return score
df["score"] = df.apply(
    score_row,
    axis=1
)
recommended = df.sort_values(
    by="score",
    ascending=False
)

print(
    recommended[
        ["title", "category", "score"]
    ].head(20)
)