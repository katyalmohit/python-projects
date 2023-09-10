import cv2 as cv

#capture = cv.VideoCapture('videos/dog.mp4')
capture = cv.VideoCapture(0)
address = 'http://192.168.93.27:8080/video' #url of IPwebcam
capture.open(address)

def rescale(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read() #read the video frame by frame
    resized_frame = rescale(frame, 0.5)
    cv.imshow('Video',resized_frame) #show the video frame by frame
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    

capture.release()
cv.destroyAllWindows()
    
    