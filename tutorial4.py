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

    # Drawing a circle
    # Pass the source image, center position, radius, color, and line thickness or -1 to fill
    img = cv2.circle(img, (300, 300), 60, (0, 0, 225), -1)

    # Drawing a text
    # Specify a font as the first step
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Drawing text coordinate is based on bottom left hand corner
    # Pass the source image, text to render, position, font, font scale, color, thickness, lineType. OpenCV recommends passing cv2.LINE_AA
    img = cv2.putText(img, 'Tim is Great!', (100, height - 10), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()