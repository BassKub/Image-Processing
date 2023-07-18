import cv2
import numpy as np

image = cv2.imread('01.jpg',0)

kernel_size = 60
Angle = 45

kernel = np.zeros((kernel_size,kernel_size))
kernel[int((kernel_size-1)/2), :] = np.ones(kernel_size)
kernel = cv2.warpAffine(kernel,cv2.getRotationMatrix2D((kernel_size/2-0.5, kernel_size/2-0.5), Angle, 1.0),(kernel_size, kernel_size))
kernel = kernel/np.sum(kernel)

MB = cv2.filter2D(image, -1, kernel)

cv2.imshow('Original', image)
cv2.imshow('Motion Blur', MB)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('input.jpg',image)
cv2.imwrite('output.jpg',MB)