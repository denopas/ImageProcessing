'''

# =============================================================================
# Making Borders for Images (Padding)
# =============================================================================

Something like a photo frame, you can use cv2.copyMakeBorder() function. 
But it has more applications for convolution operation, zero padding etc. 

This function takes following arguments:

    src - input image
    top, bottom, left, right - border width in number of pixels in corresponding directions
    borderType - Flag defining what kind of border to be added. It can be following types:
        cv2.BORDER_CONSTANT - Adds a constant colored border. 
        cv2.BORDER_REFLECT - Border will be mirror reflection of the border elements
        cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Same as above, but with a slight change
        cv2.BORDER_REPLICATE - Last element is replicated throughout
        cv2.BORDER_WRAP - it will look like this : cdefgh|abcdefgh|abcdefg
value - Color of border if border type is cv2.BORDER_CONSTANT

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = cv2.imread('opencv_logo.jpg')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()