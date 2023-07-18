import cv2
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors, pyplot as plt

img = cv2.imread(r'C:/Users/shash/Downloads/MnM.jpg')
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

r,g,b = cv2.split(rgb_img)


h,s,v = cv2.split(hsv_img)
fig = plt.figure()
axis = fig.add_subplot(1,1,1, projection='3d')

pixel_colors = rgb_img.reshape((rgb_img.shape[0]*rgb_img.shape[1], 3))
norm = colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()

axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors = pixel_colors)
axis.set_xlabel("Hue")
axis.set_ylabel('Saturation')
axis.set_zlabel("Value")
plt.show()