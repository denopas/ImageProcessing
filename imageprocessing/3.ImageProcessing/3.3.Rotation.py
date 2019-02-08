'''
# =============================================================================
# Rotation
# =============================================================================
Rotation of an image for an angle \theta is achieved by the transformation matrix 

To find this transformation matrix, OpenCV provides a function, cv2.getRotationMatrix2D. 
Check below example which rotates the image by 90 degree with respect to center without any scaling.
'''

import cv2
import numpy as np

img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()