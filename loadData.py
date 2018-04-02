import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
import matplotlib.image as mpimg
from skimage.filters import sobel
from segment import segment
from scipy.misc import imread
from skimage.transform import rescale, resize, downscale_local_mean


f = open('train','r')
x = f.readlines()


trainY = []
trainX = np.array([]).reshape(0, 1200*1600)

for i in range(len(x)):
	print(i)
	x[i] = x[i].strip().split('\t')
	path = x[i][2]
	img = mpimg.imread(x[i][2])
	gray_img = segment(img).ravel()
	trainX = np.vstack((trainX, gray_img))
	trainY.append(int(x[i][0]))

trainY = np.array(trainY)


f = open('test','r')
x = f.readlines()
testY = []
testX = np.array([]).reshape(0, 300*400)

for i in range(len(x)):
	x[i] = x[i].strip().split('\t')
	path = x[i][2]
	img = imread(x[i][2])
	print(i)
	gray_img = segment(img)
	gray_img = downscale_local_mean(gray_img, (4,4)).ravel()
	testX = np.vstack((testX, gray_img))
	testY.append(int(x[i][0]))

testY = np.array(testY)


np.save('testX.npy', testX)
np.save('testY.npy', testY)
# np.save('trainX.npy', trainX)
# np.save('trainY.npy', trainY)
