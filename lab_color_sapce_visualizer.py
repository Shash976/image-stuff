import cv2
import numpy as np

def update_image(*args):
    # Get current trackbar values
    l_value = cv2.getTrackbarPos('L', 'LAB Color Space Visualizer')
    a_value = cv2.getTrackbarPos('A', 'LAB Color Space Visualizer')
    b_value = cv2.getTrackbarPos('B', 'LAB Color Space Visualizer')

    # Create a blank image with the same size as the original image
    lab_image = np.zeros_like(original_image)

    # Set the LAB values based on the trackbar values
    lab_image[:, :, 0] = l_value
    lab_image[:, :, 1] = a_value
    lab_image[:, :, 2] = b_value

    # Convert LAB image back to BGR color space
    bgr_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

    # Show the updated image
    cv2.imshow('LAB Color Space Visualizer', bgr_image)

# Create a black image
original_image = np.zeros((512, 512, 3), dtype=np.uint8)

# Convert the image to LAB color space
lab_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)

# Create a window to display the LAB color space visualizer
cv2.namedWindow('LAB Color Space Visualizer')

# Create trackbars for each channel of the LAB color space
cv2.createTrackbar('L', 'LAB Color Space Visualizer', 0, 255, update_image)
cv2.createTrackbar('A', 'LAB Color Space Visualizer', 0, 255, update_image)
cv2.createTrackbar('B', 'LAB Color Space Visualizer', 0, 255, update_image)

# Show the original image
cv2.imshow('LAB Color Space Visualizer', original_image)

# Wait for key press to exit
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
