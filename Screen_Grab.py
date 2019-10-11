import time

import cv2
import mss
import keyboard
import numpy


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 200, "left": 170, "width": 1, "height": 56}

    while "Screen capturing":
        #last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        if(img[45][0][1] < 255 or img[20][0][1] < 255):
            keyboard.press('space')

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break