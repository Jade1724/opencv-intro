import cv2
import random

# Reads out image pixels and store as a numpy array
img = cv2.imread('assets/logo.png', cv2.IMREAD_COLOR)

# Getting a pixel slice of an image
tag = img[200:300, 200: 300]
# Pick a distination to copy the image segment. Note the source and the distination has to be the same dimension.
img[100:200, 100:200] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()