import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def aff_life(data: pd.DataFrame, country: str) -> None:
    """Plots life expectancy over the years using the provided DataFrame."""
    try:
        if data is None or data.empty:
            raise ValueError("The provided dataset is empty or None.")
        elif country is None or country == "":
            raise ValueError("Country name must be provided.")
        country_data: pd.Series = data.loc[country]
        if country_data.empty:
            raise ValueError(f"No data found for the country: {country}")
        years = country_data.index.astype(int)
        life_expectancy = country_data.to_numpy(dtype=float)

        plt.figure(figsize=(10, 5))
        plt.plot(years, life_expectancy, color='blue')
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.xticks(range(int(years.min()), int(years.max()) + 1, 40))
        plt.ylabel("Life expectancy")
        plt.grid(True)
        plt.savefig(f"{country}_life_expectancy.png")
    except Exception as e:
        raise Exception(f"An error occurred while plotting the data: {e}")


def main() -> None:
    """Main function to demonstrate loading a CSV file."""
    try:
        dataset = load("life_expectancy_years.csv")
        if dataset is not None:
            aff_life(dataset, "France")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    """Main entry point of the script."""
    main()
