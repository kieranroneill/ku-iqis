import matplotlib.pyplot as plt
from pandas import DataFrame


def plot_optics_coincidence_heatmap(data: DataFrame):
    """
    Plots a heatmap of the coincidence counts for the polarizer optics

    Parameters
    ----------
    data : pandas.DataFrame
        The data to plot.
    """

    plt.figure(figsize=(8, 6))
    plt.imshow(data.fillna(0), cmap="viridis", interpolation="nearest")
    plt.colorbar(label="Coincidence Count Rate")
    plt.title("Coincidence Count Rates Heatmap")
    plt.xticks(range(len(data.columns)), data.columns)
    plt.yticks(range(len(data.index)), data.index)
    plt.xlabel("Polarizer 0 Angles (degrees)")
    plt.ylabel("Polarizer 1 Angles (degrees)")
    plt.show()
