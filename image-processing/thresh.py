import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple thresholded', thresh)

#Inverse Thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse thresholded', thresh_inv)

#Adaptive Thresholding
# This technique calculates the threshold value for each pixel based on the mean of its neighborhood 
# and adjusts it using the specified constant. This approach is useful when the 
# lighting conditions in the image vary.
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 9)
#9: A constant subtracted from the calculated mean. This can be used to fine-tune the threshold value.
cv.imshow('Adaptive thresholded', adaptive_thresh)

#Inverse Adaptive Thresholding
adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11,9)
cv.imshow('Inverse Adaptive thresholded', adaptive_thresh_inv)

cv.waitKey(0)