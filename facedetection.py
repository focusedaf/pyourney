import cv2 as cv

img = cv.imread('images/terry.jpg')
# cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# faces_rect is the rectangular coordinates for the faces found in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(20,20))

print(f'Number of faces found = {len(faces_rect)}')

# looping over the faces_rect(which is a list) to grab those coordinates to draw the rectangle around the detected faces
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y), (x+w, y+h), (0,255,0), thickness=2)
 
cv.imshow('Detected faces', img)


cv.waitKey(0)