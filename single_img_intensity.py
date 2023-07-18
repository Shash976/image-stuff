import cv2
import numpy as np

channels = ['blue', 'green', 'red']
color_ranges = {
    'black': [
        np.array([0, 0, 0]),
        np.array([180, 255, 50])
        ],
    'white':[
        np.array([0, 0, 200]),
        np.array([180, 30, 255])
        ],
    'blue': [
        np.array([110,50,50]), 
        np.array([130,255,255])
        ],
    'green': [
        np.array([40, 50, 50]),
        np.array([80, 255, 255])
        ],
    'red': [
        np.array([0, 100, 100]),
        np.array([10, 255, 255])
        ],
    }


def color_detection(image, required_color):
    image = cv2.imread(image)
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    ranges = color_ranges[required_color]

    mask = cv2.inRange(hsv_img, ranges[0], ranges[1])
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(contours, key = cv2.contourArea)
    x,y,w,h = cv2.boundingRect(c)
    cropped = image[y:y+h, x:x+w]

    colors = {'Colors':[], 'blue':[],'green':[], 'red':[]}
    for row in cropped:
        for col in row:
            i=0
            for intensity in col:
                colors[channels[i]].append(intensity)
                i += 1
    colors['Colors'] = ['Value' for val in colors['blue']]        
    for channel in channels:
        mean = np.mean(colors[channel])
        colors[channel].append(mean)
    colors['Colors'].append('Mean')
    return colors