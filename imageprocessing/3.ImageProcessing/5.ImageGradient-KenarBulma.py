'''
Bir görsel üzerinde X ve Y eksenleri doğrultusunda çeşitli filtreler kullanılarak 
görsel gradyanları (image gradients) bulunabilir. Bu iş için en çok kullanılan filtreler 

- Robinson, 
- Sobel, 
- Kirsch, 
- Scharr filtreleridir.

OpenCV üzerinde bir görsel için herhangi bir kernel yürütmek istediğimizde filter2D fonksiyonunu kullanırız. 
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
Robinson Kerneli
Robinson matrisi yönlü gradyanları bulmak için akla gelen en temel kerneldir.
'''
kernel_x_Robinson = np.array(
    [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ]
)

'''
Sobel Kerneli
Sobel genel kullanımda sıkça kendine yer edinmiş bir filtredir.
'''
kernel_x_Sobel = np.array(
    [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]
)


'''
Kirsch Kerneli
Kirsch köşe bulma algoritmalarında sıkça kullanılır.
'''
kernel_x_Kirsch = np.array(
    [
        [-3, 0, 3],
        [-5, 0, 5],
        [-3, 0, 3]
    ]
)


'''
Scharr Kerneli
Scharr, Sobel’in geliştirilmiş halidir.
'''

kernel_x_Scharr = np.array(
    [
        [-3, 0, 3],
        [-10, 0, 10],
        [-3, 0, 3]
    ]
)


img = cv2.imread("messi5.jpg",cv2.IMREAD_GRAYSCALE)

convolved_x_Robinson = cv2.filter2D(img, -1, kernel_x_Robinson)
convolved_y_Robinson = cv2.filter2D(img, -1, kernel_x_Robinson.T)


convolved_x_Sobel = cv2.filter2D(img, -1, kernel_x_Sobel)
convolved_y_Sobel = cv2.filter2D(img, -1, kernel_x_Sobel.T)


convolved_x_Kirsch = cv2.filter2D(img, -1, kernel_x_Kirsch)
convolved_y_Kirsch = cv2.filter2D(img, -1, kernel_x_Kirsch.T)


convolved_x_Scharr = cv2.filter2D(img, -1, kernel_x_Scharr)
convolved_y_Scharr = cv2.filter2D(img, -1, kernel_x_Scharr.T)


# Goruntu Ekraninin isimleri ve Degiskenleri Atanir#
titles = ['Original Image','Robinson_x','Robinson_y',
          'Original Image','Sobel_x','Sobel_y'
          ]

titles2 = [
          'Original Image','Kirsch_x','Kirsch_y',
          'Original Image','Scharr_x','Scharr_y' 
          ]

images = [img, convolved_x_Robinson, convolved_x_Robinson, 
          img, convolved_x_Sobel, convolved_y_Sobel
          ]

images2 = [
          img, convolved_x_Kirsch, convolved_y_Kirsch,
          img, convolved_x_Scharr, convolved_y_Scharr
          ]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images2[i],'gray')
    plt.title(titles2[i])
    plt.xticks([]),plt.yticks([])

plt.show()



