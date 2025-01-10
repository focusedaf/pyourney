import cv2 as cv

# # imread() is used to  read images
# img = cv.imread('images/hanami.jpg')

# # imshow() to display the image and it displays the image as a window so you just need to pass the name of the window and the actual matrix or pixels required to display the said image in this case its img 
# cv.imshow('Hanami', img)


# Waits indefinitely for a key press before closing all displayed windows.
# cv.waitKey(0)

#use capture variable to read vid since its an instance of this class VideoCapture()
# pass in the value 0 for webcam 
capture = cv.VideoCapture('video/s.mp4')
# to read videos a while loop is required
while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    # this is to avoid the video from playing infinitely
    # 0xFF==ord('d') basically means that if letter d is pressed then end the video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()


