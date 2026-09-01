import numpy as np
from numpy import ndarray
from PIL import Image


def save_image(image: ndarray, jpg_name: str = "output.jpg") -> None:
    """Saves the image."""
    img = Image.fromarray(image.astype(np.uint8))
    img.save(jpg_name)


def ft_load(path: str) -> ndarray:
    """Loads an image from the specified file path\
and returns it as a NumPy array."""
    try:
        if not path.endswith(".jpg") and not path.endswith(".jpeg"):
            raise ValueError("Unsupported file format. ",
                             "Please provide a .jpg or .jpeg image.")
        with Image.open(path) as img:
            img = img.convert("RGB")
            image = np.array(img)
        print("The shape of image is:", image.shape)
        return image
    except Exception as e:
        raise Exception(f"An error occurred while loading the image: {e}")
