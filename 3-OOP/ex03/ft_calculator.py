class calculator:
    """
        A simple calculator class that performs arithmetic operations
        on a list of float values.
    """
    def __init__(self, values: list[float]) -> None:
        self.values = values

    def __add__(self, object) -> None:
        for i in range(len(self.values)):
            self.values[i] += object
        print(self.values)

    def __mul__(self, object) -> None:
        for i in range(len(self.values)):
            self.values[i] *= object
        print(self.values)

    def __sub__(self, object) -> None:
        for i in range(len(self.values)):
            self.values[i] -= object
        print(self.values)

    def __truediv__(self, object) -> None:
        if object == 0:
            print("Error: Division by zero is not allowed.")
            return
        for i in range(len(self.values)):
            self.values[i] /= object
        print(self.values)


def main() -> None:
    """
        Main function to demonstrate the calculator class functionality.
    """
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    v3 / 0


if __name__ == "__main__":
    main()
