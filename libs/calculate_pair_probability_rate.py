from pandas import DataFrame

from libs.convert_picoseconds_to_seconds import convert_picoseconds_to_seconds


def calculate_pair_probability_rate(data: DataFrame, repetition_rate: float) -> float:
    time_difference_label = data.columns[0]
    counts_per_bin_label = data.columns[1]
    pair_peak_min = -500
    pair_peak_max = 500
    pair_data = data[(data[time_difference_label] >= pair_peak_min) & (data[time_difference_label] <= pair_peak_max)]
    total_pair_count = pair_data[counts_per_bin_label].sum()

    return total_pair_count / repetition_rate
