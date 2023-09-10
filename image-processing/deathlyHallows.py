import cv2 as cv
import numpy as np

dh = np.zeros((500,500),dtype='uint8')

#Array consisting of triangle points
pts = np.array([[250,10],[10,400],[490,400]],np.int32)

#drawing three lines
cv.polylines(dh,[pts],True,(255,255,255),thickness=4)

#drawing circle
cv.circle(dh,(250,265),132,(255,255,255),thickness=1)

#drawing line
cv.line(dh,(250,10),(250,400),(255,255,255),thickness=2)

#writing text
cv.putText(dh,"Deathly Hallows",(10,460),cv.FONT_ITALIC,2,(255,255,255),thickness=2)
cv.imshow('Deathly Hallows',dh)

cv.waitKey(0)