import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/hanami.jpg')
cv.imshow('Hanami', img)

#opencv reads images in the format of bgr and in real world evrrything is there in rgb

# color spaces is a system of representing an array of pixel colors. ex: rgb, greyscale,hsv etc

# bgr to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# bgr to hsv(hue saturation value and is based on how humans think and conceive of color)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# bgr to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# display a bgr image using matplot lib. since mtplt doesnt know that its displaying a bgr image it displays the bgr image in rgb format
plt.imshow(img)
# plt.show()

# to solve this issue you can just convert the img to rgb using opencv
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
plt.imshow(rgb)
# plt.show()

# you can convert gray to bgr, hsv to bgr etc but you cannot convert gray to hsv directly it first needs to be converted into bgr and then it will be converted to hsv

# hsv to bgr
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

# lab to  bgr
lab_bgr = cv.cvtColor(lab,cv.COLOR_HSV2BGR)
cv.imshow('LAB to BGR', lab_bgr)



cv.waitKey(0)