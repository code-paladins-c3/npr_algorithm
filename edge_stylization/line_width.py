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
    
    if edge_map.dtype != np.uint8:
        edge_map = edge_map.astype(np.uint8)
    if len(edge_map.shape) > 2:
        edge_map = cv.cvtColor(edge_map, cv.COLOR_BGR2GRAY)
        
    edge_map = np.where(edge_map > 0, 255, 0).astype(np.uint8)
    
    inverted_edge_map = 255 - edge_map
    
    edge_strength = cv.distanceTransform(inverted_edge_map, cv.DIST_L2, 3)
    normalized_strength = cv.normalize(edge_strength, None, 0, 1.0, cv.NORM_MINMAX)

    thickness_map = (normalized_strength * (max_thickness - min_thickness) + min_thickness)

    thick_edges = np.zeros_like(edge_map)

    contours, _ = cv.findContours(edge_map, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    for cnt in contours:
        mean_thickness = int(np.mean(thickness_map[cnt[:, 0, 1], cnt[:, 0, 0]]))
        cv.drawContours(thick_edges, [cnt], -1, 255, thickness=mean_thickness)

    return thick_edges
