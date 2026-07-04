from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

text = """
Artificial Intelligence is transforming industries worldwide.
Companies are investing heavily in machine learning.
New AI models are becoming more capable every year.
Researchers continue to improve performance and efficiency.
Many experts believe AI will reshape the future of work.
"""

summary = summarizer(
    text,
    max_length=50,
    min_length=20,
    do_sample=False
)

print(summary[0]["summary_text"])