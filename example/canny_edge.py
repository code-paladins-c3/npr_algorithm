import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2 as cv
from edge_detection.filters import apply_median_filter
from edge_detection.gradient import get_sobel_filters
from edge_detection.suppresion import non_maximum_suppression
import numpy as np

input_img = cv.imread("input/pyramid.jpeg", cv.IMREAD_GRAYSCALE)

median_filtered_img = apply_median_filter(input_img)

kernel_x, kernel_y = get_sobel_filters()
grad_x = cv.filter2D(median_filtered_img, cv.CV_64F, kernel_x)
grad_y = cv.filter2D(median_filtered_img, cv.CV_64F, kernel_y)

grad_magnitude, grad_angle = cv.magnitude(grad_x, grad_y), cv.phase(grad_x, grad_y, angleInDegrees=False)

nms_result = non_maximum_suppression(grad_magnitude, grad_angle)

binary_img = cv.adaptiveThreshold(nms_result.astype(np.uint8), 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

cv.imwrite("output/canny_edge.jpg", binary_img)
cv.imshow("Canny Edge Detection", binary_img)
cv.waitKey(10)
cv.destroyAllWindows()