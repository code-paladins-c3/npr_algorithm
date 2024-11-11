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
    pattern = np.ones(size, dtype=np.uint8) * 255
    h, w = size
    angle_rad = np.deg2rad(angle)

    if np.isclose(np.cos(angle_rad), 0, atol=1e-6):
        for x in range(0, w, spacing):
            pt1 = (x, 0)
            pt2 = (x, h)
            cv.line(pattern, pt1, pt2, color=0, thickness=1)
    else:
        tan_angle = np.tan(angle_rad)
        for x in range(-w, w * 2, spacing):
            x1 = int(x)
            y1 = 0
            x2 = int(x + h * tan_angle)
            y2 = h
            pt1 = (x1, y1)
            pt2 = (x2, y2)
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
    intensity_map = (num_levels - 1) - intensity_map
    intensity_map = intensity_map.astype(np.uint8)

    h, w = image.shape[:2]
    hatched_image = np.zeros((h, w), dtype=np.uint8)

    patterns = []
    for i in range(num_levels):
        pattern_path = os.path.join(patterns_dir, f'hatch{i+1}.png')
        pattern = cv.imread(pattern_path, cv.IMREAD_GRAYSCALE)
        if pattern is None:
            raise FileNotFoundError(f'Hatching pattern not found: {pattern_path}')
        pattern = cv.resize(pattern, (w, h), interpolation=cv.INTER_NEAREST)
        cv.imwrite(f'output/resized_pattern_{i+1}.png', pattern)
        patterns.append(pattern)

    for level in range(num_levels):
        mask = (intensity_map == level).astype(np.uint8) * 255
        pattern = patterns[level]
        pattern_masked = cv.bitwise_and(pattern, pattern, mask=mask)

        cv.imwrite(f'output/mask_level_{level}.png', mask)
        cv.imwrite(f'output/pattern_masked_level_{level}.png', pattern_masked)
        
        hatched_image = cv.addWeighted(hatched_image, 1, pattern_masked, 0.5, 0)


    hatched_image = 255 - hatched_image

    hatched_image_bgr = cv.cvtColor(hatched_image, cv.COLOR_GRAY2BGR)

    return hatched_image_bgr
