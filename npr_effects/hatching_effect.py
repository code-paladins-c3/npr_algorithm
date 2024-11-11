import cv2 as cv
import numpy as np
from edge_detection.canny_edge import modified_canny_detector
from edge_stylization.hatching import apply_hatching
from edge_stylization.edge_coloring import color_edges
from edge_stylization.line_width import adjust_line_width

def apply_hatching_effect(image, patterns_dir='texture/hatching_patterns', num_levels=5, use_gradient=True):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    edges = modified_canny_detector(image)
    thick_edges = adjust_line_width(edges, min_thickness=1, max_thickness=2)
    colored_edges = color_edges(thick_edges, color=(0, 0, 0))

    if use_gradient:
        grad_x = cv.Sobel(gray_image, cv.CV_64F, 1, 0, ksize=3)
        grad_y = cv.Sobel(gray_image, cv.CV_64F, 0, 1, ksize=3)
        gradient_magnitude = cv.magnitude(grad_x, grad_y)
        intensity_map = gradient_magnitude
    else:
        intensity_map = gray_image

    hatched = apply_hatching(image, intensity_map, patterns_dir, num_levels=num_levels)

    hatched_with_edges = cv.addWeighted(hatched, 1, colored_edges, 1, 0)

    return hatched_with_edges
