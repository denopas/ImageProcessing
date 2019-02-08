import numpy as np
import cv2

'''
# =============================================================================
# CAPTURE VIDEO FROM CAMERA
# =============================================================================

Often, we have to capture live stream with camera. 
OpenCV provides a very simple interface to this.
To capture a video, you need to create a VideoCapture object. 
Its argument can be either the device index or the name of a video file. 
Device index is just the number to specify which camera. 
Normally one camera will be connected (as in my case). So I simply pass 0 (or -1). 
'''

cap = cv2.VideoCapture(0)

'''
cap.read() returns a bool (True/False). If frame is read correctly, it will be True. 
So you can check end of the video by checking this return value.
'''

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    '''
    Check the frame width and height by cap.get(3) and cap.get(4). 
    ret = cap.set(3,320)
    ret = cap.set(4,240)
    '''
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

