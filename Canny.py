import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

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

    m = np.median(frame)

    plt.subplot(1, 4, 1)
    plt.imshow(frame)
    plt.title("Original")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 4, 2)
    plt.imshow(cv.Canny(frame, max(0,0.5*m), min(1.5 * m, 255)))
    plt.title("0.5")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 4, 3)
    plt.imshow(cv.Canny(frame, max(0,0.66*m), min(1.33 * m, 255)))
    plt.title("0.66")
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 4, 4)
    plt.imshow(cv.Canny(frame, 255/3, 255))
    plt.title("255 and 255/3")
    plt.xticks([])
    plt.yticks([])

    plt.show()
    if cv.waitKey(1) == 'q' or cv.getWindowProperty('Window Camera', cv.WND_PROP_VISIBLE) < 1:
        break


cap.release()
cv.destroyAllWindows()