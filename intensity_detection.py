import cv2
import numpy as np
import matplotlib.pyplot as plt
import os, sys
from intensity_histograms import ScrollableWindow

image = cv2.imread(r"C:\Users\shash\Downloads\AI_Data\1.5 mM h2o2\129.jpg") if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]) else cv2.imread(sys.argv[1])
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
reuse = image.copy()

blue = [
        np.array([110,50,50]), 
        np.array([130,255,255])
        ]

mask = cv2.inRange(hsv_img, blue[0], blue[1])
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

c = max(contours, key = cv2.contourArea)
x,y,w,h = cv2.boundingRect(c)
cropped = reuse[y:y+h, x:x+w]

row = 0
col = 0

colors = {0:[],1:[], 2:[]}

for row in cropped:
    for col in row:
        i=0
        for intensity in col:
            colors[i].append(intensity)
            i += 1

blue_intensities = colors[0]
red_intensities = colors[2]
green_intensities = colors[1]

mean_blue = np.mean(blue_intensities)
mean_green = np.mean(green_intensities)
mean_red = np.mean(red_intensities)


images={'Original': image,'cropped':cropped}
ScrollableWindow(images=images, figsize=(10,10))
