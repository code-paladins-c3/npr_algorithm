import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import cv2 as cv
from edge_detection.filters import apply_median_filter
from edge_detection.gradient import get_sobel_filters
from edge_detection.suppresion import non_maximum_suppression
from edge_detection.threshold import calculate_threshold

def modified_canny_detector(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = apply_median_filter(img)

    kernel_x, kernel_y = get_sobel_filters()
    grad_x = cv.filter2D(np.float64(img), cv.CV_64F, kernel_x)
    grad_y = cv.filter2D(np.float64(img), cv.CV_64F, kernel_y)

    mag, ang = cv.cartToPolar(grad_x, grad_y, angleInDegrees=True)
    height, width = img.shape

    mag = non_maximum_suppression(mag, ang, width, height)

    adaptive_threshold = calculate_threshold(mag)

    _, binarized_image = cv.threshold(mag, adaptive_threshold, 255, cv.THRESH_BINARY)

    return binarized_image


input_img = cv.imread("input/pyramid2.jpeg")

modified_canny_img = modified_canny_detector(input_img)

cv.imwrite("output/improved_canny_edge.jpg", modified_canny_img)
cv.imshow("Modified Canny Edge Detection", modified_canny_img)
cv.waitKey(100000)
cv.destroyAllWindows()
