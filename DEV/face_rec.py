#imports

import numpy as np
import os
import math
from matplotlib import pyplot as plt
#%matplotlib inline
import cv2
print (cv2.__version__)

webcam = cv2.VideoCapture(0)
ret, frame = webcam.read()
print (ret)
webcam.release()

# open new thread to manage external cv2 interaction
cv2.startWindowThread()

cv2.namedWindow("PyData Tutorial", cv2.WINDOW_NORMAL)
cv2.imshow("PyData Tutorial", frame)

#press any key to close external window
cv2.waitKey()
cv2.destroyAllWindows()
