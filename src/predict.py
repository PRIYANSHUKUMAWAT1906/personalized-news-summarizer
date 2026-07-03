import joblib

model = joblib.load("models/news_classifier.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

text = """
OpenAI released a new AI model that improves reasoning and coding abilities.
"""

text_vector = vectorizer.transform([text])

prediction = model.predict(text_vector)

print("Predicted Category:", prediction[0])