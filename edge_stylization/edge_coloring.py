import cv2 as cv
import numpy as np

def color_edges(edge_map, image=None, color=(0, 0, 0)):
    """
    Colors the edges in the edge map with a specified color or samples from the image.

    Parameters:
    - edge_map: Edge map from custom edge detection.
    - image: Original image to sample colors if needed (optional).
    - color: Tuple representing the BGR color to apply to the edges.

    Returns:
    - colored_edges: Color image with edges colored.
    """
    colored_edges = np.zeros((*edge_map.shape, 3), dtype=np.uint8)

    if image is not None:
        colored_edges[edge_map != 0] = image[edge_map != 0]
    else:
        colored_edges[edge_map != 0] = color

    return colored_edges