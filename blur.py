import os

import cv2
img = cv2.imread(os.path.join('.','schoolBus.png'))

k_size = 7
img_blur = cv2.blur(img,(k_size,k_size))
img_gaussian_blur = cv2.GaussianBlur(img,(k_size,k_size),5)
cv2.imshow('img', img_gaussian_blur)
cv2.waitKey(0)