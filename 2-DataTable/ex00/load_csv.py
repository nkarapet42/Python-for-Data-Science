import pandas as pd


class Dataset:
    """A simple Dataset class to hold data."""
    def __init__(self, data: pd.DataFrame):
        self.data = data


def load(path: str) -> Dataset | None:
    """Loads a CSV file from the specified file path
    and returns it as a Dataset object."""
    try:
        if path is None or path == "":
            return None
        if not path.endswith(".csv"):
            raise ValueError("Unsupported file format. ",
                             "Please provide a .csv file.")
        data = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions", data.shape)
        return Dataset(data)
    except Exception as e:
        raise Exception(f"An error occurred while loading the CSV file: {e}")


def main() -> None:
    """Main function to demonstrate loading a CSV file."""
    try:
        dataset = load("/home/nkarapet/Downloads/life_expectancy_years.csv")
        if dataset is not None:
            print(dataset.data)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
