import cv2 as cv

img = cv.imread('/home/mohit/Repositories/python/image-processing/photos/cat.jpg')
# cv.imshow('Cat', img)

dimensions = img.shape
print(dimensions)
cv.waitKey(0)