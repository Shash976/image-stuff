import numpy as np
import cv2
import matplotlib.pyplot as plt
from intensity_histograms import ScrollableWindow

file_path = r'C:/Users/shash/Downloads/MnM.jpg'
image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
img = cv2.medianBlur(image, 5)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)


