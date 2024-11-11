import cv2 as cv
import numpy as np
import os

def create_hatching_pattern(angle, spacing=10, size=(100, 100)):
    """
    Creates a hatching pattern image at a specified angle.

    Parameters:
    - angle: Angle in degrees for the hatching lines.
    - spacing: Spacing between the hatching lines.
    - size: Size of the output pattern image.

    Returns:
    - pattern: Hatching pattern image.
    """
    pattern = np.ones(size, dtype=np.uint8) * 255  # Start with a white image
    tan_angle = np.tan(np.deg2rad(angle))
    h, w = size

    for x in range(-w, w, spacing):
        pt1 = (int(x), 0)
        pt2 = (int(x + h * tan_angle), h)
        cv.line(pattern, pt1, pt2, color=0, thickness=1)

    return pattern

def apply_hatching(image, intensity_map, patterns_dir, num_levels=5):
    """
    Applies hatching to an image based on intensity levels.

    Parameters:
    - image: Original image.
    - intensity_map: Grayscale image representing intensity or gradient magnitude.
    - patterns_dir: Directory containing hatching patterns.
    - num_levels: Number of intensity levels.

    Returns:
    - hatched_image: Image with hatching applied.
    """
    intensity_map = cv.normalize(intensity_map, None, 0, num_levels - 1, cv.NORM_MINMAX)
    intensity_map = intensity_map.astype(np.uint8)

    h, w = image.shape[:2]
    hatched_image = np.ones((h, w), dtype=np.uint8) * 255  # Start with a white image

    patterns = []
    for i in range(num_levels):
        pattern_path = os.path.join(patterns_dir, f'hatch{i+1}.png')
        pattern = cv.imread(pattern_path, cv.IMREAD_GRAYSCALE)
        if pattern is None:
            raise FileNotFoundError(f'Hatching pattern not found: {pattern_path}')
        patterns.append(pattern)

    for level in range(num_levels):
        mask = (intensity_map == level).astype(np.uint8) * 255
        pattern = cv.resize(patterns[level], (w, h), interpolation=cv.INTER_NEAREST)
        pattern_masked = cv.bitwise_and(pattern, pattern, mask=mask)
        hatched_image = cv.bitwise_and(hatched_image, pattern_masked)

    hatched_image_bgr = cv.cvtColor(hatched_image, cv.COLOR_GRAY2BGR)

    return hatched_image_bgr