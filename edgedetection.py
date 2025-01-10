import cv2 as cv
import numpy as np

img = cv.imread('images/hanami.jpg')
# cv.imshow('hanami', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# following all are edge detection algos

# laplacian 
# d depth/ data depth in this case is CV_64F
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel: it works along both x and y axes
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
# cv.imshow('Sobel X', sobelx)
# cv.imshow('Sobel Y', sobely)

combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('Combined Sobel', combined_sobel)

# comparing laplacian and sobel with canny
canny = cv.Canny(gray,150,175)
cv.imshow('Canny', canny)


cv.waitKey(0)