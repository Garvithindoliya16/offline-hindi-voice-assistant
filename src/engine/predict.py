import joblib

model = joblib.load("hindi_number_normalizer.joblib")

def normalize(text):
    tokens = text.split()
    norm_tokens = []

    for t in tokens:
        try:
            norm_tokens.append(model.predict([t])[0])
        except:
            norm_tokens.append(t)

    return " ".join(norm_tokens)






