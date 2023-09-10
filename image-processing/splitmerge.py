import cv2 as cv
import numpy as np

img = cv.imread('photos/park.jpg')
cv.imshow('Original', img)

#Splitting the image
#we can display the specific color chanel of an image
#Here, the image will be displayed in three components b,g,r
b, g, r = cv.split(img)
#here each splitted image will be displayed in grayscale image
#where lighter portion represents the higher intensity of that color
#and darker portion represents the lower intensity of that color
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

#Printing the dimensions of images
print(img.shape) #here the output will contain third part as well which will display the number of color chanels
print(b.shape)
print(g.shape)
print(r.shape)

#Merging
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

#Specifying color chanels differently
blank = np.zeros(img.shape[:2], 'uint8')
# cv.imshow('Blank', blank)
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
#same concept about intensity: lighter implies more intensity, darker implies less intensity of color
cv.imshow('Blue(Alternate)', blue)
cv.imshow('Green(Alternate)', green)
cv.imshow('Red(Alternate)', red)


# merged_2 = cv.merge([blue, green, red]) #now we cannot merge them like this
# cv.imshow('Merged_2', merged_2)

cv.waitKey(0)