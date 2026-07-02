import json
import pandas as pd

with open("data/raw/technology_news.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

df = pd.DataFrame(articles)

print(df.head())
print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())