import numpy as np


def validate_inputs(height: list[int | float],
                    weight: list[int | float]) -> None:
    """Validate the input lists for BMI calculation."""
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")
    elif type(height) is not list or type(weight) is not list:
        raise ValueError("Height and weight must be lists.")
    elif len(height) == 0 or len(weight) == 0:
        raise ValueError("Height and weight lists must not be empty.")
    elif not all(isinstance(h, (int, float)) for h in height):
        raise ValueError("All height values must be integers or floats.")
    elif not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError("All weight values must be integers or floats.")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI values from height and weight lists."""
    height_array = np.array(height)
    weight_array = np.array(weight)
    bmi_array = weight_array / (height_array ** 2)
    return bmi_array.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list indicating which BMI values exceed the given limit."""
    bmi_array = np.array(bmi)
    limit_array = bmi_array > limit
    return limit_array.tolist()


def main() -> None:
    """Main function to demonstrate BMI calculation and limit application."""
    heights = [2.71, 1.15, 1.8, 1.75]
    weights = [165.3, 38.4, 80.5, 70.2]

    try:
        validate_inputs(heights, weights)
        bmi = give_bmi(heights, weights)
        print("BMI values:", bmi)
        limit = 23
        above_limit = apply_limit(bmi, limit)
        print(f"BMI values above {limit}:", above_limit)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
