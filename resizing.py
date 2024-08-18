#resize
import cv2
import os

img = cv2.imread(os.path.join('.','schoolBus.png'))
resized_img = cv2.resize(img, (315,520))
print(img.shape)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_iomg', resized_img)
cv2.waitKey(0)
