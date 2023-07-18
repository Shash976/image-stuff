import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

file_path = (r"C:/Users/shash/Downloads/jonny.jpg" if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]) else sys.argv[1])
img = cv2.imread(file_path)

def negative(image):
    img_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_negative = np.zeros(img_grayscale.shape, dtype=np.uint8)
    for y in range(len(img_grayscale)):
        for x in range(len(img_grayscale[y])):
            img_negative[y][x] = 255 - img_grayscale[y][x]
    return img_negative

if __name__ == "main":
    cv2.imshow('image', negative(img))
    cv2.waitKey(0)
    cv2.destroyAllWindows()