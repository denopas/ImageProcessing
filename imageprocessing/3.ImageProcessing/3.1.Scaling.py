'''
# =============================================================================
# Scaling
# =============================================================================
Scaling is just resizing of the image. OpenCV comes with a function cv2.resize() for this purpose. 
The size of the image can be specified manually, or you can specify the scaling factor. 
Different interpolation methods are used. Preferable interpolation methods are cv2.INTER_AREA for 
shrinking and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming. 
By default, interpolation method used is cv2.INTER_LINEAR for all resizing purposes. 
You can resize an input image either of following methods:
'''

import cv2
import numpy as np

img = cv2.imread('messi5.jpg')

#res = cv2.resize(img, None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#OR
height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()