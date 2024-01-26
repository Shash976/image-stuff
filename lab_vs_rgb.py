import cv2
import numpy as np

# Function to update the image based on trackbar values
def update_image(*args):
    # Retrieve the trackbar positions
    l = cv2.getTrackbarPos('L', 'Color Adjustments')
    a = cv2.getTrackbarPos('A', 'Color Adjustments')
    b = cv2.getTrackbarPos('B', 'Color Adjustments')
    r = cv2.getTrackbarPos('R', 'Color Adjustments')
    g = cv2.getTrackbarPos('G', 'Color Adjustments')
    blue = cv2.getTrackbarPos('B', 'Color Adjustments')

    # Convert LAB to RGB
    lab = np.array([[[l, a, b]]], dtype=np.uint8)
    rgb_from_lab = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)[0][0]

    # Update RGB trackbars if LAB is changed
    if args[0] in ['L', 'A', 'B']:
        cv2.setTrackbarPos('R', 'Color Adjustments', rgb_from_lab[2])
        cv2.setTrackbarPos('G', 'Color Adjustments', rgb_from_lab[1])
        cv2.setTrackbarPos('B', 'Color Adjustments', rgb_from_lab[0])

    # Create an image with the current color
    color = [blue, g, r]
    img[:] = color
    cv2.imshow('Color Adjustments', img)

# Create a black image and a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Color Adjustments')

# Create trackbars for color change
cv2.createTrackbar('L', 'Color Adjustments', 0, 255, lambda x: update_image('L'))
cv2.createTrackbar('A', 'Color Adjustments', 128, 255, lambda x: update_image('A'))
cv2.createTrackbar('B', 'Color Adjustments', 128, 255, lambda x: update_image('B'))
cv2.createTrackbar('R', 'Color Adjustments', 0, 255, lambda x: update_image('R'))
cv2.createTrackbar('G', 'Color Adjustments', 0, 255, lambda x: update_image('G'))
cv2.createTrackbar('B', 'Color Adjustments', 0, 255, lambda x: update_image('B'))

# Initialize the window with a black image
cv2.imshow('Color Adjustments', img)

# Wait until user press some key
cv2.waitKey(0)
cv2.destroyAllWindows()

