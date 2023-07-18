import numpy as np
import cv2 as cv
img = cv.imread('Denoising image/01 with sp.png',cv.IMREAD_GRAYSCALE)

output = cv.medianBlur(img,5)

cv.imwrite('Input.png', img)
cv.imwrite('Output.png', output)