import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], 'uint8')
circle_mask = cv.circle(blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img, img, mask = circle_mask)
cv.imshow('Masked', masked)
#Color Histogram
colors = ('b','g','r')

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of chanels')
for i,col in enumerate(colors):
    #for without masked histogram
    #hist = cv.calcHist([img], [i], None, [256], [0, 256])
    
    #for masked histogram
    hist = cv.calcHist([img], [i], circle_mask, [256], [0, 256])
    #if we have to compute the histogram of masked colored image, then we have to pass the mask as parameter,
    #not the masked image.
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.show()



cv.waitKey(0)