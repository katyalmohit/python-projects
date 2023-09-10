import cv2 as cv

img = cv.imread('photos/park.jpg')
cv.imshow('Original',img)

#1. Grayscale
#cvtColor - convert color
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayScale',gray)

#2. Blur using GaussianBlur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
#here (3,3) is kernel size which needs to be and odd number
#highert he ksize, higher the blur
cv.imshow('Blur',blur)

#3. Edge Cascade
#Detects edges using canny
canny = cv.Canny(img,125,175)
#125 and 175 are threshold values(lower and upper)
#These are used to determine which edges are strong and which one are weak
#The edges with gradient magnitudes larger than T_tupper are considered strong edges,
#and those with gradient magnitudes smaller than T+lower are considered non-edges.
#Edges with gradient magnitudes between T_lower and T_upper are considered weak edges.
#If we use blur image instead of original image, then it will have less edges
cv.imshow("Edge", canny)

#4. Dialating the canny image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

#5. Eroding(Using this we can again get the NEARLY original canny image, if dilated image is operated)
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded', eroded)

#6. Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
#interpolation is used when we are resizing the image to retain the quality 
#cv.INTER_AREA is used when the resized image has lower dimensions than the operated image
#cv.INTER_LINEAR or cv.INTER_CUBIC is used when the resized image has higher dimensions than the operated image
#cubic is a bit slower but effective function
cv.imshow("Resized",resized)

#7. Cropping
cropped = img[100:400,100:400]
#takes a specific portion with the help of the coordinates
cv.imshow('Cropped',cropped)

cv.waitKey(0)