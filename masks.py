import cv2
import numpy as np
import matplotlib.pyplot as plt
import os,sys
from intensity_histograms import ScrollableWindow

img = cv2.imread('C:/Users/shash/Downloads/MnM.jpg') if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]) else cv2.imread(sys.argv[1])

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

color_ranges = {
    'black': [
        np.array([0, 0, 0]),
        np.array([180, 255, 50])
        ],
    'white':[
        np.array([0, 0, 200]),
        np.array([180, 30, 255])
        ],
    'blue': [
        np.array([110,50,50]), 
        np.array([130,255,255])
        ],
    'green': [
        np.array([40, 50, 50]),
        np.array([80, 255, 255])
        ],
    'red': [
        np.array([0, 100, 100]),
        np.array([10, 255, 255])
        ],
    }

images = {'Original':img}

for color, ranges in color_ranges.items():
    masked = cv2.inRange(hsv_img, ranges[0], ranges[1])
    images[color +' mask'] = masked

ScrollableWindow(images=images, figsize=(10,15))