import cv2
import random

# Reads out image pixels and store as a numpy array
img = cv2.imread('assets/logo.png', cv2.IMREAD_COLOR)

for i in range(100):
    for j in range(img.shape[1]):

        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()