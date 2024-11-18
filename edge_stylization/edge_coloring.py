import cv2 as cv
import numpy as np

def color_edges(edge_map, image=None, color=(0, 0, 0)):

    colored_edges = np.zeros((*edge_map.shape, 3), dtype=np.uint8)

    if image is not None:
        colored_edges[edge_map != 0] = image[edge_map != 0]
    else:
        colored_edges[edge_map != 0] = color

    return colored_edges