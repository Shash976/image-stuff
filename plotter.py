import cv2
import matplotlib.pyplot as plt
import numpy as np
from intensity_histograms import ScrollableWindow

def make_plot(rows, cols, images, hist=False):
    figsize = (cols*3 // 1, rows*2)
    if hist:
        ScrollableWindow(images=images, figsize=figsize)
    else:
        plt.figure(figsize=figsize)
        image_names = images.keys()
        for i, image_name in enumerate(image_names):
            image = images[image_name]
            plt.subplot(rows,cols, i+1)
            plt.title(image_name)
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) if len(image.shape) == 3 else plt.imshow(image, cmap='gray')
        plt.show()