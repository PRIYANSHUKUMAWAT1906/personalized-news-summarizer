import json
import pandas as pd

categories = [
    "technology",
    "business",
    "sports",
    "health",
    "science",
    "entertainment"
]

all_data = []

for category in categories:

    with open(
        f"data/raw/{category}_news.json",
        "r",
        encoding="utf-8"
    ) as f:

        articles = json.load(f)

        for article in articles:
            article["category"] = category
            all_data.append(article)

df = pd.DataFrame(all_data)

print(df.shape)

df.to_csv(
    "data/processed/news_dataset.csv",
    index=False
)

print("Dataset saved successfully")