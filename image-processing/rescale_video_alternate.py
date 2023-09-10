import cv2 as cv

capture = cv.VideoCapture(0)

#Alternate method
def changeRes(width, height):
    #For Live videos only
    capture.set(3,width)
    capture.set(4,height)
    #3 & 4 are used to set resolution of image
    
    #capture.set(10,width) 
    #capture.set(12,height)

changeRes(300,300)
while True:
    isTrue, frame = capture.read()
    
    cv.imshow("Live video", frame)
    
    if cv.waitKey(20) & 0xFF == ord("d"):
        break
    
capture.release()
cv.destroyAllWindows()