import numpy as np

def posterize_image(image, levels=4):
    """
    Posterizes the image by reducing the number of color levels.

    Parameters:
    - image: Original image (numpy array).
    - levels: Number of levels to reduce each color channel to.

    Returns:
    - posterized_image: Posterized image.
    """
    quantization_step = 256 // levels

    posterized_image = (image // quantization_step) * quantization_step + quantization_step // 2

    posterized_image = np.clip(posterized_image, 0, 255).astype(np.uint8)

    return posterized_image