import cv2 as cv
import numpy as np

img =cv.imread('images/hanami.jpg')
# cv.imshow('Hanami',img)

# using bitwise ops masking can be performed in opencv

#bitwise ops require single channel mask

# masking allows you to focus on certain parts of the image that you want to display and removes all the unwanted parts of the image

# note: the dimensions of the mask needs to be the same size as that of the img otherwise it wont work
# img.shape[:2] extracts only the first two elements of img.shape, i.e., (height, width) whereas img.shape returns a tuple with three values: (height, width, channels)
blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)

# draw a circular mask on the blank img
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),200,255,-1)
# cv.imshow('Mask', mask)

# masked image
masked = cv.bitwise_and(img,img,mask=mask)
# cv.imshow('Masked Image',masked)

# rectangular mask
mask1 = cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2 + 100,img.shape[0]//2 + 100),255,-1)
# cv.imshow('rectangular mask', mask1)

masked1 = cv.bitwise_and(img,img,mask=mask1)
# cv.imshow('Masked rectangular image', masked1)

# creating weird masks
circle = cv.circle(blank.copy(), (img.shape[0]//2 + 45, img.shape[1]//2 + 45), 200, 255,-1)

rectangle = cv.rectangle(blank.copy(),(20,20),(370,370),255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)

cv.imshow('Weird shapes', weird_shape)

masked2 =cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('weird mask', masked2)


cv.waitKey(0)