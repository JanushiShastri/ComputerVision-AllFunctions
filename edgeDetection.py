import os

import cv2
img = cv2.imread(os.path.join('.','schoolBus.png'))

img_edge = cv2.Canny(img, 200, 200)
cv2.imshow('img', img)

cv2.imshow('img_edge', img_edge)
cv2.waitKey(0)