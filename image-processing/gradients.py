import cv2 as cv
import numpy as np

img = cv.imread('photos/park.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian:
#Detects edges using second derivatives, sensitive to noise.
# so it's often applied to images that have been pre-processed or smoothed.
#It highlights areas with rapid intensity changes.
lap = cv.Laplacian(gray, cv.CV_64F)
#cv.CV_64F: The data type of the output Laplacian image. 
# In this case, it's using a 64-bit floating-point data type.
#The result of this line is an image containing the Laplacian edges, 
# but these edges might have negative values and can range outside the [0, 255] range.
lap = np.uint8(np.absolute(lap))
#np.absolute(lap): This takes the absolute value of each pixel in the Laplacian image. 
#np.uint8(...): This converts the result to an 8-bit unsigned integer data type. 
# The Laplacian image is now within the [0, 255] range, suitable for display as a grayscale image.
cv.imshow('Laplacian', lap)

# Sobel:
#Computes gradients to highlight edges, more noise-resistant than Laplacian. 
# The Sobel operator can be applied separately in the horizontal and vertical directions 
# to calculate the gradients in those directions.
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
#1: This specifies the order of the derivative in the x direction. 
# A value of 1 means first-order derivative, which is used to calculate the gradient.

#0: This specifies the order of the derivative in the y direction. 
# A value of 0 means no derivative in the y direction.
cv.imshow('Sobel x', sobelx)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('Sobel y', sobely)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel', combined_sobel)

# Canny:
#Multi-stage process for accurate and noise-resistant edge detection, produces thin edges.
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)