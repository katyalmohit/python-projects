import cv2 as cv
import numpy as np

blank = np.zeros((400,400), 'uint8')
cv.imshow('Blank', blank)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), (255, 255, 255), -1)
cv.imshow("Rectange", rectangle)

#here we are using blank.copy()to prevent over-riding because if we have drawn rectangle on the blank image,
#and then try to draw a circle on blank, then it will overlap the rectangle and show them both at same time
#blank.copy() prevents the image from over-riding.
circle = cv.circle(blank.copy(), (200, 200), 200, (255, 255, 255), -1)
cv.imshow('Circle', circle)

#bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

#bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

#bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

#bitwise NOT -->  inverts the colors or pixel values of an image
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)