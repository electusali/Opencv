import numpy as np
import cv2

img=cv2.imread('kapak.png')
img2=img.copy()

img_gray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)

ret,thr=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
cnts,hierarch=cv2.findContours(thr,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img,cnts,-1,(0,255,0),3)

cv2.imshow('org',img2)
cv2.imshow('thress',thr)
cv2.waitKey(0)
cv2.destroyAllWindows()