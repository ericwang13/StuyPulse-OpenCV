# import numpy as np
import cv2 as cv

# 0 is the id of the video capture device, my PC only has one webcam, so 0 id will always refer to that one
# You can read an existing video the same way, just replace the id with the video file
cap = cv.VideoCapture(0)

# Checks that the video capture device is working properly
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    # ret is set to true or false, frame is the actual frame matrix itself
    ret, frame = cap.read()
    # This checks if the frame was read correctly, if not the program exits, it also checks if the stream ends
    if not ret:
        print("Can't receive frame (stream end?). Exiting")
        break
    # Here would all the frame processes go, in this case all we do is convert the color to greyscale
    lap = cv.Laplacian(frame,cv.CV_64F)
    sobelx = cv.Sobel(frame,cv.CV_64F,1,0,ksize=5)
    sobely = cv.Sobel(frame,cv.CV_64F,0,1,ksize=5)

    sobel = cv.addWeighted(sobelx,1/3,sobely,1/3,0)
    post = cv.addWeighted(lap,1/3,sobel,2/3,0)
    # Display the resulting frame
    cv.imshow('frame', post)

    # The waitKey() argument defines how many ms should the program wait between
    k = cv.waitKey(1)
    if cv.getWindowProperty('frame', cv.WND_PROP_VISIBLE) < 1:
        break
        # frames to check if an input was given, if this argument is too high (100 or 1000) the video will appear in
        # slow motion, a value like 1 ms will look the best
         # If the user does input the correct keycode, the infinite loop is broken so the program can carry on

# When everything done, release the capture and kill the GUIs
cap.release()
cv.destroyAllWindows()
