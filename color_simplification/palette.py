import cv2 as cv
import numpy as np

def apply_color_palette(image, palette):
    """
    Applies a specified color palette to an image.

    Parameters:
    - image: Original image.
    - palette: List of BGR color tuples to map the image to.

    Returns:
    - palette_image: Image with applied color palette.
    """
    pixel_data = image.reshape((-1, 3))
    
    pixel_data = np.float32(pixel_data)

    k = len(palette)
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, _ = cv.kmeans(pixel_data, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

    palette = np.array(palette, dtype=np.uint8)
    quantized_pixels = palette[labels.flatten()]
    
    palette_image = quantized_pixels.reshape(image.shape)

    return palette_image