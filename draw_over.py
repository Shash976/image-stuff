import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

file_path = (r"C:/Users/shash/Downloads/MnM.jpg" if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]) else sys.argv[1])

image = cv2.imread(file_path)

left, right, upper, lower = [150, 300, 150, 300] if len(sys.argv) < 3 or not type(sys.argv[2]) != list else sys.argv[2]

start_point, end_point = (left, upper),(right, lower)
image_draw = np.copy(image)
cv2.rectangle(image_draw, pt1=start_point, pt2=end_point, color=(0, 255, 0), thickness=3) 
plt.figure(figsize=(5,5))
plt.imshow(cv2.cvtColor(image_draw, cv2.COLOR_BGR2RGB))
plt.show()