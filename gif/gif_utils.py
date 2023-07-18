import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

def getFrames(gif_path):
    gif = cv2.VideoCapture(gif_path)
    frames = []
    ret, frame = gif.read()
    while ret:
        ret, frame = gif.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def getMaxFrame(frames):
    frames = frames if type(frames) is not str else getFrames(frames) 
    max_intensity_projection = np.max(frames, axis=0)
    return max_intensity_projection

def getAdditions(frame_height, frame_width, row,col,xp,xd,yp,yd):
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
    return xp,xd,yp,yd

def getVar(argument, prompt, default):
    var = default
    if len(sys.argv) > argument:
        var = str(sys.argv[argument]).replace("'", "").replace('"', '').strip()
        if os.path.exists(var):
            var = var
    else:
        x = str(input(f'{prompt} (Press Enter to use {default}): ')).replace('"', '').strip()
        if os.path.exists(str(x)):
            var =  x
    if var == default:
        print("Using Default")
    return var