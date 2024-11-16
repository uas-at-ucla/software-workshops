import numpy as np
import cv2


IMG_FOLDER = "../images/"

def get_coords(img_name):

    # read in the image from the image name
    img = cv2.imread(IMG_FOLDER + img_name)

    # resize the image
    img = cv2.resize(img, (400, 300))

    # insert code from week 1
