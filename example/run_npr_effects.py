import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.image_io import read_image, save_image
from utils.view import display_image
from npr_effects.cartoon import apply_cartoon_effect
from npr_effects.pencil import apply_pencil_sketch, apply_pencil_sketch_with_texture
from npr_effects.hatching_effect import apply_hatching_effect

image = read_image('input/knight.jpeg')

#cartoon_image = apply_cartoon_effect(image, num_posterization_levels=4)
#save_image('output/cartoon_effect.jpg', cartoon_image)
#display_image('Cartoon Effect', cartoon_image, 1000)

#sketch_image = apply_pencil_sketch(image, blend_factor=0.5)
#save_image('output/pencil_sketch.jpg', sketch_image)
#display_image('Pencil Sketch', sketch_image, 1000)

#sketch_texture_image = apply_pencil_sketch_with_texture(image, 'texture/paper_texture.jpg', blend_factor=0.5)
#save_image('output/pencil_sketch_with_texture.jpg', sketch_texture_image)
#display_image('Pencil Sketch with Texture', sketch_texture_image, 1000)

hatched_image = apply_hatching_effect(image, patterns_dir='texture/hatching_patterns', num_levels=5)
save_image('output/hatched_image.jpg', hatched_image)
display_image('Hatching Effect', hatched_image, 10000)
