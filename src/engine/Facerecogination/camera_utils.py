import cv2

def get_frame():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()
    return frame if ret else None
