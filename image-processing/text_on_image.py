import cv2 as cv
import numpy as np

blank = np.zeros((500,500),dtype="uint8")

#Writing text on image
cv.putText(blank,"I have written a text on image",(0,200),cv.FONT_ITALIC,1,(255,255,0),thickness=2)
cv.imshow("Blank",blank)
cv.waitKey(0)