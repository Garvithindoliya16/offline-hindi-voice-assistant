import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("intent_data.csv")

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,3), analyzer="char_wb")),
    ("clf", MultinomialNB(alpha=0.3))
])

pipeline.fit(data["sentence"], data["intent"])

joblib.dump(pipeline, "intent_model.pkl")
print("Model trained")
