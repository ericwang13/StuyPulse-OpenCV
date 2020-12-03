import numpy as np
import cv2 as cv
import matplotlib as mpl
from matplotlib import pyplot as plt

# print(np.__version__)
# print(cv.__version__)
# print(mpl.__version__)

img = cv.imread("photo-1552519507-da3b142c6e3d.jfif",0)

edges = cv.Canny(img, 100, 200)

plt.subplot(121),plt.imshow(img,cmap = "gray")
plt.title("Original Image"), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(edges,cmap = "gray")
plt.title("Edge Image"), plt.xticks([]), plt.yticks([])

plt.show()
