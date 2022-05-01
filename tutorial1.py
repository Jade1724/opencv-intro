import cv2

img = cv2.imread('assets/logo.png', 1)
cv2.imshow('Image', img)

# Wait for any key press for infinite time
cv2.waitKey(0)
cv2.destroyAllWindows()