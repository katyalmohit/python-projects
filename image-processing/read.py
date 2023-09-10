import cv2 as cv

img = cv.imread('photos/colorful.jpg') #read image in matrix form

#1st parameter is image name to be displayed, 2nd is matrix form
cv.imshow('This is cat',img) #display the image


cv.waitKey(2000) #determines the time for displaying the image on console
# if 0 is used then, image will be displayed for infinite amount of time

