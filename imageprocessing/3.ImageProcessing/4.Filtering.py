'''
# =============================================================================
# Filtreleme
# =============================================================================
Filtreleme operasyonu görüntü işlemede en çok gerçekleştirilen operasyonlardan biridir. 
Bu operasyonlar iki boyutlu görüntü dizimizdeki her piksel ve çevresindeki pikseller için tanımlanırlar. 
Filtreleme operasyonlarının büyük çoğunluğu bir pikselin ve çevresindeki komşu piksellerin uygun başka bir 
matrisle çarpılması ile gerçekleştirler. Bu matrise kernel ismi verilir.

# =============================================================================
# Motivasyon: "Gürültü"
# =============================================================================
Gerek ağırlıklı ortalama filtresinde gerek ortanca değer filtresinde amaç "genelde" 
bir resim üzerindeki gürültüyü yok etmektir. 
Gürültü bir sinyal bir kanal üzerinde aktarılırken, çevredeki etkenlerin altında oluşan istenmeyen değişimlerdir. 
Gürültü kavramına günlük hayattan bir örnek olarak telefon konuşmalarındaki cızırtı seslerini verebiliriz. 
'''


'''
# =============================================================================
# 1.Gaussian Noise(Gauss Dağılımına Sahip Gürültü)
# =============================================================================
Gauss gürültü -beyaz gürültü de denir- en çok uğraştığımız gürültü tipidir. 
Bir sinyal(ses veya görüntü) Gauss gürültüye sahip dendiğinde kastedilen, 
sinyalin olması gerekenden belirli bir Gauss fonksiyonu cinsinden bir hata payı ölçüsünde uzaklaşmış olduğudur. 
Bu hata payı gürültüyü oluşturan Gauss fonksiyonunun sigma(σ) parametresine bağlıdır. 
'''

'''
# =============================================================================
# Impulsive Noise(Ani Çıkış Yapan Gürültü)
# =============================================================================
Ani çıkış yapan gürültülerde sinyal belirli bir trende sahiptir fakat çok ani 
alakasız değişikliklere maruz kalmıştır. 
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('filter2.jpg')

blur1 = cv2.blur(img,(5,5))
blur2 = cv2.GaussianBlur(img,(5,5),0)
blur3 = cv2.medianBlur(img,5)


# Goruntu Ekraninin isimleri ve Degiskenleri Atanir#
titles = ['Original Image','Blur','GaussianBlur','medianBlur']
images = [img, blur1, blur2, blur3]

# Ayni Ekranda Thresholdlar Gozlenir#
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()