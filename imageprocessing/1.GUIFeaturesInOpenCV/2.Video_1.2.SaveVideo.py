import numpy as np
import cv2

'''
Saving a Video
So we capture a video, process it frame-by-frame and we want to save that video. 

We create a VideoWriter object. We should specify the output file name (eg: output.avi). 
Then we should specify the FourCC code. Then number of frames per second (fps) 
and frame size should be passed. And last one is isColor flag. If it is True, encoder expect color frame, 
otherwise it works with grayscale frame.
'''

cap = cv2.VideoCapture(0)

fps = 30.0
capsize = (1280, 720)

# Define the codec and create VideoWriter Object
fourcc = cv2.VideoWriter_fourcc('m', 'p','4','v')
out = cv2.VideoWriter()
success = out.open('output.mov', fourcc, fps, capsize, True)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:        
        # frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()