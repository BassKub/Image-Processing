import random
import cv2 as cv

img = cv.imread('Denoising image/01.jpg',cv.IMREAD_GRAYSCALE)

density_salt = 0.1
density_pepper = 0.1

number_of_white_pixel = int(density_salt*(img.shape[0]*img.shape[1]))

for i in range(number_of_white_pixel):
    y_coord = random.randint(0, img.shape[0] - 1)
    x_coord = random.randint(0, img.shape[1] - 1)
    img[y_coord][x_coord] = 255

number_of_black_pixel = int(density_pepper*(img.shape[0]*img.shape[1]))

for i in range(number_of_black_pixel):
    y_coord = random.randint(0, img.shape[0] - 1)
    x_coord = random.randint(0, img.shape[1] - 1)
    img[y_coord][x_coord] = 0
    
cv.imwrite('01 with sp.png',img)