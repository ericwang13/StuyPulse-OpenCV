import cv2 as cv  # Import opencv-python into the project and give it the alias cv for convenience

# Read the image file with image read
# Could take a second argument for format

# IMREAD_COLOR is the default, reads the image only considering the RGB channels, ignoring the alpha channel
# If no second argument is passed, this format is used
img = cv.imread("../img/fox.jpg", cv.IMREAD_COLOR)

# IMREAD_UNCHANGED reads the image with the alpha channel, allowing for transparency
# img = cv.imread("fox.jpg", cv.IMREAD_UNCHANGED)
# IMREAD_GRASCALE reads the image in greyscale
# img = cv.imread("fox.jpg", cv.IMREAD_GRAYSCALE)

# Different way to read the file, using another OpenCV function for locating files
# img = cv.imread(cv.samples.findFile("fox.jpg"))

# Check that image was loaded in properly
if img is None:  # None is effectively == to null
    print("Image could not be read")
    exit()

# Window name followed by image matrix
cv.namedWindow("frame", cv.WINDOW_NORMAL)
cv.resizeWindow("frame", 1280, 720)
cv.imshow("frame", img)

# waitKey() does 2 things, it takes an input from the user as a keycode and keeps the window open
# Without this, the program displays the image and immediately closes the window
# waitKey() tells the program to wait n ms before closing the window, but if 0 is passed it means to wait
# infinitely until a condition is met, the condition here is that the keycode is equal to "q"
key = cv.waitKey(0)
if key == ord("q") or cv.getWindowProperty('Window Camera', cv.WND_PROP_VISIBLE) < 1:
    # You can destroy one window specifically or all windows, in this case there is only 1 window
    cv.destroyWindow("frame")  # cv.destroyAllWindows()
    # This allows you to rewrite the img matrix to another file, or the same file
    # cv.imwrite("fox.jpg", img)
