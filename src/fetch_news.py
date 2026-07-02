from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

API_KEY = os.getenv("News_API")

newsapi = NewsApiClient(api_key=API_KEY)

articles = newsapi.get_everything(
    q="technology",
    language="en",
    sort_by="publishedAt",
    page_size=20
)

print("Articles fetched:", len(articles["articles"]))

with open("data/raw/technology_news.json", "w", encoding="utf-8") as f:
    json.dump(articles["articles"], f, indent=4)

print("Saved successfully!")