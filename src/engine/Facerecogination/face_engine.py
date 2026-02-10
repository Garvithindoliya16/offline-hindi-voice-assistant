import cv2
import numpy as np
import os

CASCADE = cv2.CascadeClassifier("Facerecogination/haarcascade_frontalface_default.xml")
RECOGNIZER = cv2.face.LBPHFaceRecognizer_create()

MODEL_FILE = "faces/recognizer.yml"

if os.path.exists(MODEL_FILE):
    RECOGNIZER.read(MODEL_FILE)

def detect_face(gray):
    faces = CASCADE.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(60, 60)
    )
    return faces[0] if len(faces) else None

def recognize_face(gray_face):
    try:
        label, confidence = RECOGNIZER.predict(gray_face)
        return label, confidence
    except:
        return None, None

def train_face(gray_face, label_id):
    RECOGNIZER.update([gray_face], np.array([label_id]))
    RECOGNIZER.write(MODEL_FILE)
