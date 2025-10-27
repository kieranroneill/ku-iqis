import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_optics_bar_graph(
    single_zero_data: pd.DataFrame, single_one_data: pd.DataFrame, coincidence_data: pd.DataFrame
):
    angles = []
    zero_counts = []
    one_counts = []
    coincidence_counts = []

    for row_angle in single_zero_data.index.astype(str):
        for col_angle in single_zero_data.columns.astype(str):
            angles.append(f"{row_angle}/{col_angle}")
            zero_counts.append(
                single_zero_data.at[row_angle, col_angle] if pd.notna(single_zero_data.at[row_angle, col_angle]) else 0
            )
            one_counts.append(
                single_one_data.at[row_angle, col_angle] if pd.notna(single_one_data.at[row_angle, col_angle]) else 0
            )
            coincidence_counts.append(
                coincidence_data.at[row_angle, col_angle] if pd.notna(coincidence_data.at[row_angle, col_angle]) else 0
            )

    # Create bar positions
    x = np.arange(len(angles))
    width = 0.25

    plt.figure(figsize=(14, 7))
    plt.bar(x - width, zero_counts, width, label="Single 0", color="blue")
    plt.bar(x, one_counts, width, label="Single 1", color="red")
    plt.bar(x + width, coincidence_counts, width, label="Coincidence", color="yellowgreen")

    plt.xlabel("Polarizer 0/1 Angle Pairs (degrees)")
    plt.ylabel("Count Rate")
    plt.title("Photon Count Rates by Polarizer Angle Pairs")
    plt.xticks(ticks=x, labels=angles, rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.show()
