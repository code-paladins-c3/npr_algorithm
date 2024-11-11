import cv2 as cv


def read_image(filename):
    """
    Reads an image from the specified file path.

    Parameters:
    - filename: Path to the image file.

    Returns:
    - image: Image read from the file.
    """
    return cv.imread(filename)

def save_image(filename, image):
    """
    Saves an image to the specified file path.

    Parameters:
    - filename: Path to save the image.
    - image: Image to save.
    """
    cv.imwrite(filename, image)
