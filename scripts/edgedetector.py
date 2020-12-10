import numpy as np
import cv2 as cv

# Kernel Convolution
# A kernel in CV != kernel in computer architecture
# Kernels are each section of pixels that a program will read through as it performs processes on an image


# img = cv.imread("../img/plain.png")
#
# guassian = cv.GaussianBlur(img, (5, 5), 0)
# box = cv.boxFilter(img, -1, (25, 25))
#
#
# cv.namedWindow("frame", cv.WINDOW_NORMAL)
# cv.resizeWindow("frame", 1280, 720)
# cv.imshow("frame",np.hstack((img, guassian, box)))
#
# if cv.waitKey() == ord("q"):
#     cv.destroyAllWindows()

# for i in img:
#     print(i)

# for i in img:
#     for j in i:
#         j[0] -= 100
#         j[1] -= 200
#         j[2] -= 50
#
#
# cv.imshow("frame", img)
# cv.waitKey(0)