import cv2

# Reads out image pixels and store as a numpy array
img = cv2.imread('assets/logo.png', cv2.IMREAD_COLOR)

# Printing pixels value with range
print(img[257][45:400])