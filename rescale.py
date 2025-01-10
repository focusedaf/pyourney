import cv2 as cv

img =cv.imread('images/hanami.jpg')
cv.imshow('Hanami', img)

# works for images,videos and live video
def rescaleFrame(frame,scale=0.75):
    width =int (frame.shape[1] *scale)    
    height =int (frame.shape[0] *scale)    
    dimensions = (width,height)
    # cv.resize() resizes the frame to a particular dimension
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

img_resized = rescaleFrame(img)
cv.imshow('hanami', img)
cv.imshow('hanami resized', img_resized)
cv.waitKey(0)

# another way to change the width and height of a video is by  handling its resolution

# only works for live video
def changeResolution(width,height):
    capture.set(3,width)
    capture.set(4,height)

# read videos
# capture = cv.VideoCapture('video/s.mp4')
# # to read videos a while loop is required
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('video', frame)

#     frame_resized = rescaleFrame(frame)
#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)
#     # this is to avoid the video from playing infinitely
#     # 0xFF==ord('d') basically means that if letter d is pressed then end the video
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()


