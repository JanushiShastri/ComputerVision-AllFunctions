import os
import cv2

img = cv2.imread(os.path.join('.','schoolBus.png'))
print(img.shape)

cropped_img = img[109:567,121:585]

cv2.imshow('img', img)
cv2.imshow('crop',cropped_img)
cv2.waitKey(0)