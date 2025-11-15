def mean(data: list[float]) -> float:
    """
    Calculate the mean of a list of float values.
    """
    return sum(data) / len(data)


def median(data: list[float]) -> float:
    """
    Calculate the median of a list of float values.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        median_value = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        median_value = sorted_data[mid]
    return median_value


def quartiles(data: list[float]) -> tuple[float, float]:
    """
    Calculate the first and third quartiles of a list of float values.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)

    def percentile(p: float) -> float:
        k = (n - 1) * p / 100
        f = int(k)
        c = k - f
        if f + 1 < n:
            return sorted_data[f] + (sorted_data[f + 1] - sorted_data[f]) * c
        else:
            return sorted_data[f]

    q1 = percentile(25)
    q3 = percentile(75)
    return q1, q3


def std(data: list[float]) -> float:
    """
    Calculate the standard deviation of a list of float values.
    """
    mean_value = sum(data) / len(data)
    variance = sum((x - mean_value) ** 2 for x in data) / (len(data))
    std_dev = variance ** 0.5
    return std_dev


def variance(data: list[float]) -> float:
    """
    Calculate the variance of a list of float values.
    """
    mean_value = sum(data) / len(data)
    variance = sum((x - mean_value) ** 2 for x in data) / (len(data))
    return variance


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Calculate and print statistical measures based on provided arguments.

    :param args: Variable length argument list of numerical values.
    :param kwargs: Keyword arguments specifying which statistics to compute.
    """
    data: list[float] = [arg for arg in args if isinstance(arg, (int, float))]
    if not data:
        for _ in range(len(kwargs)):
            print("ERROR")
    for key in kwargs.values():
        match key:
            case "mean":
                if data:
                    print(f"mean: {mean(data)}")
            case "median":
                if data:
                    print(f"median: {median(data)}")

            case "quartile":
                if data:
                    q1, q3 = quartiles(data)
                    print(f"quartiles: [{q1}, {q3}]")
            case "std":
                if len(data) > 1:
                    print(f"std : {std(data)}")
                elif len(data) == 1:
                    print("std : At least two data points required.")
            case "var":
                if len(data) > 1:
                    print(f"var : {variance(data)}")
                elif len(data) == 1:
                    print("var : At least two data points required.")


def main() -> None:
    """Main function to demonstrate the ft_statistics function."""
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
