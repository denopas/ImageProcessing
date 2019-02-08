'''
Basics
Background subtraction is a major preprocessing steps in many vision based applications. 
For example, consider the cases like visitor counter where a static camera takes the number of 
visitors entering or leaving the room, or a traffic camera extracting information about the vehicles etc. 
In all these cases, first you need to extract the person or vehicles alone. 

Technically, you need to extract the moving foreground from static background.

If you have an image of background alone, like image of the room without visitors, 
image of the road without vehicles etc, it is an easy job. Just subtract the new image from the background. 
You get the foreground objects alone. But in most of the cases, you may not have such an image, 
so we need to extract the background from whatever images we have. It become more complicated 
when there is shadow of the vehicles. Since shadow is also moving, simple subtraction will mark that also as foreground. 
It complicates things.

Several algorithms were introduced for this purpose.
'''


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()