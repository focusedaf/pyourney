import cv2 as cv
import numpy as np

img = cv.imread('images/hanami.jpg')
cv.imshow('Hanami', img)

# splitting an image into its color channels
b,g,r = cv.split(img)

# images will be depicted and displayed as grayscale images that show distribution of pixel intensities, lighter regions show more pixel concentrations and darker regions show little to no pixel concentration
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

# printing the dimensions of the image
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging these color channels together
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

# merging single color
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)


cv.waitKey(0)
