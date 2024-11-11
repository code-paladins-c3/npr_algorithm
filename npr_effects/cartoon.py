import cv2 as cv
import numpy as np
from edge_detection.canny_edge import modified_canny_detector
from edge_stylization.line_width import adjust_line_width
from edge_stylization.edge_coloring import color_edges
from color_simplification.posterization import posterize_image

def apply_cartoon_effect(image, num_posterization_levels=4):
    """
    Applies a cartoon effect using custom edge detection and posterization.

    Parameters:
    - image: Original BGR image (numpy array).
    - num_posterization_levels: Number of levels for posterization.

    Returns:
    - cartoon_image: Image with cartoon effect.
    """
    edges = modified_canny_detector(image)

    thick_edges = adjust_line_width(edges, min_thickness=1, max_thickness=3)

    colored_edges = color_edges(thick_edges, color=(0, 0, 0))

    posterized_image = posterize_image(image, levels=num_posterization_levels)

    cartoon_image = cv.bitwise_and(posterized_image, posterized_image, mask=255 - thick_edges)

    cartoon_image = cv.addWeighted(cartoon_image, 1, colored_edges, 1, 0)

    return cartoon_image
