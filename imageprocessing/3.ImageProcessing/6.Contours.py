'''
# =============================================================================
# KONTUR NEDİR?
# =============================================================================


Konturlar aynı renk ve yoğunluğa sahip olan tüm kesintisiz noktaları sınır boyunca 
birleştiren bir eğri olarak basitçe açıklanabilir.Konturlar şekil analizi,nesne algılama 
ve tanıma için çok yararlı bir araçtır.
Kontur bulunması istenirken daha doğru sonuç için binary(siyah-beyaz) formunda resim kullanılmalıdır.
FindContours yöntemiyle konturleri bulunan resim komple değişir orjinal halini bir daha kullanılamaz 
hale gelir. Bunun için resimi yazılımda yedeklemeniz gerekmektedir.
OpenCV'de kontur bulma işlemi siyah zeminde beyaz nesne bulmak gibidir.Unutulmamalıdır ki bulunması 
gereken nesne beyaz arka plan siyah olmalıdır.


cv2.findContours() işleminde konturlar bulunmuştur.Bu işleme kodda bakıldığı zaman 3 argümanın olduğu görülmüştür.

     1.Birinci argüman kontur bulunacak kaynak görüntüdür.
     2.İkinci argüman kontur alma modudur. 
     3.Üçüncü argüman ise kontur yaklaşım metodur.

Bu işlem sonucu görüntüyü konturu ve hiyerarşiyi ortaya çıkarır.
Koddaki "contours " değişkenine atanan bilgiler aslında görüntüdeki konturların pythondaki bir listesidir.
'''


import numpy as np
import cv2

im = cv2.imread('kare.png')
cv2.imshow('Orjinal resim',im)

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,1)
cv2.imshow('thresh',thresh)

img,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(im, contours,-1, (255,0,0), 1)
cv2.imshow('para',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


'''
# =============================================================================
# KONTURLARI ÇİZMEK?
# =============================================================================

Konturlar cv2.drawContours() fonksiyonu ile çizdirilir.Bu fonkisyonda ilk argüman kaynak görüntü,
ikinci argüman görüntüdeki konturların python listesi,üçüncü argüman konturların indeksi ,dördüncü 
argüman çizimin rengi ve beşinci argüman çizimin kalınlığıdır.

Bir resimdeki bütün konturları çizdirmek için;

img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

Tek bir kontur çizilmek istenirse örneğin 4. kontür;
cnt = contours[4]
img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

'''