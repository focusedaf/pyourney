import cv2 as cv

# normally any image that is displayed contains 3 channel bgr
img = cv.imread('images/hanami.jpg')
cv.imshow('hanami', img)

# converting an image to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# bluring an image helps to remove noise from an image
# gaussianblur takes the source image and kernel size as the arguement, kernel size is always odd
blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# edge cascade and cv.Canny() accepts parameters such as the img,lowerthreshold(125) and upperthershold(175)
canny = cv.Canny(img,125,175)
cv.imshow('canny edge',canny)

# dilating the image
dilated = cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilating an image', dilated)

# eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# resize
# by defualt interpolation=cv.INTER_AREA (FOR SHRINKING IMG)
# FOR INCREASING/SCALING USE cv.INTER_LINEAR OR cv.INTER_CUBIC()
resized = cv.resize(img,(500,500))
cv.imshow('Resized image', resized)

# cropping
cropped = img[20:100, 300:400]
cv.imshow('cropped image', cropped)

cv.waitKey(0)