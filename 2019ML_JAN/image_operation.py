#!/usr/bin/python2

import  cv2

print(cv2.__version__)
#  reading  data from a image file  
'''
imread --- 1 , 0 , -1
1 -- original image
0 - grayscale (black and white)
-1 transparency ingore 
'''
img=cv2.imread('fast.jpg',1)
img1=cv2.imread('cat.jpg',1)
img2=cv2.imread('cat.jpg',0)
img3=cv2.imread('cat.jpg',0)
img4=cv2.imread('img2.JPG',0)
print(img)
print(img.shape)
print(img1.shape)
#  to show the image
cv2.imshow('windowname',img1+30)
cv2.imshow('windowname1',img2)
cv2.imshow('windowname2',img1+img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
