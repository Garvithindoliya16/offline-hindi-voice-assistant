import joblib

model = joblib.load("intent_model.pkl")

def predict_intent(text):
    prob = model.predict_proba([text])[0]
    pred = model.classes_[prob.argmax()]
    if prob.max() < 0.40:
        return "other"
    return pred



