import cv2 as cv

img = cv.imread('images/hanami.jpg')
cv.imshow('Hanami',img)

# smoothing an image is basically done to remove noise caused by camera sensors, lighting issues when the image was taken etc and can be done by applying blurring methods

# kernel = no of rows and columns

# blurring techniques

# averaging = depending on the kernel size the middle pixel new pixel intensity is the average intensity of its surrounding pixels
average = cv.blur(img,(3,3))
cv.imshow('Average Blur', average)

# gaussian blur = does the same thing as averaging but instead of computing the average of the surrounding pixels each surrounding pixel is given a weight and the average of the product of the weight gives you the value for true center and it gives less blurring compared to averaging but gb is more natural than avg
gaussian_blur = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur', gaussian_blur)

# median blur = same thing as averaging but instead of computing avg of surrounding pixels it finds the median and this method is more effective for reducing noise 
# this method accepts kernal size as a single integer instead of giving it a tuple
median_blur = cv.medianBlur(img, 3)
cv.imshow('median blur', median_blur)

# bilateral blurring is the most effective as it applies blurring but retains the edges of the image
# this method accepts the img(obviously), diameter(5 in this case), sigmacolor(15 in this case, larger the value of color sigma means more colors in the neighbourhood which will be considered when blur is computed),sigmaspacing(15 in this case, larger value of space sigma means there are pixels further out from the central pixel which will influence the blurring process )
bilateral = cv.bilateralFilter(img, 5,15,15)
cv.imshow('bilateral blur', bilateral)


cv.waitKey(0)