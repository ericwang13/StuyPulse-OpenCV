import cv2 as cv

src = cv.imread('ocean.jpg')

#percent by which the image is resized
# scale_percent = 50

#calculate the 50 percent of original dimensions
# width = int(src.shape[1] * scale_percent / 100)
# height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (400,400)

# resize image
output = cv.resize(src, dsize)

k = cv.waitKey(0)

cv.imwrite('ocean400.png', output) 
if k == ord(" "):
    cv.destroyAllWindows()
