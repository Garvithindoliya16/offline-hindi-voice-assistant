import cv2
import time
from camera_utils import get_frame
from face_engine import detect_face, recognize_face, train_face
from face_db import load_labels, save_labels
# from speaker import speak
# from stt import listen   # your VOSK listen()
from engine.speaker import speak

labels = load_labels()
next_id = len(labels)

speak("कृपया कैमरे की तरफ देखें")

found_face = None
start = time.time()

# -------- FACE DETECTION LOOP --------
while time.time() - start < 5:
    frame = get_frame()
    if frame is None:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    face = detect_face(gray)
    if face is not None:
        found_face = face
        break

if found_face is None:
    speak("चेहरा दिखाई नहीं दे रहा")
    exit()

x, y, w, h = found_face
face_img = gray[y:y+h, x:x+w]

label, confidence = recognize_face(face_img)

# -------- KNOWN USER --------
if label is not None and confidence < 80 and label in labels:
    name = labels[label]
    speak(f"नमस्ते {name} जी, आपका स्वागत है")
    

# -------- NEW USER --------
else:
    speak("नमस्ते, आप पहली बार आए हैं")
    speak("कृपया अपना नाम बताइए")

    name = listen()
    speak(f"धन्यवाद {name}")

    labels[next_id] = name
    save_labels(labels)

    train_face(face_img, next_id)
    speak("आपकी पहचान सुरक्षित कर ली गई है")
