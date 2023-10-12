import cv2 as cv
import cv2.aruco as aruco
import numpy as np

# Load the predefined dictionaries
dictionary = aruco.Dictionary_get(aruco.DICT_6X6_250)

# Generate the marker
markerImage = np.zeros((250,250), dtype=np.uint8)
markerImage = aruco.drawMarker(dictionary, 33, 200, markerImage, 1)