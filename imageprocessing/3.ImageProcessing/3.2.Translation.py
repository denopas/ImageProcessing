'''
# =============================================================================
# Translation
# =============================================================================
Translation is the shifting of object’s location.

You can take make it into a Numpy array of 
type np.float32 and pass it into cv2.warpAffine() function. 
See below example for a shift of (100,50):
'''

import cv2
import numpy as np

img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()