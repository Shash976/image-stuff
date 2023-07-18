import cv2
import os
import sys
from intensity_histograms import ScrollableWindow

file_path = (r"C:/Users/shash/Downloads/MnM.jpg" if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]) else sys.argv[1])
img = cv2.imread(file_path)

blurred_gray = cv2.GaussianBlur(img, (3,3), 0.1,0.1)

ddepth = cv2.CV_32F
# Applys the filter on the image in the X direction
grad_x = cv2.Sobel(src=blurred_gray, ddepth=ddepth, dx=1, dy=0, ksize=3)
grad_y = cv2.Sobel(src=blurred_gray, ddepth=ddepth, dx=0, dy=1, ksize=3)

abs_grad_x = cv2.convertScaleAbs(grad_x) #data form suitable for showing image (0 to 255)
abs_grad_y = cv2.convertScaleAbs(grad_y) #data form suitable for showing image (0to 255)

grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

images = {
    'At X' : abs_grad_x,
    'At Y' : abs_grad_x,
    'Weighted' : grad
}

ScrollableWindow(images=images, figsize=(10,10))