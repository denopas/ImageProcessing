'''
# =============================================================================
# MOUSE AS A PAINT BRUSH
# =============================================================================
'''
import cv2
import numpy as np


# =============================================================================
# STEP 1: SHOW EVENTS
# =============================================================================
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)


# =============================================================================
# STEP 2: SHOW DEMO
# =============================================================================
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()