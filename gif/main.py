from maxima_main import *
from gif_utils import *
import numpy as np
import cv2
import matplotlib.pyplot as plt

path = getVar(1, "GIF", r"C:/Users/shashg/Documents/gifs/3mM L+C 7mM H2o2 b.gif" ).strip()
gif_path = path

maxFrame = getMaxFrame(gif_path)
'''----------------------------------------------------x----------------------------------------------------------x---------------------------'''
testImg = maxFrame.copy()
testImg[:,:,2] = np.zeros((testImg.shape[0], testImg.shape[1]))
ranges =  [np.array([112,0,0]) ,np.array([115,255, 255])]
mask = cv2.inRange(cv2.cvtColor(testImg,cv2.COLOR_BGR2HSV), ranges[0], ranges[1])
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
c = max(contours, key = cv2.contourArea)
x,y,w,h = cv2.boundingRect(c)
'''------------------------------------------------------x-------------------------------------------------------x------------------'''
cropped_image = maxFrame[y:y+h, x:x+w]

prominence, y_cords,x_cords, frame = getMaximaPoints(cropped_image)
xp,xd,yp,yd = 12,12,12,12
regions = []
for x, y in zip(x_cords, y_cords):
    frame_height, frame_width = frame.shape
    xp,xd,yp,yd = getAdditions(frame_height, frame_width, y, x, xp,xd,yp,yd)
    region = maxFrame[y-yd:y+yp, x-xd:x+xp]
    mean = np.mean(region)
    regions.append({"mean":mean, 'x':x,'y':y,"x-cords":[x-xd, x+xp], "y-cords":[y-yd, y+yp], "region":region })
maxMean = max([obj['mean'] for obj in regions])
maxObj = [obj for obj in regions if obj['mean'] == maxMean][0]

print(f"Mean: {maxMean}\nX:{maxObj['x']+x} Y:{maxObj['y']+y} \nProminenece {prominence}")
x = maxObj['x']+x
y = maxObj['y']+y
plt.imshow(cv2.cvtColor(maxFrame, 4))
plt.plot(x,y,'ro')
plt.show()