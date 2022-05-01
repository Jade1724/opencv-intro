'''
Corner detection tutorial involving introduction to computer vision algorithms supported in OpenCV
Useful documentation: https://opencv-python-tutorials.readthedocs.io

This tutorial focuses on Shi-Tomasi corner detection & good features to track
'''

import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0, 0,), fx=0.75, fy=0.75)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

