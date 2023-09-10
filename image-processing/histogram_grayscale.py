import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)



#converting img to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

#computing histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
#instead of only one image 'gray', we can pass a list of images to compute the histogram
#[0]: This specifies the channel index for which you want to compute the histogram. 
#       For grayscale images, there's only one channel (usually channel index 0).
# None: This parameter is the mask, which allows you to calculate the histogram for only a 
#       certain region of the image. In this case, since it's set to None, the entire image is considered.
# [256]: This is the number of bins you want to use for the histogram. It means the 
#       pixel values will be divided into 256 intervals or bins.
# [0, 256]: This is the range of pixel values that will be considered when creating the histogram. 
#       In this case, it's the full range of grayscale pixel values from 0 to 255.
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('No. of chanels')
# plt.xlim([0,256])
# plt.plot(gray_hist)
# plt.show()

#histogram of masked image
blank = np.zeros(img.shape[:2], 'uint8')
circle_mask = cv.circle(blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(gray, gray, mask = circle_mask)
cv.imshow('Masked Image', masked)
masked_hist = cv.calcHist([gray], [0], circle_mask, [256], [0, 256])
#here instead of 'circle_mask' parameter, we can also pass the masked image, as there is only one chanel.
#but when we compute the histogram of maskeed colored images, then we have to pass the mask in this case, 'circle_mask'

plt.figure()
plt.title('Histogram of masked grayscale image')
plt.xlabel('Bins')
plt.ylabel('No. of chanels')
plt.xlim([0,256])
plt.plot(masked_hist)
plt.show()

cv.waitKey(0)