import cv2
import numpy as np

img = cv2.imread('harf.png',0)
kernel = np.ones((5,5),np.uint8) 

#tek sayı olmak zorunda 3x3, 7x7
erozyon = cv2.erode(img,kernel,iterations = 1)

dialate = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('erezyon',erozyon)
cv2.imshow('dilate',dialate)
cv2.imshow('opening',opening)
cv2.imshow('close',closing)
cv2.imshow('org',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
