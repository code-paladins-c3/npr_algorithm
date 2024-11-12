import cv2 as cv

def display_image(window_name, image, wait_time):
    """
    Displays an image in a window.

    Parameters:
    - window_name: Name of the window.
    - image: Image to display.
    - wait_time: Time in milliseconds to wait for a key press.
    """
    cv.imshow(window_name, image)
    cv.waitKey(wait_time)
    cv.destroyAllWindows()
