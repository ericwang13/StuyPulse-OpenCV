# import numpy as np
import cv2 as cv

# 0 is the id of the video capture device, my PC only has one webcam, so 0 id will always refer to that one
# You can read an existing video the same way, just replace the id with the video file
cap = cv.VideoCapture(0)
# cap = cv.VideoCapture("../video/taylor-cheer.mp4")
res = 1280, 720

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
    post = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.namedWindow("frame", cv.WINDOW_NORMAL)
    cv.resizeWindow("frame", 1280, 720)
    cv.imshow("frame", post)

    if cv.waitKey(40) == ord('q'):# or cv.getWindowProperty('Window Camera', cv.WND_PROP_VISIBLE) < 1:
        break
    # if cv.waitKey(10) == ord('q'):  # The waitKey() argument defines how many ms should the program wait between
    #     # frames to check if an input was given, if this argument is too high (100 or 1000) the video will appear in
    #     # slow motion, a value like 1 ms will look the best
    #     break  # If the user does input the correct keycode, the infinite loop is broken so the program can carry on

# When everything done, release the capture and kill the GUIs
cap.release()
cv.destroyAllWindows()
