import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("photo-1552519507-da3b142c6e3d.jfif"))

if img is None:
    sys.exit("Could not read image")

cv.imshow("Display", img)
k = cv.waitKey(0)

if k == ord(" "):
    cv.imwrite("img2.jpg", img)
