import cv2
import numpy as np


backsub = cv2.createBackgroundSubtractorMOG2()
capture = cv2.VideoCapture("video.avi")

sayac=0


if capture:

  while True:

    ret, frame = capture.read()

    if ret:
        fgmask = backsub.apply(frame, None, 0.01)
        cv2.line(frame, (50, 0), (50, 300), (0, 255, 0), 2)
        cv2.line(frame, (70, 0), (70, 300), (0, 255, 0), 2)


        im,contours, hierarchy = cv2.findContours(fgmask.copy(), 
                                                  cv2.RETR_EXTERNAL,
                                                  cv2.CHAIN_APPROX_NONE)
        try: 
            hierarchy = hierarchy[0]
        except: 
            hierarchy = []
        for contour, hier in zip(contours, hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            if w > 40 and h > 40:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                if x>50 and x<70:
                    sayac+=1
                    print(sayac)

        cv2.putText(frame,"Araba: "+str(sayac), (220, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 0), 2)

        cv2.imshow("Takip", frame)
        cv2.imshow("Arka Plan Cikar", fgmask)



    key = cv2.waitKey(60)
    if key == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()

