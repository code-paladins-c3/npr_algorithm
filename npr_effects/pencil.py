import cv2 as cv
import numpy as np
from edge_detection.canny_edge import modified_canny_detector

def apply_pencil_sketch(image, blend_factor=0.5):
    """
    Applies a pencil sketch effect using custom edge detection.

    Parameters:
    - image: Original BGR image.
    - blend_factor: Blending factor for the final image.

    Returns:
    - sketch_image: Image with pencil sketch effect.
    """
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    inverted_gray = 255 - gray_image

    blurred = cv.GaussianBlur(inverted_gray, (21, 21), 0)

    sketch = cv.divide(gray_image, 255 - blurred, scale=256)

    edges = modified_canny_detector(image)
    edges_inv = 255 - edges

    sketch = cv.multiply(sketch, edges_inv, scale=1/255)

    sketch = cv.normalize(sketch, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)

    sketch_bgr = cv.cvtColor(sketch, cv.COLOR_GRAY2BGR)

    sketch_image = cv.addWeighted(image, 1 - blend_factor, sketch_bgr, blend_factor, 0)

    return sketch_image

def apply_pencil_sketch_with_texture(image, texture_path, blend_factor=0.5):
    """
    Applies a pencil sketch effect and overlays a paper texture.

    Parameters:
    - image: Original BGR image.
    - texture_path: Path to the texture image.
    - blend_factor: Blending factor for the final image.

    Returns:
    - sketch_image: Image with pencil sketch effect and texture.
    """
    sketch_image = apply_pencil_sketch(image, blend_factor)

    texture = cv.imread(texture_path, cv.IMREAD_GRAYSCALE)
    texture = cv.resize(texture, (image.shape[1], image.shape[0]))

    texture = texture.astype(np.float32) / 255.0

    sketch_texture = cv.multiply(sketch_image.astype(np.float32) / 255.0, cv.cvtColor(texture, cv.COLOR_GRAY2BGR))

    sketch_texture = (sketch_texture * 255).astype(np.uint8)

    return sketch_texture
