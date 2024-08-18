import os
import cv2
import numpy as npc
img = cv2.imread('birds.jpg',cv2.IMREAD_GRAYSCALE)

#two types
#1.     wrapAffine -> 2x3 matrix transformation
#2. warppersective -> 3x3 MT

rows,cols,ch = img.shape
 
# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv2.warpAffine(img,M,(cols,rows))

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)
 
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()