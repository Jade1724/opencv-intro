import numpy as np
import cv2

# Load images as a greyscale (flag 0)
# Template image has to have the similar size with what is on the original image
img = cv2.imread('assets/soccer_practice.jpg', 0)
img= cv2.resize(img, (0, 0), fx=0.7, fy=0.7)
# template = cv2.imread('assets/ball.PNG', 0)
template = cv2.imread('assets/shoe.png', 0)
template = cv2.resize(template, (0, 0), fx=0.7, fy=0.7)

# Template shape of greyscale returns height and width while color image shape returns channel as the third value
h, w = template.shape

methods = [cv2.TM_CCOEFF,
          cv2.TM_CCOEFF_NORMED,
          cv2.TM_CCORR,
          cv2.TM_CCORR_NORMED,
          cv2.TM_SQDIFF,
          cv2.TM_CCOEFF_NORMED]

# Find out which method performs the best
for method in methods:
    img2 = img.copy()
    
    # Convolutional operation will slide the template on the original image
    # Returns a 2D array of number of times the template image can slide
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc)

    # For the following method, min_loc shows the best location, otherwise max_loc contains the best location
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
