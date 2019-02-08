# import the necessary packages
import numpy as np
import cv2

isRGB = True
# load the image
image = cv2.imread("muslera.png")

# define the list of boundaries

if (isRGB):
    boundaries = [
        ([17, 10, 100], [50, 60, 200]),
        ([25, 146, 190], [100, 180, 250])]
    converted = image
else: #HSV
    boundaries = [
        ([160, 0, 0], [180, 255, 255]),
        ([20, 0, 0], [30, 255, 255])]
    converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
     
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(converted, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
    
    cv2.imshow("images", output)
    cv2.waitKey(0)
    
'''
HSV renk uzayında kırmızı rengi ayırt etmek için ise Saturation ve Value değerlerinin ne olduğuna bakmaksızın 
sadece Hue değerine bakarak filtreleme yapabiliriz!. Kırmızı için renk değeri 160-180 arası bölgeyi, 
sarı için ise 20-30 arasındaki renk değerlerini filtreleyerek istediğimiz sonuca ulaşabiliriz.  
Böylece Hem daha kolay hem de daha hassas sonuç elde ediyoruz..
'''

'''
How to find HSV values to track?
It is very simple and you can use the same function, cv2.cvtColor(). 
Instead of passing an image, you just pass the BGR values you want. 
For example, to find the HSV value of Green, try following commands in Python terminal:

>>> green = np.uint8([[[0,255,0 ]]])
>>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
>>> print hsv_green
[[[ 60 255 255]]]

Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively. 
Apart from this method, you can use any image editing tools like GIMP or any online converters 
to find these values, but don’t forget to adjust the HSV ranges.
'''
    