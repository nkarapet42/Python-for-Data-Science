import numpy as np
from numpy import ndarray
from PIL import Image
from zoom import save_image, ft_zoom


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


def main() -> None:
    """Main function to demonstrate loading an image."""
    try:
        image = ft_load("/home/nkarapet/Downloads/animal.jpeg")
        print(image)
        zoomed_image = ft_zoom(image, size=500, channel="rgb")
        print(zoomed_image)
        save_image(zoomed_image, "Zoomed Image", "zoomed_output.jpg")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
