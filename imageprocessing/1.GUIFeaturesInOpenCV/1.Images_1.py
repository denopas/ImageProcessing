'''
# =============================================================================
# READ AN IMAGE
# =============================================================================
Use the function cv2.imread() to read an image. The image should be in the working directory or a full path of 
image should be given.

Second argument is a flag which specifies the way image should be read.

cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
'''

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)



'''
# =============================================================================
# DISPLAY AN IMAGE
# =============================================================================
Use the function cv2.imshow() to display an image in a window. The window automatically fits to the image size.

First argument is a window name which is a string. second argument is our image. 
You can create as many windows as you wish, but with different window names.

cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. 
The function waits for specified milliseconds for any keyboard event. If you press any key in that time, 
the program continues. 
If 0 is passed, it waits indefinitely for a key stroke. It can also be set to detect specific key strokes like, 
if key a is pressed etc which we will discuss below.

cv2.destroyAllWindows() simply destroys all the windows we created. If you want to destroy any specific window, 
use the function cv2.destroyWindow() where you pass the exact window name as the argument.

'''

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# =============================================================================
# WRITE AN IMAGE
# =============================================================================

Use the function cv2.imwrite() to save an image.

First argument is the file name, second argument is the image you want to save.
'''

#Bu satırı doğru yere taşı?
cv2.imwrite('messigray.png',img)
