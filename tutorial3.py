import numpy as np
import cv2

# Number of camera you want to access
cap = cv2.VideoCapture(0)

while True:
    # Returns ret (if the capture worked properly) and frame (image itself in numpy array)
    ret, frame = cap.read()

    # Create a blank canvas to show four images
    image = np.zeros(frame.shape, np.uint8)
    cv2.imshow('Frame', image)

    # Wait up to one millisecond and if q is pressed, end showing the video
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()