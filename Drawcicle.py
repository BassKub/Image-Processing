import numpy as np
import cv2 as cv

img = np.zeros([300,400], dtype = np.uint8)

cv.circle(img,(200, 150),100,(255, 0, 0),2)
cv.circle(img,(200, 150),35,(255, 0, 0),1)
cv.circle(img,(200, 150),65,(255, 0, 0),1)
cv.circle(img,(70, 50),30,(255, 0, 0),-1)
cv.circle(img,(380, 250),70,(255, 0, 0),-1)

cv.imshow('Drawing',img)
cv.waitKey(0)
cv.destroyAllWindows()