import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt


def save_image(image: ndarray,
               title: str = "Image", jpg_name: str = "output.jpg") -> None:
    """Saves the image with axes."""
    plt.imshow(image, cmap="gray"
               if image.ndim == 2
               or image.shape[-1] == 1 else None)
    plt.title(title)
    plt.savefig(jpg_name)


def ft_rotate(image: ndarray, angle: float) -> ndarray:
    """Rotates the given image by the specified angle in degrees.

    Args:
        image (ndarray): The input image as a NumPy array.
        angle (float): The angle in degrees to rotate the image.

    Returns:
        ndarray: The rotated image as a NumPy array.
    """
    theta = np.radians(angle)
    cos_theta, sin_theta = np.cos(theta), np.sin(theta)

    h, w = image.shape[:2]
    center_x, center_y = w / 2, h / 2

    rotated_image = np.zeros_like(image)

    for y in range(h):
        for x in range(w):
            x_shifted = x - center_x
            y_shifted = y - center_y

            x_rotated = int(cos_theta * x_shifted
                            + sin_theta * y_shifted + center_x)
            y_rotated = int(-sin_theta * x_shifted
                            + cos_theta * y_shifted + center_y)
            if 0 <= x_rotated < w and 0 <= y_rotated < h:
                rotated_image[y, x] = image[y_rotated, x_rotated]
    return rotated_image
