'''
 OpenCV'de iki şeklin veya iki konturun karşılaştırılmasını sağlayan cv2.matchShapes() kullanılır. 
 Bu komut benzerliği gösteren bir metriği döndürür.
 Sonuç ne kadar düşükse karşılaştırma işlemi bir o kadar daha iyi sonuç vermiş anlamına gelmektedir.
 
 cv2.matchShapes() komutu Hu-moments değerlerine dayanarak hesaplanır.
 
 3 farklı resmi kıyaslayalım giriş resimleri ise 2 farklı yıldız ve bir dikdörtgen olsun. 
 önce aynı resmi birbiriyle kıyaslayarak birebir aynılıkta hangi değeri verdiğini gözleyelim.
 Daha sonra ise diğerlerini birbiriyle gözleyelim
 
'''

import cv2
import numpy as np

img1 = cv2.imread('yildiz.jpg',0)
img2 = cv2.imread('yildiz.jpg',0)
#img2 = cv2.imread('dikdortgen.jpg',0)

ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
img,contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
img1,contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print (ret)