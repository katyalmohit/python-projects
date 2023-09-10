import cv2 as cv

img = cv.imread('photos/lady.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors= 3)
# scaleFactor and minNeighbors control the sensitivity and accuracy of the detection process.
#if scaleFactor is set to 1.1, the algorithm will shrink the image by 10% at each scale, 
# searching for objects at progressively smaller sizes. A larger scaleFactor (e.g., 1.5) 
# will speed up the detection but might miss smaller objects.


#minNeighbors: Higher values of minNeighbors will reduce false positives 
# but may also result in missing some true positives.
#If minNeighbors is set to 3, a region will only be considered as a valid detection 
# if at least 3 other overlapping regions have also been classified as detections in that area.
print(f'No. of faces found: {len(faces_rect)}')

#Drawing rectangle around the face
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow('Detected Faces', img)

cv.waitKey(0)