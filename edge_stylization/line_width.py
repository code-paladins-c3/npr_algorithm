import cv2 as cv
import numpy as np

def adjust_line_width(edge_map, min_thickness=1, max_thickness=3):
    """
    Adjusts the line width of edges based on edge strength.

    Parameters:
    - edge_map: Edge map from custom edge detection
    - min_thickness: Minimum line thickness.
    - max_thickness: Maximum line thickness.

    Returns:
    - thick_edges: Edge map with adjusted line widths.
    """
    edge_strength = cv.distanceTransform(255 - edge_map, cv.DIST_L2, 3)
    normalized_strength = cv.normalize(edge_strength, None, 0, 1.0, cv.NORM_MINMAX)

    thickness_map = (normalized_strength * (max_thickness - min_thickness) + min_thickness).astype(np.uint8)

    thick_edges = np.zeros_like(edge_map)

    contours, _ = cv.findContours(edge_map, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    for cnt in contours:
        mean_thickness = int(np.mean(thickness_map[cnt[:, 0, 1], cnt[:, 0, 0]]))
        cv.drawContours(thick_edges, [cnt], -1, 255, thickness=mean_thickness)

    return thick_edges
