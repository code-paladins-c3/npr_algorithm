import cv2 as cv
import numpy as np

def apply_pencil_sketch(image, blend_factor=0.5):
    """
    Applies a pencil sketch effect to the image.

    Parameters:
    - image: Original BGR image (numpy array).
    - blend_factor: Blending factor for the final image.

    Returns:
    - sketch_image: Image with pencil sketch effect.
    """
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    inverted_gray = 255 - gray_image

    blurred = cv.GaussianBlur(inverted_gray, (21, 21), 0)

    sketch = cv.divide(gray_image, 255 - blurred, scale=256)

    sketch_bgr = cv.cvtColor(sketch, cv.COLOR_GRAY2BGR)

    sketch_image = cv.addWeighted(image, 1 - blend_factor, sketch_bgr, blend_factor, 0)

    return sketch_image
