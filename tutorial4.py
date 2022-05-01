import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    # Drawing a line
    # Coordinate system in OpenCV starts from left top as (x, y) = (0, 0)
    # Pass the source image, starting position, ending position, color, thickness
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)

    # Drawing a rectangle
    # Pass the source image, center points, radius, color, and line thicknes or -1 to fill
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)

    cv2.imshow('Frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()