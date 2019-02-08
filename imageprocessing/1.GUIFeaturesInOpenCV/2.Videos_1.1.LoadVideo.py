import numpy as np
import cv2

'''
Playing Video from file
It is same as capturing from Camera, just change camera index with video file name. 
Also while displaying the frame, use appropriate time for cv2.waitKey(). 
If it is too less, video will be very fast and if it is too high, 
video will be slow (Well, that is how you can display videos in slow motion). 
25 milliseconds will be OK in normal cases.
'''

cap = cv2.VideoCapture('Video1.mov')

while(cap.isOpened()):
    ret, frame = cap.read()
    
    #print (cap.get(5)) #to display frame rate of video
    #print (cap.get(cv2.cv.CV_CAP_PROP_FPS))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #try COLORMAP_WINTER

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
