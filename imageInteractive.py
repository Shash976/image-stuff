import cv2

def display_image_with_adjustment(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Create a window and display the image
    cv2.namedWindow('Image Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Image Display', image)

    while True:
        # Wait for a key press
        key = cv2.waitKey(1) & 0xFF

        # Check if the user pressed 'q' to quit
        if key == ord('q'):
            break

        ''''# Check if the user pressed '+' to increase size
        if key == ord('+'):
            # Get the current window size
            width, height = cv2.getWindowImageRect('Image Display')[2:4]

            # Increase the size by 10 pixels
            width += 10
            height += 10

            # Resize the window
            cv2.resizeWindow('Image Display', width, height)

        # Check if the user pressed '-' to decrease size
        if key == ord('-'):
            # Get the current window size
            width, height = cv2.getWindowImageRect('Image Display')[2:4]

            # Decrease the size by 10 pixels
            width -= 10
            height -= 10

            # Resize the window
            cv2.resizeWindow('Image Display', width, height)
        '''
        # Check if the user pressed the left arrow key to decrease width
        if key == ord('a'):
            width, height = cv2.getWindowImageRect('Image Display')[2:4]
            width -= 10
            print(f"{width} Going left")
            cv2.resizeWindow('Image Display', width, height)

        # Check if the user pressed the right arrow key to increase width
        if key == ord('d'):
            width, height = cv2.getWindowImageRect('Image Display')[2:4]
            width += 10
            print(f"{width} right arrow key pressed")
            cv2.resizeWindow('Image Display', width, height)

        # Check if the user pressed the up arrow key to increase height
        if key == ord('w'):
            width, height = cv2.getWindowImageRect('Image Display')[2:4]
            height -= 10
            print(f"{height} Up arrow key pressed")
            cv2.resizeWindow('Image Display', width, height)

        # Check if the user pressed the down arrow key to decrease height
        if key == ord('s'):
            width, height = cv2.getWindowImageRect('Image Display')[2:4]
            height += 10
            print(f"{height}  Down Arrow Key Pressed" )
            cv2.resizeWindow('Image Display', width, height)

    # Destroy the window and release resources
    cv2.destroyAllWindows()

# Usage example
image_path = r'C:/Users/shash/Downloads/MnM.jpg'
display_image_with_adjustment(image_path)
