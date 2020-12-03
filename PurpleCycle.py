import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Camera no work")
    exit()

up = True
num = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Couldn't read frame")
        break
    rows, cols, channels = frame.shape
    upsideDown = cv.warpAffine(
                frame,
                cv.getRotationMatrix2D(((cols - 1)/2.0, (rows - 1)/2.0), 180, 1),
                (cols, rows)
            )
    red = upsideDown.copy()
    blue = upsideDown.copy()

    red[:,:,1] = 0
    red[:,:,0] = 0
    blue[:,:,1] = 0
    blue[:,:,2] = 0

    upsideDown = red + blue

    yellow = frame.copy()
    yellow[:,:,0] = 0

    frame = cv.addWeighted(upsideDown, num, yellow, 1 - num, 0)
    cv.imshow('Window Camera', frame)

    if up:
        num += 0.05
        if num >= 1:
            up = False
    else:
        num -= 0.05
        if num <= 0:
            up = True

    k = cv.waitKey(1)
    if cv.getWindowProperty('Window Camera', cv.WND_PROP_VISIBLE) < 1:
        break


cap.release()
cv.destroyAllWindows()