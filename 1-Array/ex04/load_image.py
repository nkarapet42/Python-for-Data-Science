import numpy as np
from numpy import ndarray
from PIL import Image
from rotate import ft_rotate, save_image


def ft_crop(image: ndarray, size: int = 400, channel: str = "gray") -> ndarray:
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
    print(f"The shape of image is: {zoomed.shape}",
          f"or ({zoomed.shape[0]}, {zoomed.shape[1]})")
    return zoomed


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
        cropped_image = ft_crop(image, size=500, channel="rgb")
        print(cropped_image)
        rotated_image = ft_rotate(cropped_image, angle=-90)
        print(rotated_image)
        save_image(rotated_image, jpg_name="rotated_image.jpg")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
