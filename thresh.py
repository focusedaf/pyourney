import cv2 as cv

img = cv.imread('images/hanami.jpg')
# cv.imshow('hanami', img)

# thresholding is binarization of an img(converting an image to binary) where the pixels are either 0 (black) or 255(white)
# less than the threshold value img would be black (0) and if its above then it will be white(255)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# simple thresholding
# we'll be using cv.threshold() which returns threshold and thresh(binarized image)
# if the pixel is above 150(threshold) then the it will be set to 255 otherwise it sets to 0 and all this is done by cv.THRESH_BINARY
threshold, thresh = cv.threshold(gray,150,255, cv.THRESH_BINARY)
cv.imshow('simple thresholded', thresh)

# in thresh_inv pixels values that are below 150 are set to 255
threshold, thresh_inv = cv.threshold(gray,150,255, cv.THRESH_BINARY_INV)
cv.imshow('inverted thresholded', thresh_inv)

# adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive threshold', adaptive_thresh)

adaptive_thresh_1 = cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('adaptive threshold 1', adaptive_thresh_1)

cv.waitKey(0)