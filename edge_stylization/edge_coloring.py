import cv2 as cv
import numpy as np

def color_edges(edge_map, color=(0, 0, 0)):
    """
    Colors the edges in the edge map with a specified color.

    Parameters:
    - edge_map: Edge map from custom edge detection.
    - color: Tuple representing the BGR color to apply to the edges.

    Returns:
    - colored_edges: Color image with edges colored.
    """
    colored_edges = np.zeros((*edge_map.shape, 3), dtype=np.uint8)
    colored_edges[edge_map != 0] = color
    return colored_edges