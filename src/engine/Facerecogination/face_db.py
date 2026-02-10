import pickle
import os

FACES_DIR = "faces"
LABELS_FILE = os.path.join(FACES_DIR, "labels.pkl")

def load_labels():
    if not os.path.exists(LABELS_FILE):
        return {}
    with open(LABELS_FILE, "rb") as f:
        return pickle.load(f)

def save_labels(labels):
    os.makedirs(FACES_DIR, exist_ok=True)  # 🔥 THIS FIX
    with open(LABELS_FILE, "wb") as f:
        pickle.dump(labels, f)
