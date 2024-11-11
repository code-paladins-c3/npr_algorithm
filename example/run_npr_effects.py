import cv2 as cv
from utils.image_io import read_image, save_image
from utils.visualization import display_image
from npr_effects.cartoon_effect import apply_cartoon_effect
from npr_effects.pencil_sketch.py import apply_pencil_sketch

image = read_image('input/sample_image.jpg')

cartoon_image = apply_cartoon_effect(image, num_posterization_levels=4)
save_image('output/cartoon_effect.jpg', cartoon_image)
display_image('Cartoon Effect', cartoon_image)

sketch_image = apply_pencil_sketch(image, blend_factor=0.5)
save_image('output/pencil_sketch.jpg', sketch_image)
display_image('Pencil Sketch', sketch_image)