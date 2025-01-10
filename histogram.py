import cv2 as cv
import  numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/hanami.jpg')
# cv.imshow('hanami', img)

# histograms allows you to visualize pixel intensities distribution in an image

# computing a histogram for a gray scale image
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray) 

# calcHist() accepts images in the form of lists
gray_hist = cv.calcHist([gray],[0], None,[256],[0,256])
# plt.figure()
# plt.title("gray scale histogram")
# plt.xlabel('Bins')
# plt.ylabel('Number of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# making a histogram for a circular mask
blank = np.zeros(img.shape[:2],dtype='uint8')

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),200,255,-1)

mask = cv.bitwise_and(gray,gray,mask=circle)
# cv.imshow('Mask', mask)

# setting the mask parameter from NONE to mask
gray_hist = cv.calcHist([gray],[0], mask,[256],[0,256])
# plt.figure()
# plt.title("gray scale histogram")
# plt.xlabel('Bins')
# plt.ylabel('Number of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# rgb histogram
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB Image', rgb)

colors = ('r', 'g', 'b')  
plt.figure()
plt.title("RGB Histogram")
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')

# circle1 = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),200,255,-1)
# cv.imshow('Mask', circle1)
# mask = cv.bitwise_and(rgb,rgb,mask=circle1)

for i, color in enumerate(colors):
    hist = cv.calcHist([rgb], [i], None, [256], [0, 256])  
    plt.plot(hist, color=color) 
    plt.xlim([0, 256])

plt.show()


cv.waitKey(0)