import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Original', img)

#Averaging: Uniform blurring, fast but might not preserve edges well.
average = cv.blur(img, (7,7))
#we provide a kernel size, such as (7, 7), which defines a window 
# or matrix of dimensions 7x7 (or an odd-sized kernel in general).
# For each pixel in the image, the kernel is centered around that pixel.
# The values of all the pixels within the kernel are summed up.
# The sum is then divided by the total number of pixels in the kernel 
# (in this case, 7x7 = 49) to obtain the average value.
# The pixel being processed is then replaced with this average value.


cv.imshow('Average', average)

#Gaussian Blur: Smooth and natural-looking blur, often used for noise reduction and pre-processing.
gb = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gb)

#Median Blur: Effective at removing salt-and-pepper noise, preserves edges.
mb = cv.medianBlur(img, 7)
cv.imshow('Median Blur', mb)

#Bilateral Blur: Blurs while preserving edges and textures, 
# good for noise reduction without sacrificing details.
bb = cv.bilateralFilter(img, 7, 15, 10)
cv.imshow('Bilateral Blur', bb)

cv.waitKey(0)