import matplotlib.pyplot as plt
from pandas import DataFrame


def plot_photon_arrival_time_histogram(data: DataFrame, title: str = "Photon Arrival Time"):
    """
    Plots the histogram of photon arrival times.

    Parameters
    ----------
    data : pandas.DataFrame
        The pandas data to plot.
    title : str, optional
        A custom title for the histogram, by default "Photon Arrival Time".
    """
    x_label = data.columns[0]
    y_label = data.columns[1]

    plt.figure(figsize=(8, 5))
    plt.bar(data[x_label], data[y_label], width=2)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.tight_layout()
    plt.show()
