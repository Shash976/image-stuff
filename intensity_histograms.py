import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
import os
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from edge_detection import auto_detection
from image_negatives import negative


def get_rgb_hist(img):
    rgb_channels = ['r','g', 'b']
    histograms = {}
    hist_size = [256] 
    hist_range = [0,256]
    for i, color in enumerate(rgb_channels):
        histogram = cv2.calcHist([img],[i], None, hist_size, hist_range)
        histograms[color] = histogram
        plt.plot(histogram, color=color)
        plt.title(color)
        plt.xlim([0, 256])
    return histograms

def plot_image(images={}, figsize=(20,30)):
    fig, axes = plt.subplots(nrows=len(images), ncols=2, figsize=figsize)
    for ax, (title, image) in zip(axes, images.items()):
        ax[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) if len(image.shape) > 2 else ax[0].imshow(image, cmap='gray')
        ax[0].set_title(title)
        if len(image.shape) == 3:
            rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            for color, histogram in get_rgb_hist(rgb_img).items():
                ax[1].plot(histogram, color=color)
            ax[1].set_title('RGB Histogram')
        else:
            ax[1].set_title('Gray')
            ax[1].plot(cv2.calcHist([image],[0], None, [256], [0,256]))

    fig.tight_layout()
    return fig


class ScrollableWindow(QtWidgets.QMainWindow):
    def __init__(self, images, figsize=(20,30)):
        self.qapp = QtWidgets.QApplication([])
        QtWidgets.QMainWindow.__init__(self)

        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QtWidgets.QVBoxLayout())
        self.widget.layout().setContentsMargins(0,0,0,0)
        self.widget.layout().setSpacing(0)

        self.fig = plot_image(images,figsize=figsize)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.scroll = QtWidgets.QScrollArea(self.widget)
        self.scroll.setWidget(self.canvas)

        self.nav = NavigationToolbar(self.canvas, self.widget)
        self.widget.layout().addWidget(self.nav)
        self.widget.layout().addWidget(self.scroll)

        self.show()
        exit(self.qapp.exec_())


if __name__ == "__main__":
    test_image = np.array([[000,000,255,000,000,000],
                           [000,000,255,000,000,000],
                           [255,255,255,255,255,255],
                           [000,000,255,000,000,000],
                           [000,000,255,000,000,000],
                           [000,000,255,000,000,000]])

    img = cv2.imread('C:/Users/shash/Downloads/MnM.jpg') if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]) else cv2.imread(sys.argv[1])

    noise = np.random.normal(0,15,(img.shape)).astype(np.uint8)

    kernels = {
        'sharpen' : np.array([[-1,-1,-1],
                             [-1,9,-1],
                             [-1,-1,-1]]),
        'sobel' : np.array([[-1,0,1],
                            [-2,0,2],
                            [-1,0,1]])                    
        }

    noisy_img = img+noise

    kernel = kernels['sharpen'] if len(sys.argv) < 3 else kernels[sys.argv[2]]

    filtered_img = cv2.filter2D(img, -1, kernel)

    
    images={
    'Original Image': img,
    'Noisy': noisy_img,
    'Gray': cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
    'Negative': negative(img),
    'Sharpened': cv2.filter2D(img, -1, kernels['sharpen']),
    'Sobel': cv2.filter2D(img, -1, kernels['sobel']),
    'Sobel on Gray': cv2.filter2D(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), -1, kernels['sobel']),
    'Equalized': cv2.equalizeHist(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)),
    'Equalized Colored': cv2.merge([cv2.equalizeHist(ch) for ch, color in zip(cv2.split(img), ['B','G', 'R'])]),
    'Edge Detection': auto_detection(img)
    }
    a = ScrollableWindow(images)

