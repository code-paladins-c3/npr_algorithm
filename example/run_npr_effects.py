import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.image_io import read_image, save_image
from utils.view import display_image
from npr_effects.cartoon import apply_cartoon_effect
from npr_effects.pencil import apply_pencil_sketch, apply_pencil_sketch_with_texture

import os

input_folder = 'input'
output_folder = 'output'
texture_path = 'texture/paper_texture.jpg'

for filename in os.listdir(input_folder):
    if filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(input_folder, filename)
        image = read_image(image_path)

        cartoon_image = apply_cartoon_effect(image, num_posterization_levels=4)
        cartoon_output_path = os.path.join(output_folder, f'cartoon_effect_{filename}')
        save_image(cartoon_output_path, cartoon_image)
        display_image('Cartoon Effect', cartoon_image, 10000)

        sketch_texture_image = apply_pencil_sketch_with_texture(image, texture_path, blend_factor=0.5)
        sketch_texture_output_path = os.path.join(output_folder, f'pencil_sketch_with_texture_{filename}')
        save_image(sketch_texture_output_path, sketch_texture_image)
        display_image('Pencil Sketch with Texture', sketch_texture_image, 10000)
