from findmaxima2d import *
import numpy as np
import cv2
import matplotlib.pyplot as plt
from gif_reading import *

def getMaximaPoints(image,prominence = 100):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image,6)
    local_max = find_local_maxima(image)
    y,x,_ = find_maxima(image, local_max, prominence)
    img_height, img_width = image.shape

    break_loop = False

    while break_loop == False:
        x = x.tolist() if type(x) is not list else x
        y = y.tolist() if type(y) is not list else y
        no_x = [num for num in  range(img_width, img_width-11, -1)] + [num for num in range(0,11,1)]
        no_y = [num for num in  range(img_height, img_height-11, -1)] + [num for num in range(0,11,1)]
        for num in no_x:
            if num in x:
                i = x.index(num)
                x.pop(i)
                y.pop(i)
        for num in no_y:
            if num in y:
                i = y.index(num)
                x.pop(i)
                y.pop(i)

        if len(x) > 0:
            break_loop = True
        else:
            if prominence > 0:
                if prominence > 10:
                    prominence -= 5
                if prominence <= 10:
                    prominence -= 0.1
                y,x,_ = find_maxima(image, local_max, prominence)
            else:
                print("No Maxima")
                break_loop = True
    return prominence,y,x, image


if __name__ == "__main__":
    image_path = getVar(1, 'Image Path: ', r'C:/Users/shashg/Documents/Frames/3mM L+C 7mM H2o2 b.jpg')
    color_image = cv2.imread(image_path)
    image = cv2.cvtColor(color_image, 6)
    prominence, y, x, image = getMaximaPoints(image)
    print(f"Y: {y},\nX: {x},\nProminence: {prominence}")