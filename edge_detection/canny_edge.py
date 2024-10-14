import cv2 as cv
import numpy as np
import sys

input_img = cv.imread("input/pyramid.jpeg")
gray_img = cv.cvtColor(input_img, cv.COLOR_BGR2GRAY)

median_filter = cv.medianBlur(gray_img, 3)

kernel_x = np.array([[-np.sqrt(2)/4, 0, np.sqrt(2)/4],
                     [-1, 0, 1],
                     [-np.sqrt(2)/4, 0, np.sqrt(2)/4]])

kernel_y = np.array([[-np.sqrt(2)/4, -1, -np.sqrt(2)/4],
                     [0, 0, 0],
                     [np.sqrt(2)/4, 1, np.sqrt(2)/4]])

grad_x = cv.filter2D(median_filter, cv.CV_64F, kernel_x)
grad_y = cv.filter2D(median_filter, cv.CV_64F, kernel_y)

grad_magnitude = np.sqrt(grad_x**2 + grad_y**2)
grad_angle = np.arctan2(grad_y, grad_x)

def non_max_suppression(grad_magnitude, grad_angle):
    rows, cols = grad_magnitude.shape
    result = np.zeros((rows, cols),dtype=np.int32)
    angle = grad_angle * 180. / np.pi
    angle[angle < 0] += 180
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            prev = 255
            next = 255
            
            angle = grad_angle[i, j]
            if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
                prev = grad_magnitude[i, j+1]
                next = grad_magnitude[i, j-1]
            elif (22.5 <= angle < 67.5):
                prev = grad_magnitude[i+1, j-1]
                next = grad_magnitude[i-1, j+1]
            elif (112.5 <= angle < 157.5):
                prev = grad_magnitude[i-1, j-1]
                next = grad_magnitude[i+1, j+1]

            if (grad_magnitude[i, j] >= prev) and (grad_magnitude[i, j] >= next):
                result[i, j] = grad_magnitude[i, j]
            else:
                result[i, j] = 0
    
    return result

nms_result = non_max_suppression(grad_magnitude, grad_angle)

binary_img = cv.adaptiveThreshold(nms_result.astype(np.uint8), 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

cv.imwrite("output/edge_detection.jpg", binary_img)
cv.imshow('Edge Detection', binary_img)
cv.waitKey(0)
cv.destroyAllWindows()