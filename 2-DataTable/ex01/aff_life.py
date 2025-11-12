import matplotlib.pyplot as plt
from load_csv import Dataset


def aff_life(data: Dataset, country: str) -> None:
    """Plots life expectancy over the years using the provided DataFrame."""
    try:
        if data is None or data.data.empty:
            raise ValueError("The provided dataset is empty or None.")
        elif country is None or country == "":
            raise ValueError("Country name must be provided.")
        country_data = data.data.loc[country]
        if country_data.empty:
            raise ValueError(f"No data found for the country: {country}")
        years = country_data.index.astype(int)
        life_expectancy = country_data.values.astype(float)

        plt.figure(figsize=(10, 5))
        plt.plot(years, life_expectancy, color='blue')
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.xticks(range(min(years), max(years) + 1, 40))
        plt.ylabel("Life expectancy")
        plt.grid(True)
        plt.savefig(f"{country}_life_expectancy.png")
    except Exception as e:
        raise Exception(f"An error occurred while plotting the data: {e}")
