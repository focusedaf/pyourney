import cv2 as cv
import numpy as np

img = cv.imread('images/hanami.jpg')
# cv.imshow('hanami', img)

# translation 
# -x = left, -y = up x = right y = down
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    # img.shape[0]=width img.shape[1]=height
    dimensions =(img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated = translate(img,100,100)
# cv.imshow('translated image', translated)

# rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,60)
# cv.imshow('rotated image', rotated)

rotated_rotated = rotate(rotated, -45)
# cv.imshow('Rotated Rotated', rotated_rotated)

# resizing 
# by default cv.interpolation=cv.INTER_AREA 
resized =  cv.resize(img,(500,500))
# cv.imshow('Resized image', resized)

#flipping an image
# flip code 0= over x axis(vertically), 1= over y axis(horizonatally) -1=over both axes(vertically and horizontally)
flipped = cv.flip(img,-1)
# cv.imshow('Flipped image', flipped)

# cropping
cropped = img[200:400 ,300:400]
cv.imshow('cropped image', cropped)

cv.waitKey(0)