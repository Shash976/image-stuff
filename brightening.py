# import opencv library
import cv2
import numpy as np
import matplotlib.pyplot as plt


# read the image
img = cv2.imread('C:/Users/shash/Downloads/MnM.jpg',0)
cv2.imshow("Grayscale_image_modified.jpg",img)
cv2.waitKey()

for k in range(0,50):
    img[:,:] = np.where(img[:,:]* 1.03 < 255, (img[:,:] * 1.03).astype(np.uint8) , img[:,:])
    # show the results
    cv2.imshow('Updated',img)
    cv2.waitKey(40)
    
# save the image
cv2.destroyAllWindows()
# show the results
plt.imshow(cv2.cvtColor(img.astype('uint16'), cv2.COLOR_BGR2RGB))
plt.show()