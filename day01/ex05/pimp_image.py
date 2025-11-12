from numpy import array
import numpy as np


def ft_invert(array) -> array:
    """Inverts the colors of the image."""
    invert_img = 255 - array
    print("Inversion completed.")
    return invert_img


def ft_red(array) -> array:
    """Keeps only the red channel of the image."""
    red_img = array * [1, 0, 0]
    print("Red channel extraction completed.")
    return red_img


def ft_green(array) -> array:
    """Keeps only the green channel of the image."""
    green_img = array.copy()
    green_img[:, :, 0] = 0
    green_img[:, :, 2] = 0
    print("Green channel extraction completed.")
    return green_img


def ft_blue(array) -> array:
    """Keeps only the blue channel of the image."""
    blue_img = array.copy()
    blue_img[:, :, 0] = 0
    blue_img[:, :, 1] = 0
    print("Blue channel extraction completed.")
    return blue_img


def ft_grey(array) -> array:
    """Converts the image to grayscale."""
    gray_img = array.copy()
    gray_img = array[:, :, 0] / 3
    gray_img = array[:, :, 1] / 3
    gray_img = array[:, :, 2] / 3
    print("Grayscale conversion completed.")
    return gray_img.astype(np.uint8)
