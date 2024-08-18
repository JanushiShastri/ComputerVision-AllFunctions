import os

import cv2
img = cv2.imread(os.path.join('.','schoolBus.png'))
b,g,r = cv2.split(img)


cv2.imshow('blue',b)
cv2.imshow('red',r)
cv2.imshow('green',g)
cv2.waitKey(0)