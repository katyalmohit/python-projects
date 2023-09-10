import cv2 as cv

#capture = cv.VideoCapture('videos/dog.mp4')
capture = cv.VideoCapture(0)

# we can also pass integer arguments in this function like 0,1,2,3
#integer arguments are used when we are using webcam instead of filepath.
#the numbers 0,1,2 can denote multiple webcams when used on a single device

#we display video frame by frame using while loop

while True:
    isTrue, frame = capture.read() #read the video frame by frame
    
    cv.imshow('Video',frame) #show the video frame by frame
    
    #after some time while playing the video it shows exception"(-215)assertion failed"
    #this is because it has ran out of frames
    #similar exception can be seen if we specify the wrong path
    
    #to stop the video from playing indefinitely we define delay or any key like here 'd'
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()
    
    