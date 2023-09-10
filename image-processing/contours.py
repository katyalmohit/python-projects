import cv2 as cv
import numpy as np
#contours can be explained simply as a curve joining all the continuous points (along the boundary), 
# having same color or intensity.The contours are a useful tool for shape analysis and 
# object detection and recognition

img = cv.imread('photos/cats.jpg')
cv.imshow('Original',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

canny = cv.Canny(img,125,175) #blur can be used instead of img
cv.imshow('Canny',canny)

# if we use blur image instead of original image, there will be significant reduction in the contours.


# ret, thresh = cv.threshold(gray, 125, 175, cv.THRESH_BINARY)
# cv.imshow('Threshold', thresh)

# in simple kind of thresholding, it has several disadvantages when used for a single value,
#but in most cases it is the most favorite kind of thresholding because it is simple and it does pretty well.

contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)#thresh can be used instead of canny
print(f'{len(contours)} contour(s) found')

#draw contours 
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("Contours drawn", blank)

cv.waitKey(0)