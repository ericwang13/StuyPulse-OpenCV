import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
#ret is return, boolean;
if not cap.isOpened():
    print("error1")
    exit()
while True:
    ret, frame = cap.read()
    if (not ret):
        print ("error2")
        break
    #processes
    kernel = np.ones((5,5),np.uint8)
    erosion = cv.erode(frame,kernel,iterations = 1)
    #OR
    cv.imshow("video",erosion)
    k = cv.waitKey(1)
    if k == ord("q"):
        break

cap.release()
cv.destroyAllWindows()