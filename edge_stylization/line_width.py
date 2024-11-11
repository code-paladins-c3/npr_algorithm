import cv2 as cv
import numpy as np

def adjust_line_width(edge_map, min_width, max_width):
    
    edge_strenght = cv.distanceTransform(225 - edge_map, cv.DIST_L2, 3)
    normalized_edge_strenght = cv.normalize(edge_strenght, None, 0, 1, cv.NORM_MINMAX)
    
    