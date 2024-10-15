import cv2 as cv

def apply_median_filter(gray_img, kernel_size=3):

    return cv.medianBlur(gray_img, kernel_size)
