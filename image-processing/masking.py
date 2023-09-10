import cv2 as cv
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], 'uint8')
#we have to pass the same size here as of original image
#otherwise we'll not be able to perform masking
cv.imshow('Blank', blank)

#Circle Mask
circle_mask = cv.circle(blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 80, (255, 255, 255), -1)
#we can shift the mask by shifting the coordinates of the circle here
# cv.imshow('Circle Mask', circle_mask)

#Rectangle Mask
rect_mask = cv.rectangle(blank.copy(), (200,200), (400, 400), 255, -1)
# cv.imshow('Rectangle Mask', rect_mask)

#Weird Mask
weird_mask = cv.bitwise_and(circle_mask, rect_mask)
cv.imshow('Weird Mask', weird_mask)

#masking
# masked = cv.bitwise_and(img, img, mask = circle_mask)
masked = cv.bitwise_and(img, img, mask = weird_mask)
cv.imshow('Masked', masked)

cv.waitKey(0)