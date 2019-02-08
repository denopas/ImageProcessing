# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 16:19:10 2018
@author: Akshay Narla
Working well with little error. Can't be tweaked by the user himself. 
The Person program can be copied here or be imported according to the requirement.
"""

import datetime
import numpy as np
import cv2 as cv
import Person

def nothing(x):
    pass

#video capture
var=cv.VideoCapture('ada.mov')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
EntranceCounter= 0
ExitCounter= 0
frame_width= var.get(3)
frame_height= var.get(4)
res = (frame_height * frame_width)

# Calculate the min and max size of the object
min_areaTH = res / 40
max_areaTH = res / 3

# Bottom line
bottom = int(3 * (frame_height / 5))
pt1 =  [0, bottom]
pt2 =  [frame_width, bottom]
pts_L1 = np.array([pt1, pt2], np.int32)
pts_L1 = pts_L1.reshape((-1, 1, 2))
bottom_color = (255, 0, 0)

# Top line
top = int(2*(frame_height / 5))
pt3 =  [0,top]
pt4 =  [frame_width, top]
pts_L2 = np.array([pt3, pt4], np.int32)
pts_L2 = pts_L2.reshape((-1, 1, 2))
top_color = (0, 0, 255)
persons = []
iteration_counter = 0
now_setting = [1,1,1,1,1]

ret, mask = var.read()
while (var.isOpened()):
    #if grabbed enter loop else break    
    ret, frame = var.read()
    if not ret:
        text = "No Video"
        break
    
    #adjusting frame size and blurring  
    absd =  cv.absdiff(frame, mask)
    gray= cv.cvtColor(absd,cv.COLOR_BGR2GRAY, cv.CV_8UC1)
    resize = cv.GaussianBlur( gray,(21,21),0)
    
    #background subtraction
    fgmask= fgbg.apply(resize)
    ret, th3 = cv.threshold(fgmask ,25,200,cv.THRESH_BINARY+cv.THRESH_OTSU)
    
    #smoothing and filling holes
    blur = cv.blur(th3,(5,5))
    kernel = np.ones((5,5),np.uint8)
    dil= cv.dilate( blur,kernel,iterations = 1)
   
    ret, th3 = cv.threshold(dil,0,50,cv.THRESH_BINARY+cv.THRESH_OTSU)
    #contours and tracking    
    im2, contours, hierarchy = cv.findContours(th3.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(im2, contours, -1, (200,50,50), 2)
    
    #grab all contours and draw rectangles and their centroids in original frame    
    for c in contours:
        area= cv.contourArea(c)
        if area> min_areaTH and area<max_areaTH:
             M = cv.moments(c)
             cx = int(M['m10']/M['m00'])
             cy = int(M['m01']/M['m00'])
             (x,y,w,h)= cv.boundingRect(c)
             new = True
             #tracking function
             for i in persons:        
                 # If the object is close to already detected
                 if abs(cx-i.getX()) <= w and abs(cy-i.getY()) <= h:
                     new = False
                    # Update coordinates for better tracking
                     i.updateCoords(cx,cy)
                    # Check crossing and update Counter
                     if i.UP(bottom,top) == True:
                         EntranceCounter += 1
                     elif i.DOWN(bottom, top) == True:
                         ExitCounter += 1
                 if i.timedOut():
                     index = persons.index(i)
                     persons.pop(index)
                     del i
             if new == True:
                 p = Person.MyPerson(cx, cy)
                 persons.append(p)
             cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
             cv.circle(frame, (cx,cy), 1, (0, 0, 255), 3)

    #display the output
    frame = cv.polylines(frame,[pts_L1], False, bottom_color, thickness = 1)
    frame = cv.polylines(frame,[pts_L2], False, top_color,thickness = 1)

    cv.putText(frame, "WentIn:"+format(str(EntranceCounter)),(10,20),cv.FONT_HERSHEY_SIMPLEX,.5,(0,0,0))
    cv.putText(frame, "WentOut:"+format(str(ExitCounter)),(10,35),cv.FONT_HERSHEY_SIMPLEX,.5,(0,0,0))
    cv.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
               (10, frame.shape[0] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.35, (255, 0, 0), 1)

    cv.putText(frame, "Inside:"+format(str(EntranceCounter-ExitCounter)),(10,50),cv.FONT_HERSHEY_SIMPLEX,.5,(255,255,255))
    cv.imshow('Panel', frame)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

var.release()
cv.waitKey(0)
cv.destroyAllWindows()