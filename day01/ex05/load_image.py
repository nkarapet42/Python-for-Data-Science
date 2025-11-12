import numpy as np
from numpy import ndarray
from PIL import Image
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey


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


def main() -> None:
    """Main function to demonstrate loading an image."""
    try:
        image = ft_load("/home/nkarapet/Downloads/landscape.jpg")
        print(image)
        save_image(ft_invert(image), jpg_name="inverted_image.jpg")
        save_image(ft_red(image), jpg_name="red_image.jpg")
        save_image(ft_green(image), jpg_name="green_image.jpg")
        save_image(ft_blue(image), jpg_name="blue_image.jpg")
        save_image(ft_grey(image), jpg_name="grey_image.jpg")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
