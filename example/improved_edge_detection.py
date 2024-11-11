import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2 as cv
from edge_detection.canny_edge import modified_canny_detector

input_img = cv.imread("input/knight.jpeg")

modified_canny_img = modified_canny_detector(input_img)

cv.imwrite("output/improved_canny_edge.jpg", modified_canny_img)
cv.imshow("Modified Canny Edge Detection", modified_canny_img)
cv.waitKey(100000)
cv.destroyAllWindows()
