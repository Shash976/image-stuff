import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from pil_funcs import plot_image

test_image = np.array([[0,0,255,0,0,0],
                       [0,0,255,0,0,0],
                       [255,255,255,255,255,255],
                       [0,0,255,0,0,0],
                       [0,0,255,0,0,0],
                       [0,0,255,0,0,0]])

img = test_image if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]) else cv2.imread(sys.argv[1])


'''
sobel_kernel = np.array([[-1,0,1],
                         [-2,0,2],
                         [-1,0,1]])
'''


noise = np.random.normal(0,15,(img.shape)).astype(np.uint8)
noisy_img = img + noise
kernel_sharp = np.array([[-1,-1,-1],
                         [-1,9,-1],
                         [-1,-1,-1]])

sharpened = cv2.filter2D(img, -1, kernel_sharp)

plot_image(image_1=cv2.cvtColor(img, cv2.COLOR_BGR2RGB), image_2=cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB),title_1="Orignal",title_2="Sharpened Image")