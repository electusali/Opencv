import cv2
import numpy as np


ekran=np.zeros((500,500,3),dtype=np.uint8)
for i in range(3):
    cv2.line(ekran,(0,125+i*125),(500,125+i*125),(0,250,0),2)
    
for i in range(3):
    cv2.line(ekran,(125+i*125,i*125),(125+i*125,500-i*125),(255,0,0),2)

cv2.rectangle(ekran,(250,250),(500,500),(255,0,0),2)    
cv2.imshow('pencere',ekran)
cv2.waitKey(0)
cv2.destroyAllWindows()
