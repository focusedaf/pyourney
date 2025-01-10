import cv2 as cv
import numpy as np

# When you use blank directly, you are working with the original array (image) in memory. Any modifications to blank will change the original data.
blank = np.zeros((400,400), dtype='uint8')

# When you use blank.copy(), a new copy of the array is created in memory. Any changes made to the copy do not affect the original blank.
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255, -1)
circle = cv.circle(blank.copy(),(200,200),200,255, -1)
cv.imshow('rectangle',rectangle)
cv.imshow('circle', circle)

#bitwise ops require single channel 

# bitwise AND = intersecting regions
bitwise_and =cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR = non-intersecting regions and intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR = non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT = inverts the binary color
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT',bitwise_not)


cv.waitKey(0)