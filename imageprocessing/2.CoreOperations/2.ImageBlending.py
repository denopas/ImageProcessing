'''
# =============================================================================
# Image Blending
# =============================================================================
This is also image addition, but different weights are given to images so that 
it gives a feeling of blending or transparency. 
'''

import cv2

img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv_logo.jpg')

# Difference of dimensions
print (img1.shape)
print (img2.shape)


piece1 = img1[180:280, 330:430]
print (piece1.shape)

new = cv2.addWeighted(piece1, 0.7, img2, 0.3, 0)

cv2.imshow('dst',new)
cv2.waitKey(0)
cv2.destroyAllWindows()