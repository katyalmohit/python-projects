import cv2 as cv
import numpy as np

#Drawing a blank image
#we have to pass 3 parameters while defining the shape i.e. width, height and the number of color chanels
#like here we are using RGB, so 3 color chanels
blank = np.zeros((500,500,3),dtype="uint8")
#cv.imshow("Blank",blank)

# Paint the image in certain color

# blank[:]=0,255,0
# blank[100:200,100:200]= 0,255,0
# cv.imshow("Blank",blank)

#Rectange
cv.rectangle(blank,(0,0),(255,255),(0,255,0),thickness=2)


#Circle
cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(0,0,255),thickness=-1)
#BRG istead of RGB is used here
#if thickness = -1 or cv.FILLED, then it will fill the whole shape
#(blank.shape[0]//2,blank.shape[1]//2) is used to get the centre of the window

#Line
cv.line(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(255,255,255),thickness=4)
cv.imshow("Blank",blank)
cv.waitKey(0)