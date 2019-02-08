'''
John F. Canny tarafından 1986'da geliştirildi. Çok aşamalı bir algoritması bulunmaktadır.

1) Gürültü Azaltma (Noise Reduction)
Canny Kenar algılama algoritması çok hassas çalıştığından görüntüdeki istenmeyen gürültüleride 
kenar olarak algılayabilir.Bunun için yapılması gereken ilk adım "Gaussian Filtresi" uygulanarak 
resimdeki istenmeyen gürültülerin kaldırılmasıdır.

2) Görüntünün Yoğunluk Derecesini Bulma (Finding Intensity Gradient of the Image)
Filtre uygulanarak düzeltilmiş resim yatay yönde(Gx) ve dikey yönde (Gy)  türevler elde edilmesi 
için "Sobel" kerneliyle süzülür. 

3) Maksimum Bastırma (Non-maximum Suppression)
Eğim büyüklüğü ve yönü alındıktan sonra kenar oluşturmayan,istenmeyen pikselleri kaldırmak için 
görüntünün tam bir taraması yapılır.Bunun için her bir pikselin eğim yönündeki alanında yer 
maksimumluğu kontrol edilir.


4) Histerisiz Eşikleme (Hysteresis Thresholding)
Bu noktada tüm kenarların gerçekten kenar olup olmadığına karar verilir.Bunun için iki eşik 
değeri olan "minVal" ve "maxVal" ihtiyaç duyulur.Yoğunluk Gradiantı maxVal'dan daha büyük olan 
kenarlar kesinlikle kenar olarak kabul edilir.Yoğunluk Gradiantı minVal'den küçük olan kenarlar 
'''


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()