import os
import cv2
import numpy as np
img = cv2.imread('birds.jpg',cv2.IMREAD_GRAYSCALE)

#erode image transformation
#white region decreases
kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(img,kernel, iterations = 3)
dilation = cv2.dilate(img,kernel,iterations = 3)

cv2.imshow('img',img)
cv2.imshow('erode image', erosion)

#dilation, white region increase after noise
cv2.imshow('dilate image',dilation)
cv2.waitKey(0)
