import cv2 as cv
import numpy as np
from edge_detection.canny_edge import modified_canny_detector
from edge_stylization.line_width import adjust_line_width
from edge_stylization.edge_coloring import color_edges
from color_simplification.posterization import posterize_image
from color_simplification.quantization import quantize_colors_kmeans
 
def apply_cartoon_effect(image, num_posterization_levels=4, use_quantization=False):
    """
    Applies a cartoon effect using custom edge detection, bilateral filtering, and color simplification.
 
    Parameters:
    - image: Original BGR image (numpy array).
    - num_posterization_levels: Number of levels for posterization.
    - use_quantization: If True, uses K-Means color quantization instead of posterization.
 
    Returns:
    - cartoon_image: Image with cartoon effect.
    """
    edges = modified_canny_detector(image)
 
    thick_edges = adjust_line_width(edges, min_thickness=1, max_thickness=3)
 
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
    thick_edges = cv.dilate(thick_edges, kernel, iterations=1)
 
    colored_edges = color_edges(thick_edges, color=(0, 0, 0))
 
    num_bilateral_filters = 5
    smooth_image = image.copy()
    for _ in range(num_bilateral_filters):
        smooth_image = cv.bilateralFilter(smooth_image, d=9, sigmaColor=75, sigmaSpace=75)
 
    if use_quantization:
        # Use K-Means color quantization
        simplified_image = quantize_colors_kmeans(smooth_image, k=8)
    else:
        # Use posterization
        simplified_image = posterize_image(smooth_image, levels=num_posterization_levels)
 
    mask = 255 - thick_edges
    cartoon_image = cv.bitwise_and(simplified_image, simplified_image, mask=mask)
 
    cartoon_image = cv.addWeighted(cartoon_image, 1, colored_edges, 1, 0)
 
    return cartoon_image
