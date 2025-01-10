import cv2 as cv
import numpy as np

img = cv.imread('images/hanami.jpg')
cv.imshow('Hanami', img)

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# using cv.Canny to grab the edges
canny = cv.Canny(blur, 125,175)
# cv.imshow('Canny', canny)


# contours are basically boundaries of an object, the line or curve that joins the continuous points along the boundary of an object

# cv.findContours() basically returns contours, hierarchies by looking at the edges that were found in the image(canny image) and hierarchies is just hierarchial representation of contours

# cv.RETR_LIST gives the complete list of all the contours whereas cv.RETR_EXTERNAL returns only external contours, cv.RETR_TREE returns hierarchial contours

# cv.CHAIN_APPROX_NONE returns all the contours whereas cv.CHAIN_APPROX_SIMPLE compresses the contours and then returns it

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contour(s) found:')

# another way of contouring is using ret threshold
# threshold(cv.THRESH_BINARY) just looks at an image and binarizes it so in this case if the intensity of a pixel is below 125 its going to be set to zero or blank and if its above 125 then its set to white or 255 inshort it converts an image to black(0) or white(255)
ret,thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found:')

# opencv allows us to visualize contours on the image
# earlier in draw.py we were giving specific height and width for the creation of blank window we can just use img.shape
blank = np.zeros(img.shape, dtype ='uint8')
cv.imshow('Blank', blank)

# to draw contours over a blank img and it accepts the parameters blank(the place on which you are drawing the contours), contours(the list of all contours), contourindex=-1(since we want all contours),color and thickness
cv.drawContours(blank, contours, -1,(255,0,0),1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)