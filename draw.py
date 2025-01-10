import cv2 as cv
import numpy as np

# shapes can be drawn directly on images or by creating a dummy image
# for np.zeros() you need to pass height,width and no of color channels(generally its 3)
blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('blank', blank)

# color the blank image lol
blank[:] = 255,0,0
blank[200:300, 300:400] = 255,0,0 #square
# # cv.imshow('Blue', blank)

# rectangle
cv.rectangle(blank, (0,0),(250,250), (255,0,0), thickness=3)
# to fill the rectangle use cv.FILLED  or -1
# cv.imshow('rectangle', blank)

# circle
# center is at 250,250 and radius is at 40
cv.circle(blank ,(250,250), 40,(0,255,0), thickness=cv.FILLED)
# cv.imshow('circle', blank)

# line
cv.line(blank,(0,0),(250,250),(0,0,255), thickness=2)
# cv.imshow('line', blank)

# text on an image
cv.putText(blank,"Hello",(225,225), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), 2)
# cv.imshow('text', blank)

img = cv.imread('images/hanami.jpg')
# cv.imshow('hanami', img)

cv.putText(img,"bye Felicia!!!", (225,225),cv.FONT_HERSHEY_DUPLEX,1.2,(255,0,0),2)
cv.imshow('hanami', img)

cv.circle(img, (200,200), 50, (0,255,0), thickness=-1)
cv.imshow('hanami', img)

cv.line(img, (0,0), (230,240),(255,0,0), thickness=2)
cv.imshow('hanami', img)

cv.rectangle(img,(0,0),(400,200),(0,0,255), thickness=-1)
cv.imshow('hanami', img)

cv.waitKey(0)