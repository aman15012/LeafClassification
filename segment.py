import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
import matplotlib.image as mpimg
from skimage.filters import sobel

# values from flavia paper
def segment(rgb):
    temp = np.dot(rgb[...,:3], [ 0.2989,  0.5870, 0.1140])
    temp -= np.min(temp)
    temp /= np.max(temp)
    temp[temp>0.95] = 1
    temp[temp<=0.95] = 0 
    kernel = np.ones((3,3),np.float32)/9
    temp = cv2.filter2D(temp,-1,kernel)
    temp[temp>0.95] = 1
    temp[temp<=0.95] = 0 
    return sobel(temp)

img = mpimg.imread('./Leaves/1001.jpg')     
gray_img = segment(img)    

plt.imshow(gray_img, cmap=plt.cm.gray)
plt.show()