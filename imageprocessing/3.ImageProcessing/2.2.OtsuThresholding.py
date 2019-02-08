'''
# =============================================================================
# Otsu Eşik Belirleme
# =============================================================================

Normalde bir gri görüntüyü ikili biçime çevirmek için izlenecek yöntem oldukça basittir. 
Bir eşik değeri belirlenir ve bu eşik değerin üzerindeki renkler beyaza, altındaki renkler
siyaha dönüştürülür. Ancak tüm görüntüler aynı niteliklere sahip değildir. 
Sabit bir eşik değeri tüm görüntüler üzerinde kabul edilebilir sonuçlar üretemeyebilir. 
Dolayısıyla eşik değerin, resmin renk dağılımına uygun olarak belirlenmesini sağlayacak bir yönteme ihtiyaç duyulur.

Otsu metodu, gri seviye görüntüler üzerinde uygulanabilen bir eşik tespit yöntemidir. 
Bu metod kullanılırken görüntünün arka plan ve ön plan olmak üzere 
iki renk sınıfından oluştuğu varsayımı yapılır. Daha sonra tüm eşik değerleri için 
bu iki renk sınıfının sınıf içi varyans değeri hesaplanır. 
Bu değerin en küçük olmasını sağlayan eşik değeri, optimum eşik değeridir.
'''

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)

# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()