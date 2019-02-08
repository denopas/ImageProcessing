import numpy as np
import cv2
from matplotlib import pyplot as plt

'''
Using Matplotlib
Matplotlib is a plotting library for Python which gives you wide variety of plotting methods. 
'''

img = cv2.imread('messi5.jpg',0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.show()