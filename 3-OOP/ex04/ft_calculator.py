class calculator:
    """
        A simple calculator class that performs arithmetic operations
        on a list of float values.
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [a + b for a, b in zip(V1, V2)]
        print(f"Add Vector is : {[float(x) for x in result]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [a - b for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {[float(x) for x in result]}")


def main() -> None:
    """
        Main function to demonstrate the calculator class functionality.
    """
    a = [5.0, 10.0, 2.0]
    b = [2.0, 4.0, 3.0]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    """Main entry point of the script."""
    main()
