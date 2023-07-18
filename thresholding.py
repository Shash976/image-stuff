# openCV library 
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# reading the image from the same directory
img = cv.imread('C:/Users/shash/Downloads/MnM.jpg', cv.IMREAD_GRAYSCALE)

# threshold with the simple binary method
ret1,simp_thresh = cv.threshold(img,127,255,cv.THRESH_BINARY)

# Otsu's threshold without any filter
ret2,simp_thresh_otsu = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# Otsu's threshold using Gaussian filtering
blur = cv.GaussianBlur(img,(5,5),0)
ret3,otsu_filter = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print(ret1, ret2, ret3)
# histogram of images
images = [img, 0, simp_thresh,
          img, 0, simp_thresh_otsu,
          blur, 0, otsu_filter]

titles = ['Original Image','Histogram','Global Thresholding (v=127)',
          'Original Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

# using a loop to visualize the different types of methods
def getThreeColPlots(titles, images):
    plt.figure(figsize=(10,6))
    rows = len(titles)//3
    for i in range(rows):
        plt.subplot(rows,3,i*3+1),plt.imshow(images[i*3],'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
        plt.subplot(rows,3,i*3+2),plt.hist(images[i*3].ravel(),256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        plt.subplot(rows,3,i*3+3),plt.imshow(images[i*3+2],'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

getThreeColPlots(titles, images)
plt.show()