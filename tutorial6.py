'''
Corner detection tutorial involving introduction to computer vision algorithms supported in OpenCV
Useful documentation: https://opencv-python-tutorials.readthedocs.io

This tutorial focuses on Shi-Tomasi corner detection & good features to track
'''

from turtle import color
import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0, 0,), fx=0.75, fy=0.75)

# For the corner detection, greyscale image is easier to find features
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Shi-Tomashi corner detection function
# Pass the source image, the number of best corner to return, minimum quality (degree of confidence) of corner, minimum Euclidean distant of two corners
corners = cv2.goodFeaturesToTrack(grey, 100, 0.01, 10)

# The extracted corners are float, needed to be converted into int
corners = np.int0(corners)

# Loop through each corner to decompose the nested numpy array
for corner in corners:
    # ravel() flattens numpy array
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

# Draw lines between corners
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        # Generate random color
        # Convert numpy's special 64 bits integer to Python 32 bit integer
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)


cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()