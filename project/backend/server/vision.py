import numpy as np
import cv2


IMG_FOLDER = "../images/"

def get_coords(img_name):

    # read in the image from the image name
    img = cv2.imread(IMG_FOLDER + img_name)

    # resize the image
    img = cv2.resize(img, (400, 300))

    # insert code from week 1
    blurred = cv2.GaussianBlur(img, (9, 9), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    lower_red1 = (0, 70, 0)
    upper_red1 = (5, 255, 255)

    lower_red2 = (165, 70, 0)
    upper_red2 = (180, 255, 255)

    # Create two masks for the red color in both ranges
    red_mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    red_mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Combine the two masks using bitwise OR
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)

    M = cv2.moments(largest_contour)
    if M['m00'] != 0:
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])
        x_dim = np.shape(red_mask)[1]
        y_dim = np.shape(red_mask)[0]
        x_dist = cX - x_dim/2
        y_dist = cY - y_dim/2
    else:
        x_dist, y_dist = 0, 0
    return x_dist, y_dist