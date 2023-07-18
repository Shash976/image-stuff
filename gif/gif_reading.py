import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
from gif_utils import *

def grayMaxIntensity(gif, size=(12,12,12,12)):
    frame = gif if type(gif) is np.ndarray else getMaxFrame(gif)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    g_max = np.max(gray_img)
    finalMeans = []
    rows, cols = np.where(gray_img == g_max)
    xd,xp,yd,yp = size
    finalMeans = getGrayFinalMeans(frame, finalMeans, rows, cols, xd, xp, yd, yp)
    while len(finalMeans) == 0:
        g_max = g_max-1
        rows, cols = np.where(gray_img==g_max)
        finalMeans = getGrayFinalMeans(frame, finalMeans, rows, cols, xd, xp, yd, yp)

    maxVal = max([obj['mean'] for obj in finalMeans if str(obj['mean']).lower() != 'nan'])
    meanObj = [obj for obj in finalMeans if obj['mean'] == maxVal][0]
    meanObj['max'] = g_max
    return meanObj

def getGrayFinalMeans(frame, finalMeans, rows, cols, xd, xp, yd, yp):
    frame_height,frame_width,_ = frame.shape
    for row, col in zip(rows,cols):
        if row+yp > frame_height:
            yd += row+yp-frame_height
            yp = frame_height - row
        elif row - yd < 0:
            yp += abs(row-yd)
            yd = row
        if col+xp > frame_width:
            xd += col+xp-frame_width
            xp = frame_width - col
        elif col-xd < 0:
            xp += abs(row-xd)
            xd = col
        row2, row1, col2, col1 = row+yp, row-yd, col+xp, col-xd
        region = frame[row1:row2, col1:col2]
        m = np.mean(region)
        if not np.isnan(m):
            finalMeans.append({'mean': m, 'region':region, 'x': [
                              col2, col1], 'y': [row2, row1]})
    return finalMeans

def calcGIFByROI(gif):
    frame = gif if type(gif) is np.ndarray else getMaxFrame(gif) 
    regions = getRegionsOfInterest(frame)
    mean = max([region['mean'] for region in regions])
    meanObj = [obj for obj in regions if obj['mean'] == mean][0]
    return (meanObj, frame)

def getRegionsOfInterest(frame):
    regions = []
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    for hue in range(90, 131, 3):
        for saturation in range(20, 255, 5):
            ranges =  [np.array([0,0,0]) ,np.array([hue, saturation, 255])]
            mask = cv2.inRange(hsv_img, ranges[0], ranges[1])
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            #print(f"Hue: {hue} Saturation:{saturation}")
            if contours:
                #print('\t Contours Found')
                i = frame.copy()
                for contour in contours:
                    x,y,w,h = cv2.boundingRect(contour)
                    if h >=10 and w >=10:
                        #print(f"\t \t Suitable Contour Found at {x,y,w,h}")
                        cropped = frame[y:y+h, x:x+w]
                        regions.append({'mean': np.mean(cropped) ,'x':[x, x+w], 'y':[y,y+h], 'hue':hue, 'saturation':saturation, 'region':cropped})
                        #print(f"\t \t \t Added contour to regions Mean = {np.mean(cropped)}")
    return regions

if __name__ == "__main__":
    gif = getVar(1, "GIF path ", r"C:\Users\shashg\Documents\gifs\24 deg FG 5mg_ml c.gif")
    roi_mean_props, frame = calcGIFByROI(gif)
    gray_mean_props = grayMaxIntensity(gif)
    print(f'Gray:\n \t {gray_mean_props["mean"]}\nROI: \n \t {roi_mean_props["mean" ]}')
