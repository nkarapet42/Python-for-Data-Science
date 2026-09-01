import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def convert_population(value: str) -> list[float]:
    """
    Converts population strings
    with suffixes 'k' and 'M' to float values.
    """
    result = []
    for v in value:
        if v.endswith('k'):
            result.append(float(v[:-1]) / 1_000)
        elif v.endswith('M'):
            result.append(float(v[:-1]))
        else:
            result.append(float(v) / 1_000_000)
    return result


def aff_pop(data: pd.DataFrame, country: list[str]) -> None:
    """
    Displays the population over the years
    for the specified country or countries.
    """
    try:
        if data is None or data.empty:
            raise ValueError("The provided dataset is empty or None.")
        elif country is None or country == "" or len(country) == 0:
            raise ValueError("Country name must be provided.")
        elif not isinstance(country, list):
            raise ValueError("Country parameter must",
                             " be a list of country names.")
        elif len(country) != 2:
            raise ValueError("Please provide exactly two country names.")
        elif not all(isinstance(c, str) for c in country):
            raise ValueError("All country names must be strings.")
        population_data = data.loc[country]
        if population_data.empty or population_data.shape[0] != 2:
            raise ValueError(f"No data found for the country: {country}")
        years = data.columns.astype(int)
        mask = years <= 2050
        years = years[mask]
        life_expectancy = population_data.values[:, mask]
        life_expectancy = [convert_population(life_expectancy[i])
                           for i in range(2)]
        plt.figure(figsize=(10, 5))
        plt.plot(years, life_expectancy[0], label=country[0], color='blue')
        plt.plot(years, life_expectancy[1], label=country[1], color='green')
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.xticks(range(min(years), 2051, 40))
        plt.ylabel("Population")
        plt.yticks([20, 40, 60], ['20M', '40M', '60M'])
        plt.legend()
        plt.grid(True)
        plt.savefig(f"{country[0]}_{country[1]}_population.png")
    except Exception as e:
        raise Exception(f"An error occurred while plotting the data: {e}")


def main() -> None:
    """Main function to demonstrate loading a CSV file."""
    try:
        dataset = load("population_total.csv")
        if dataset is not None:
            aff_pop(dataset, ["Armenia", "France"])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    """Main entry point of the script."""
    main()
