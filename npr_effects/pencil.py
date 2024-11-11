# npr_effects/pencil_sketch.py

import cv2 as cv
import numpy as np
from edge_detection.canny_edge import modified_canny_detector
from edge_stylization.edge_coloring import color_edges

def apply_pencil_sketch(image, blend_factor=0.5):
    """
    Applies a pencil sketch effect using custom edge detection.

    Parameters:
    - image: Original BGR image (numpy array).
    - blend_factor: Blending factor for the final image.

    Returns:
    - sketch_image: Image with pencil sketch effect.
    """
    edges = modified_canny_detector(image)
    edges_inv = 255 - edges  # Invert edges for blending

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    sketch = cv.divide(gray_image, edges_inv, scale=256.0)

    sketch_bgr = cv.cvtColor(sketch, cv.COLOR_GRAY2BGR)

    sketch_image = cv.addWeighted(image, 1 - blend_factor, sketch_bgr, blend_factor, 0)

    return sketch_image
