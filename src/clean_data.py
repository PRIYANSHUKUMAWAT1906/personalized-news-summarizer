import pandas as pd
import re

df = pd.read_csv("data/processed/news_dataset.csv")

# Keep useful columns
df = df[["title", "description", "content", "category"]]

# Remove missing values
df = df.dropna()

# Combine text fields
df["text"] = (
    df["title"] + " " +
    df["description"] + " " +
    df["content"]
)

# Lowercase
df["text"] = df["text"].str.lower()

# Remove URLs
df["text"] = df["text"].apply(
    lambda x: re.sub(r"http\S+", "", x)
)

# Remove special characters
df["text"] = df["text"].apply(
    lambda x: re.sub(r"[^a-zA-Z\s]", "", x)
)

# Remove extra spaces
df["text"] = df["text"].apply(
    lambda x: " ".join(x.split())
)

print(df.head())

df.to_csv(
    "data/processed/clean_news_dataset.csv",
    index=False
)

print("Clean dataset saved")