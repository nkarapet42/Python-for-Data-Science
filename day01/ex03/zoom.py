from numpy import ndarray
from matplotlib import pyplot as plt


def save_image(image: ndarray,
               title: str = "Image", jpg_name: str = "output.jpg") -> None:
    """Displays the image with axes."""
    plt.imshow(image, cmap="gray")
    plt.title(title)
    plt.savefig(jpg_name)


def ft_zoom(image: ndarray, zoom_factor: float = 2.0) -> ndarray:
    """
    Zooms into the center of the image by the given zoom factor.
    Example: zoom_factor=2 means crop to the central 1/2 width and height.
    """
    h, w, _ = image.shape
    new_h = int(h / zoom_factor)
    new_w = int(w / zoom_factor)
    start_y = (h - new_h) // 2
    start_x = (w - new_w) // 2

    zoomed = image[start_y:start_y + new_h, start_x:start_x + new_w]
    print(f"New shape after slicing: {zoomed.shape} or ({new_h}, {new_w})")
    return zoomed
