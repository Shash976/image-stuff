import cv2
import numpy as np
import time
from gif.detect_intensity import getVar

def nothing(x):
    pass

def resize_window(event, x, y, flags, param):
    global window_size
    if event == cv2.EVENT_LBUTTONDOWN and window_size < 2.0:
        window_size += 0.1
    elif event == cv2.EVENT_RBUTTONDOWN and window_size > 0.2:
        window_size -= 0.1

cv2.namedWindow("Trackbars")

x_size = 0.5
y_size = 0.5

# Initialize the trackbars with appropriate initial values
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

# Load the image
img_path = getVar(1, 'Image', r"C:\Users\shashg\Documents\AI_Data\1.5 mM h2o2\128_cropped.jpg")
image = cv2.imread(img_path)

key_actions = {
    ord('w'): (0, -10, "Up arrow key pressed"),
    ord('a'): (-10, 0, "Going left"),
    ord('s'): (0, 10, "Down Arrow Key Pressed"),
    ord('d'): (10, 0, "right arrow key pressed")
}

frame_keys = {
    ord('i'): (0, -0.1, "Images Up arrow key pressed"),
    ord('j'): (-0.10, 0, "Images Going left"),
    ord('k'): (0, 0.10, "Images Down Arrow Key Pressed"),
    ord('l'): (0.10, 0, " Images right arrow key pressed")
}

while True:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Get the new values of the trackbars in real-time as the user changes them
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
    
    # Set the lower and upper HSV range according to the values selected by the trackbars
    lower_range = np.array([l_h, l_s, l_v])
    upper_range = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    l = []
    rows, cols = np.where(mask==255)
    for row, col in zip(rows,cols):
        l.append(image[row][col])
    l = np.array(l)
    mean = np.mean(l)
    print(mean, len(l))
    time.sleep(500)
    
    #contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    #
    #for contour in contours:
    #    x, y, w, h = cv2.boundingRect(contour)
    #    if w >= 15 and h >= 15:
    #        cropped = image[y:y+h, x:x+w]
    #        cv2.rectangle(i, (x, y), (x + w, y + h), (0, 255, 0), 1)
    #        cv2.putText(i, f"{str(round(np.mean(cropped), 2))} {y,h,x,w}", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
    #
    
    i = image.copy()
    res = cv2.bitwise_and(image, image, mask=mask)
    stacked = np.hstack((mask_3, i, res))
    key = cv2.waitKey(1)
    resized_stacked = cv2.resize(stacked, None, fx=x_size, fy=y_size)
    cv2.imshow('Trackbars', resized_stacked)
    
    if key:
        if key in key_actions.keys():
            width, height = cv2.getWindowImageRect('Trackbars')[2:4]
            width_change, height_change, message = key_actions[key]
            width += width_change
            height += height_change
            print(f"{message} - Width: {width}, Height: {height}")
            cv2.resizeWindow('Trackbars', width, height)
        elif key in frame_keys.keys():
            x_change, y_change, message = frame_keys[key]
            x_size += x_change
            y_size += y_change
            print(f"{message}")
            resized_stacked = cv2.resize(stacked, None, fx=x_size, fy=y_size)
            cv2.imshow('Trackbars', resized_stacked)
    if key == 27:
        break

cv2.destroyAllWindows()