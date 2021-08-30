import numpy as np
import cv2 as cv

img=np.zeros((512,512,3),np.uint8)
#for i in range(10):
   # cv.rectangle(img,(1+i*30,1+i*30),(512-i*30,512+i*30),(0,0,255),2)#-1 yaparsan ici dolu yapar

cv.rectangle(img,(1,1),(256,250),(0,0,255),-1)
cv.rectangle(img,(255,255),(512,512),(255,0,0),-1)
for i in range(5):
    cv.rectangle(img,(1+i*5,1+i*5),(128,128),(0,255,0),2)
for i in range(5):    
    cv.rectangle(img,(1+i*100,1),(128,128),(0,255,0),2)
cv.imshow('resim',img) 
cv.waitKey(0) 
cv.destroyAllWindows()  

for  i in range (4):
    print(' sayi.'+i )
