def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Raises x to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Outer function that returns an inner function which counts calls."""
    count = 0

    def inner() -> float:
        """Inner function that increment count and calls the given function."""
        nonlocal count
        count += 1
        res = x
        for _ in range(count):
            res = function(res)
        return res
    return inner


def main() -> None:
    """Main function to demonstrate the outer function."""
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
