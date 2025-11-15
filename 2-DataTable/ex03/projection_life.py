import matplotlib.pyplot as plt
from load_csv import Dataset


def projection_life(life_data: Dataset, gdp: Dataset) -> None:
    """
    Displays the life expectancy projection og 1900 year
    based on GDP data.
    """
    try:
        if life_data is None or life_data.data.empty:
            raise ValueError("The provided life expectancy"
                             " dataset is empty or None.")
        if gdp is None or gdp.data.empty:
            raise ValueError("The provided GDP dataset is empty or None.")
        print(life_data.data['1900'])
        life_data_1900 = life_data.data['1900']
        print(gdp.data['1900'])
        gdp_1900 = gdp.data['1900']
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
