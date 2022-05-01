import numpy as np
import cv2

# Number of camera you want to access
cap = cv2.VideoCapture(0)

while True:
    # Returns ret (if the capture worked properly) and frame (image itself in numpy array)
    ret, frame = cap.read()

    # Get a width property and height property
    # Slice cannot accept float, so need to conver it to int
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Create a blank canvas to show four images
    image = np.zeros(frame.shape, np.uint8)
    # Shrink the image to one fourth size
    # The rotated dimension has to fit teh distination matrix segment in the image
    smaller_frame = cv2.resize(frame, (0, 0), fx = 0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame
    cv2.imshow('Frame', image)

    # Wait up to one millisecond and if q is pressed, end showing the video
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()