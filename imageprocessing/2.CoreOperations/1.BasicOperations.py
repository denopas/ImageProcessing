'''
# =============================================================================
# Accessing and Modifying pixel values
# =============================================================================
'''


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi5.jpg')


'''
Accessing Image Properties
Image properties include number of rows, columns and channels, type of image data, 
number of pixels etc.

Shape of image is accessed by img.shape. It returns a tuple of number of rows, 
columns and channels (if image is color):
'''

print (img.shape)

#Total number of pixels is accessed by img.size
print (img.size)

print('Type of the image : ' , type(img))
print()
print('Shape of the image : {}'.format(img.shape))
print('Image Hight {}'.format(img.shape[0]))
print('Image Width {}'.format(img.shape[1]))
print('Dimension of Image {}'.format(img.ndim))
print('Maximum RGB value in this image {}'.format(img.max()))
print('Minimum RGB value in this image {}'.format(img.min()))




'''
You can access a pixel value by its row and column coordinates. 
For BGR image, it returns an array of Blue, Green, Red values. 
For grayscale image, just corresponding intensity is returned.
'''

px = img[100,100]
print (px)
# [B:156 G:166 R:200]

# Channel 0 --> Blue
# Channel 1 --> Green
# Channel 2 --> Red


# accessing only blue pixel (from channel 0)
blue = img[100, 100, 0]
print (blue)


# You can modify the pixel values the same way.
img[100, 100] = [255, 255, 255]
print (img[100, 100])



fig, ax = plt.subplots(nrows = 1, ncols=3, figsize=(15,5))
for c, ax in zip(range(3), ax):
    
    # create zero matrix
    split_img = np.zeros(img.shape, dtype="uint8") 
    
    # assing each channel 
    split_img[ :, :, c] = img[ :, :, c]
    
    # display each channel
    ax.imshow(split_img)
