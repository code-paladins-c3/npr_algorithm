import cv2 as cv
import numpy as np
import os
from edge_stylization.hatching import create_hatching_pattern

def generate_hatching_patterns(patterns_dir, num_levels=5, size=(100, 100)):
    angles = [0, 45, 90, 135, 180]
    spacings = [10, 8, 6, 4, 2]

    if not os.path.exists(patterns_dir):
        os.makedirs(patterns_dir)

    for i in range(num_levels):
        angle = angles[i % len(angles)]
        spacing = spacings[i % len(spacings)]
        pattern = create_hatching_pattern(angle, spacing, size)
        pattern_path = os.path.join(patterns_dir, f'hatch{i+1}.png')
        cv.imwrite(pattern_path, pattern)
        print(f'Saved hatching pattern: {pattern_path}')

if __name__ == "__main__":
    patterns_dir = 'texture/hatching_patterns'
    generate_hatching_patterns(patterns_dir)
