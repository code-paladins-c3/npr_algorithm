import cv2 as cv
from edge_detection.canny_edge import modified_canny_detector
from edge_stylization.line_drawing import stylize_edges
from color_simplification.quantization import quantize_colors

def apply_cartoon_effect(image):
    edges = modified_canny_detector(image)
    edges = cv.bitwise_not(edges)

    stylized_edges = stylize_edges(edges, line_thickness=2, smoothing=True)

    simplified_image = quantize_colors(image, k=8)

    cartoon_image = cv.bitwise_and(simplified_image, simplified_image, mask=stylized_edges)

    return cartoon_image
