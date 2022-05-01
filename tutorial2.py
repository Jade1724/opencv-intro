import cv2

# Reads out image pixels and store as a numpy array
img = cv2.imread('assets/logo.png', cv2.IMREAD_COLOR)

# Shows the image is a numpy array
print(img)
# Outputs (height in px, width in px, channels) of the image
print(img.shape)