import cv2 as cv

img1 = cv.imread(cv.samples.findFile("ocean400.png"))
img2 = cv.imread(cv.samples.findFile("arthursfist400.png"))

dst = cv.addWeighted(img1,0.7,img2,0.3,0)

cv.imshow("dst",dst)
cv.waitKey(0)
cv.destroyAllWindows()