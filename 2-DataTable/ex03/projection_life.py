import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def projection_life(life_data: pd.DataFrame, gdp: pd.DataFrame) -> None:
    """
    Displays the life expectancy projection og 1900 year
    based on GDP data.
    """
    try:
        if life_data is None or life_data.empty:
            raise ValueError("The provided life expectancy"
                             " dataset is empty or None.")
        if gdp is None or gdp.empty:
            raise ValueError("The provided GDP dataset is empty or None.")
        life_data_1900 = life_data['1900']
        gdp_1900 = gdp['1900']
        plt.figure(figsize=(10, 5))
        plt.scatter(gdp_1900, life_data_1900, color='blue')
        plt.title("1900")
        plt.xscale("log")
        plt.xlabel("Gross domestic product")
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.xlim(300, 10000)
        plt.ylabel("Life Expectancy")
        plt.savefig("projection_life_1900.png")
    except Exception as e:
        raise Exception(f"An error occurred while plotting the data: {e}")


def main() -> None:
    """Main function to demonstrate loading a CSV file."""
    try:
        dataset = load("life_expectancy_years.csv")
        incomedata = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
            )
        if dataset is not None and incomedata is not None:
            projection_life(dataset, incomedata)
        else:
            print("Failed to load dataset.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    """Main entry point of the script."""
    main()
