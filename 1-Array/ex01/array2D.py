import numpy as np


def validate_input(family: list) -> None:
    """Validates the input parameters for slicing."""
    if not isinstance(family, list):
        raise ValueError("family must be a 2D list")
    elif not all(isinstance(sublist, list) for sublist in family):
        raise ValueError("family must be a 2D list")
    elif len(family) == 0 or len(family[0]) == 0:
        raise ValueError("family must not be empty")
    else:
        for sublist in family:
            if len(sublist) != len(family[0]):
                raise ValueError("All sublists must have the same length")


def slice_me(family: list, start: int, end: int) -> list:
    """Slices a 2D list from start index to end index."""
    print("My shape is:", np.array(family).shape)
    shaped_array = np.array(family)[start:end]
    print("My new shape is:", shaped_array.shape)
    return shaped_array.tolist()


def main() -> None:
    """Main function to demonstrate slicing a 2D list."""
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]

    try:
        validate_input(family)
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
