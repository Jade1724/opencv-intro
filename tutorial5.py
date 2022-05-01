import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Convert BGR image to HSV to be usable to function to extract a color in OpenCV function
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Take the lower bound and upper bound of a color to be extracted
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Mask is a portion of an image. 
    # Returns a new image that only contains the color in the range
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply the mask to the image
    # Mask tell which pixels should be kept or discarded from the original image, blue then in, otherwise out
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    # Mask's pixel values are either 0 or 1
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


'''
Helper function to get a HSV value
As the first argument, need to pass an image represented as a numpy array

BGR_color = cv2.cvtColor([[[255, 0, 0]]], cv2.COLOR_BGR2HSV)
print(cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV))

'''
