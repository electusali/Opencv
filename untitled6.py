# -*- coding: utf-8 -*-
import cv2
import numpy as np


ekran=np.zeros((500,500,3),dtype=np.uint8)


cv2.rectangle(ekran,(100,150),(200,250),(255,0,0),2)#kare cizme
cv2.circle(ekran,(300,250),50,(255,0,0),2)#yuvarlak cizme
cv2.arrowedLine(ekran,(0,0),(240,240),(255,0,0),2)#ok c    
cv2.imshow('pencere',ekran)
cv2.waitKey(0)
cv2.destroyAllWindows()
