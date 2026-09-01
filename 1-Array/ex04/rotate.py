import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt
from load_image import ft_load
from PIL import Image


def ft_crop(image: ndarray, size: int = 400, channel: str = "gray") -> ndarray:
    """Crops the given image to the specified size and channel."""
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
    if channel == "gray":
        zoomed = np.expand_dims(zoomed, axis=-1)
    print(f"The shape of image is: {zoomed.shape}",
          f"or ({zoomed.shape[0]}, {zoomed.shape[1]})")
    return zoomed


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


def main() -> None:
    """Main function to demonstrate loading an image."""
    try:
        image = ft_load("/home/nkarapet/Downloads/animal.jpeg")
        print(image)
        cropped_image = ft_crop(image, size=400, channel="gray")
        print(cropped_image)
        rotated_image = ft_rotate(cropped_image, angle=270)
        print(f"New shape after Transpose: {rotated_image.shape}")
        print(rotated_image)
        save_image(rotated_image, jpg_name="rotated_image.jpg")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    """Main entry point of the script."""
    main()
