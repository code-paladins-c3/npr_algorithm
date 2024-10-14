import cv2 as cv

def apply_median_filter(gray_img, kernel_size=3):
    """
    Applies a median filter to the input image to reduce noise.
    :params: input gray scale image, kernel size
    :return: median filtered image
    """
    return cv.medianBlur(gray_img, kernel_size)
