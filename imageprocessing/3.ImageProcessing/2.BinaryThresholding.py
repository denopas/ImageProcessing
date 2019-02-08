'''
OpenCV Thresholding (Esikleme)

Giris olarak verilen goruntuyu ikili goruntuye cevirmek icin kullanilan bir yontemdir. 
Ikili goruntu (binary), goruntunun siyah ve beyaz olarak tanimlanmasidir. 
Morfolojik operatorler gibi goruntu uzerindeki gurultuleri azaltmak veya nesne belirlemek gibi 
farkli amaclar icin kullanilir. Giris olarak verilen goruntu uzerinde uygulanan thresholding 
tipine bagli olarak, pikselleri verilen esik degerine gore siyah ya da beyaz olarak gunceller.

OpenCV icerisindeki sik kullanilan threshold tipleri:

THRESH_BINARY
THRESH_BINARY_INV
THRESH_TRUNC
THRESH_TOZERO
THRESH_TOZERO_INV


cv2.threshold(src, thresh, maxval, type[, dst])

SRC; Giris dizisidir. Bu dizi gri tonlamali bir resim olmalidir.
TRESH; Esik ve Piksel degerlerini siniflandirmak icin kullanilir
MAXVAL; THRESH_BINARY ve THRESH_BINARY_INV esikleme turlerini maksimum degerde kullanmak icin yazilir.
TYPE; Threshold tipleri belirlenir.


'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Resim Gri Skalada Okunur#
img = cv2.imread('messi5.jpg',0)

# Resime Goruntu Esiklemeler uygulanir#
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

# Goruntu Ekraninin isimleri ve Degiskenleri Atanir#
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# Ayni Ekranda Thresholdlar Gozlenir#
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()