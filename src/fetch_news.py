from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

API_KEY = os.getenv("NEWS_API")

newsapi = NewsApiClient(api_key=API_KEY)

categories = [
    "technology",
    "business",
    "sports",
    "health",
    "science",
    "entertainment"
]

for category in categories:
    articles = newsapi.get_everything(
        q=category,
        language="en",
        page_size=20
    )

    filename = f"data/raw/{category}_news.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(articles["articles"], f, indent=4)

    print(f"{category}: {len(articles['articles'])} articles saved")