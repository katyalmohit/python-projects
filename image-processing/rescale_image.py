import cv2 as cv

def rescaleImage(image, scale=0.75):
    width = int(image.shape[1]*scale)
    height = int(image.shape[0]*scale)
    
    dimensions = (width, height) #tuple containing rescaled width and height of image
    
    return cv.resize(image, dimensions, interpolation = cv.INTER_AREA)

img = cv.imread('photos/cat.jpg')
resized_image = rescaleImage(img, 0.80)

cv.imshow("Original Image",img)
cv.imshow("Rescaled Image",resized_image)

cv.waitKey(0)
