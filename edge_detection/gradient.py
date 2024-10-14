import numpy as np
import cv2 as cv

def get_sobel_filters():
    """
    Returns the Sobel filters for edge detection.
    :return: Sobel filters for x and y direction
    """
    kernel_x = np.array([[-np.sqrt(2)/4, 0, np.sqrt(2)/4],
                         [-1, 0, 1],
                         [-np.sqrt(2)/4, 0, np.sqrt(2)/4]])

    kernel_y = np.array([[-np.sqrt(2)/4, -1, -np.sqrt(2)/4],
                         [0, 0, 0],
                         [np.sqrt(2)/4, 1, np.sqrt(2)/4]])

    return kernel_x, kernel_y