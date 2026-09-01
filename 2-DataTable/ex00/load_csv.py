import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Loads a CSV file from the specified file path
    and returns it as a Dataset object."""
    try:
        if path is None or path == "":
            raise ValueError("Invalid file path.")
        if not path.endswith(".csv"):
            raise ValueError("Unsupported file format. ",
                             "Please provide a .csv file.")
        data = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions", data.shape)
        return data
    except Exception as e:
        print("Error loading dataset:", e)
        return None


def main() -> None:
    """Main function to demonstrate loading a CSV file."""
    try:
        dataset = load("life_expectancy_years.csv")
        if dataset is not None:
            print(dataset)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    """Main entry point of the script."""
    main()
