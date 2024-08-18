import numpy as np

import cv2
blank = np.zeros((400,400), dtype='uint8')

rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv2.circle(blank.copy(), (200,200),200,255,-1)

cv2.imshow('Rectangle', rectangle)
cv2.imshow('circle',circle)

#bitwise AND
bitwise_and = cv2.bitwise_and(rectangle,circle)
cv2.imshow('bitwise and',bitwise_and)
cv2.waitKey(0)

#bitwise OR

#bitwise XOR

#bitwise NOT
