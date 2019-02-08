'''
# =============================================================================
# Changing Color-space
# =============================================================================

There are more than 150 color-space conversion methods available in OpenCV. 
But we will look into only two which are most widely used ones, BGR <-> Gray and BGR <-> HSV.

For color conversion, we use the function cv2.cvtColor(input_image, flag) 
where flag determines the type of conversion.

For BGR <-> Gray conversion we use the flags cv2.COLOR_BGR2GRAY. 
Similarly for BGR <-> HSV, we use the flag cv2.COLOR_BGR2HSV
'''

import cv2
import numpy as np

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print (flags)


'''
# =============================================================================
# Object Tracking
# =============================================================================
Now we know how to convert BGR image to HSV, we can use this to extract a colored object. 
In HSV, it is more easier to represent a color than RGB color-space. 
In our application, we will try to extract a blue colored object. 

So here is the method:

1. Take each frame of the video
2. Convert from BGR to HSV color-space
3. We threshold the HSV image for a range of blue color
4. Now extract the blue object alone, we can do whatever on that image we want.

'''

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()



