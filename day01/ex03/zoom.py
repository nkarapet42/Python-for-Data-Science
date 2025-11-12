from PIL import Image
import numpy as np
from numpy import ndarray
from matplotlib import pyplot as plt


def save_image(image: ndarray,
               title: str = "Image", jpg_name: str = "output.jpg") -> None:
    """Displays the image with axes."""
    plt.imshow(image, cmap="gray"
               if image.ndim == 2
               or image.shape[-1] == 1 else None)
    plt.title(title)
    plt.savefig(jpg_name)


def ft_zoom(image: ndarray, zoom_factor: float = float("NaN"),
            size: int = 400, channel: str = "gray") -> ndarray:
    """
    Zooms into the center of the image by the given zoom factor.
    Example: zoom_factor=2 means crop to the central 1/2 width and height.

    Args:
        image (ndarray): The input image as a NumPy array.

        Use:
        1.zoom_factor (float): The factor by which to zoom into the image.
        or
        2.size (int):The size to which the zoomed image should be resized.
          channel (str):The color channel to use ("gray" or "rgb").
    """
    if not zoom_factor != zoom_factor:
        h, w, _ = image.shape
        new_h = int(h / zoom_factor)
        new_w = int(w / zoom_factor)
        start_y = (h - new_h) // 2
        start_x = (w - new_w) // 2

        zoomed = image[start_y:start_y + new_h, start_x:start_x + new_w]
        print(f"New shape after slicing: {zoomed.shape} or ({new_h}, {new_w})")
        return zoomed
    else:
        img = Image.fromarray(image).convert("RGB")
        w, h = img.size

        left = (w - size) // 2
        top = (h - size) // 2
        right = left + size
        bottom = top + size
        img_cropped = img.crop((left, top, right, bottom))

        if channel == "gray":
            img_cropped = img_cropped.convert("L")
        elif channel != "rgb":
            raise ValueError(
                "Invalid channel. "
                "Choose from: gray or rgb."
            )
        zoomed = np.array(img_cropped)
        print(f"New shape after slicing: {zoomed.shape}",
              f"or ({zoomed.shape[0]}, {zoomed.shape[1]})")
        return zoomed
