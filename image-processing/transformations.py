import cv2 as cv
import numpy as np

img = cv.imread('photos/park.jpg')
cv.imshow('Original',img)

#1. Translation
def translate(image, x, y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (int(img.shape[1]),int(img.shape[0]))
    return cv.warpAffine(image,transmat,dimensions)

# -X --> Left
# -Y --> Up
#  X --> Right
#  Y --> Down
translated = translate(img, -100, 100)
cv.imshow('Translated',translated)

#2. Rotation
# here, we can rotate the image around any point
def rotate(image, angle, rotPoint=None):
    (width, height)= image.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(image, rotMat, dimensions)

rotated = rotate(img, 45,(200,300))
cv.imshow('Rotated',rotated)

rotated_rotated = rotate(rotated, -45,(200,300))
cv.imshow('Rotated again', rotated_rotated)

#3. Resizing 
resized = cv.resize(img,(600,600),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#4. Flipping
flipped = cv.flip(img, 1)
#flip code-->  0 --> flip vertically
#flip code-->  1 --> flip horizontally
#flip code--> -1 --> flip horizontally and vertically
cv.imshow('Flipped',flipped)

#5. Cropping 
cropped = img[200:400,300:500]
cv.imshow('Cropped', cropped)

cv.waitKey(0)