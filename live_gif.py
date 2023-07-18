import cv2
import numpy as np
import matplotlib.pyplot as plt
from gif_reading import maxGIF
import plotter

vid = cv2.VideoCapture(0)

frames = []

while(True):
    ret,frame = vid.read()
    frames.append(frame)
    cv2.imshow('Recording', frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

image, cropped, meanObj = maxGIF(frames,8,8,8,8)
maxMean = meanObj['mean']
print(
        f'Final Cropped: {maxMean},Cropped: {np.mean(cropped)}, Original: {np.mean(image)}')
plotter.make_plot(
        1, 3, {'Original': image, 'Close Crop': cropped, 'Final': meanObj['area']})