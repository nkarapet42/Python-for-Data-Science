from calendar import c
import matplotlib.pyplot as plt
from load_csv import Dataset


def aff_pop(data: Dataset, country: list[str]) -> None:
    """
    Displays the population over the years for the specified country or countries.
    """
    try:
        if data is None or data.data.empty:
            raise ValueError("The provided dataset is empty or None.")
        elif country is None or country == "" or len(country) == 0:
            raise ValueError("Country name must be provided.")
        elif not isinstance(country, list):
            raise ValueError("Country parameter must be a list of country names.")
        elif len(country) != 2:
            raise ValueError("Please provide exactly two country names.")
        elif not all(isinstance(c, str) for c in country):
            raise ValueError("All country names must be strings.")
        population_data = data.data.loc[country]
        if population_data.empty or population_data.shape[0] != 2:
            raise ValueError(f"No data found for the country: {country}")
        years = data.data.columns.astype(int)
        life_expectancy = population_data.values
        plt.figure(figsize=(10, 5))
        plt.plot(years, life_expectancy[0], label=country[0], color='blue')
        plt.plot(years, life_expectancy[1], label=country[1], color='green')
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.xticks(range(min(years), max(years) + 1 if max(years) < 2050 else 2050, 40))
        plt.ylabel("Population")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"{country[0]}_{country[1]}_population.png")
    except Exception as e:
        raise Exception(f"An error occurred while plotting the data: {e}")
