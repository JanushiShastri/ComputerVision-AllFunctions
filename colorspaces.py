import os

import cv2
img = cv2.imread(os.path.join('.','schoolBus.png'))
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# cv2.imshow('img', img)
cv2.imshow('img', img_rgb)
cv2.waitKey(0)