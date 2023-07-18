import cv2
import numpy as np
import os
import sys
import csv
import json

def getVar(argument, prompt, default):
    var = default
    if len(sys.argv) > argument:
        var = str(sys.argv[argument]).replace('"', '').strip()
        if os.path.exists(var):
            var = var
    else:
        x = str(input(f'{prompt} (Press Enter to use {default}): ')).replace('"', '').strip()
        if os.path.exists(str(x)):
            var =  x
    print(f"Using {var}")
    return var

COLOR_RANGES = {
        'black': [
            np.array([0, 0, 0]),
            np.array([180, 255, 50])
            ],
        'white':[
            np.array([0, 0, 200]),
            np.array([180, 30, 255])
            ],
        'blue': [
            np.array([0,0,18]), 
            np.array([179, 255,255])
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

def getCropped(required_color, image_path, i=False, crange=None):
    image = image_path if isinstance(image_path, np.ndarray) else cv2.imread(image_path)
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    ranges =  COLOR_RANGES[required_color] if not crange else [np.array(r) for r in json.loads(crange)]
    mask = cv2.inRange(hsv_img, ranges[0], ranges[1])
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        cropped = image[y:y+h, x:x+w]
    else:
        cropped = image
    if i:
        return cropped, image
    return cropped

def maxIntensity(frame, size=(12,13,12,13)):
    gray_img = cv2.cvtColor(frame, 6)
    g_max = np.max(gray_img)
    cords = np.where(gray_img == g_max)
    xd,xp,yd,yp = size
    finalMeans = getFinalMeans(frame, cords, xd, xp, yd, yp)
    while len(finalMeans) == 0:
        g_max = g_max-1
        rows, cols = np.where(gray_img==g_max)
        finalMeans = getFinalMeans(frame, finalMeans, rows, cols, xd, xp, yd, yp)

    maxVal = max([obj['mean'] for obj in finalMeans if str(obj['mean']).lower() != 'nan'])
    meanObj = [obj for obj in finalMeans if obj['mean'] == maxVal][0]
    return meanObj

def getFinalMeans(frame, cords, xd, xp, yd, yp):
    finalMeans = []
    for row,col in cords:
        row2, row1, col2, col1 = row+yp, row-yd, col+xp, col-xd
        region = frame[row1:row2, col1:col2]
        m = np.mean(region)
        if not np.isnan(m):
            finalMeans.append({'mean': m, 'region': region, 'x': [
                              col2, col1], 'y': [row2, row1]})
    return finalMeans

if __name__ == '__main__':
    folder = getVar(2, 'Folder Name', r'C:\Users\shash\Downloads\AI_Data\1.5 mM h2o2')
    required_color = getVar(3, 'Color', 'blue')
    images = []
    mean_intensities = []
    channels = ['blue', 'green', 'red']

    for content in os.listdir(folder):
        content_path = os.path.join(folder, content)
        if os.path.isdir(content_path):
            for img in os.listdir(content_path):
                image_path = os.path.join(content_path, img) if img.lower().endswith(('.jpg', 'png', 'jpeg')) else False
                if os.path.exists(image_path):
                    images.append(image_path)
        elif os.path.isfile(content_path) and content_path.lower().endswith(('.jpg', 'jpeg', 'png')):
            image_path = content_path
            images.append(image_path)

    for image_path in images:
        cropped = getCropped(required_color, image_path)

        mean = np.mean(cropped)
        mean_intensities.append({'Image': image_path, 'Mean Intensity': mean})

    keys = mean_intensities[0].keys()
    with open('C:/Users/shash/Downloads/record.csv', 'w+') as csv_file:
        dict_writer = csv.DictWriter(csv_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(mean_intensities)