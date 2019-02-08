'''
# =============================================================================
# DRAWING FUNCTIONS
# =============================================================================
Learn to draw different geometric shapes with OpenCV
Functions : cv2.line(), cv2.circle() , cv2.rectangle(), 
cv2.ellipse(), cv2.putText() etc.

img : The image where you want to draw the shapes
color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. 
For grayscale, just pass the scalar value.
thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, 
it will fill the shape. default thickness = 1
lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. 
cv2.LINE_AA gives anti-aliased line which looks great for curves.
'''


import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)


#To draw a rectangle, you need top-left corner and bottom-right corner of rectangle. 
#This time we will draw a green rectangle at the top-right corner of image.
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#To draw a circle, you need its center coordinates and radius. 
#We will draw a circle inside the rectangle drawn above.
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)


#Drawing Ellipse
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#Drawing Polygon
pts = np.array([[10,5],[20,30],[70,20],[50,70]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))


'''
# =============================================================================
# ADDING TEXT
# =============================================================================
To put texts in images, you need specify following things.
Text data that you want to write
Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
Font type (Check cv2.putText() docs for supported fonts)
Font Scale (specifies the size of font)
regular things like color, thickness, lineType etc. For better look, lineType = cv2.LINE_AA is recommended.
'''
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Image', (10,500), font, 4, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
k = cv2.waitKey(0)
if (k == 27):         # wait for ESC key to exit
    cv2.destroyAllWindows()
