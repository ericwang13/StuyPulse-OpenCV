import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Camera no work")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Couldn't read frame")
        break
    rows, cols, channels = frame.shape

    frame = cv.add(frame, cv.cvtColor(cv.Canny(frame,rows/5,cols/5),cv.COLOR_GRAY2BGR))
    frame = cv.flip(frame, 1)
    cv.imshow('Window Camera', frame)

    k = cv.waitKey(1)
    if cv.getWindowProperty('Window Camera', cv.WND_PROP_VISIBLE) < 1:
        break


cap.release()
cv.destroyAllWindows()