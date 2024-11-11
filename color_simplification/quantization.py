import cv2 as cv
import numpy as np

def quantize_colors_kmeans(image, k=8):
    """
    Applies color quantization using K-Means clustering.

    Parameters:
    - image: Original image (numpy array).
    - k: Number of clusters/colors.

    Returns:
    - quantized_image: Image with quantized colors.
    """
    data = image.reshape((-1, 3))
    data = np.float32(data)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv.kmeans(data, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

    centers = np.uint8(centers)
    quantized_image = centers[labels.flatten()]
    quantized_image = quantized_image.reshape(image.shape)

    return quantized_image
