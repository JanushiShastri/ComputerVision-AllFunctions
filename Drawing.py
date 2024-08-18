import os
import cv2

img = cv2.imread(os.path.join('.','whileboard.jpg'))
#line:


cv2.line(img, (119,145), (707,145), (0,0,0), 3)

#rectangle
cv2.rectangle(img, (200,350),(450,507),5)

#circle
cv2.circle(img, (800, 100), 50, (255,0,0), 5)
#text
cv2.putText(img, 'janushi',(600,400),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,0), 3)
cv2.imshow('img',img)
cv2.waitKey(0)
