'''
# =============================================================================
# Image ROI - (Region of Image)
# =============================================================================

Sometimes, you will have to play with certain region of images. For eye detection in images, 
first perform face detection over the image until the face is found, then search within the face 
region for eyes. This approach improves accuracy (because eyes are always on faces) and performance 
(because we search for a small area).

'''

import cv2
import numpy as np

img = cv2.imread('messi5.jpg')

# ROI using Numpy indexing. Here we select the ball and copy it to another region in the image:
ball = img[280:340, 330:390]


# Show ball

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', ball)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Copy and show ball in picture


img[273:333, 100:160] = ball

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
