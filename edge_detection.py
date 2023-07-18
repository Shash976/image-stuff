import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import sys


def auto_detection(image, sigma=0.33): # sigma = 0.33 as the image is divided in 3 ranges - below min threshold, above max threshold and the range to be considered for detection. hence sgma =0.33 as it signifies 33% roughly equal to 100/3
    img_median = np.median(image)
    lower_thresh = int(max(0, (1.0 - sigma)*img_median))
    upper_thresh = int(min(255, (1.0 + sigma)*img_median))
    return cv2.Canny(image, lower_thresh, upper_thresh)

if __name__ == "main":
    file_path = (r"C:/Users/shash/Downloads/MnM.jpg" if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]) else sys.argv[1])

    img = cv2.imread(file_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_img, (5,5), 0)
    
    wide = cv2.Canny(blurred, 50, 200)
    mid = cv2.Canny(blurred, 30, 150)
    tight = cv2.Canny(blurred, 210, 250)

    cv2.imshow('detected', auto_detection(blurred))
    cv2.waitKey(0)
    cv2.destroyAllWindows()