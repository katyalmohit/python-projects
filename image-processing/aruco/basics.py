import cv2 as cv
import cv2.aruco as aruco
import numpy as np

# Load the predefined dictionaries
dictionary = aruco.Dictionary_get(aruco.DICT_6X6_250)

# Generate the marker
markerImage = np.zeros((20,20), dtype=np.uint8)
markerImage = aruco.drawMarker(dictionary, 200, 200, markerImage, 1)

# Save the marker to an image file
cv.imwrite("marker33.png", markerImage)

# Display the marker to the screen
cv.imshow("Marker", markerImage)
cv.waitKey(0)