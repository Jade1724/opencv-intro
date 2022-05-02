import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Give haarcascades an image with an arbitrary size
    # Pass the base image, scale factor (how much the image should be shrunk), and minNeighbors (how many neighbors each candidate rectangle should have to retain it) 
    # The smaller the scale factor, the more accurate but slower
    #  Optionally, pass minSize and maxSize of the rectangle.
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)

    # faces are rectangles
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        # Preparing for eye detector, getting area of face
        # ROI stands for region of interest
        roi_grey = grey[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # When detecting eyes, use grey scale image
        eyes = eye_cascade.detectMultiScale(roi_grey, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            # When drawing a rectangle, use color image since this is original size
            # The coordinates are relative to roi_grey, i.e., relative to face, so draw on roi_color rather than on frame
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 225, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()