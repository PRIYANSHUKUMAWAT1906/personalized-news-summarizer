import pandas as pd

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

df = pd.read_csv("data/processed/clean_news_dataset.csv")
text = (
    str(df.iloc[0]["title"]) + ". " +
    str(df.iloc[0]["description"]) + ". " +
    str(df.iloc[0]["content"])
)

parser = PlaintextParser.from_string(
    text,
    Tokenizer("english")
)

summarizer = TextRankSummarizer()

summary = summarizer(parser.document, 3)

print("\nSUMMARY:\n")

for sentence in summary:
    print(sentence)