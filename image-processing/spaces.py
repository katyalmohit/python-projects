import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/park.jpg')
cv.imshow("Original", img)

# plt.imshow(img) #this will plot the BGR image instead of RGB Image
#but if we first convert the BGR image to RGB and then try to plot it then it will plot the RGB image.
# plt.show()

#BGR to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to l+a+b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#Gray to HSV or LAB
#We cannot convert Grayscale image to HSV or LAB directly. 
#First we have to convert the grayscale image to BGR or RGB
gray2hsv = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
gray2hsv = cv.cvtColor(gray2hsv, cv.COLOR_BGR2HSV)
cv.imshow('GRAY --> BGR --> HSV', gray2hsv)

#HSV to BGR
hsv2bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv2bgr)

#LAB to BGR
lab2bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab2bgr)

cv.waitKey(0)