import cv2
import time
from .camera_utils import get_frame
from .face_engine import detect_face, recognize_face, train_face
from .face_db import load_labels, save_labels


class Facerecogination:

    def __init__(self):
        self.found_face = None
        self.face_img = None
        self.labels = load_labels()
        self.next_id = len(self.labels)

    def capture(self):

        self.found_face = None
        self.face_img = None

        start = time.time()

        while time.time() - start < 5:
            frame = get_frame()
            if frame is None:
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.equalizeHist(gray)

            face = detect_face(gray)

            if face is not None:
                x, y, w, h = face

                face_img = gray[y:y+h, x:x+w]

                if face_img is None or face_img.size == 0:
                    continue

                self.found_face = face
                self.face_img = cv2.resize(face_img, (200, 200))
                break

    def faceReco(self):

        if self.face_img is None:
            return None

        label, confidence = recognize_face(self.face_img)

        if label is not None and confidence < 80 and label in self.labels:
            return self.labels[label]

        return None

    def saveUser(self, name):

        if not name:
            return

        if self.face_img is None or self.face_img.size == 0:
            return

        self.labels[self.next_id] = name
        save_labels(self.labels)

        train_face(self.face_img, self.next_id)

        print(f"Saved new user: {name}")

        self.next_id += 1

