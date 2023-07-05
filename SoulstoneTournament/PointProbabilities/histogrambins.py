import math

def create_histogram_bins(values, number_bins, anchor):
    values.sort()
    smallest_value = values[0]
    largest_value = values[-1]
    range = largest_value - smallest_value
    if range == 0:
        raise(ValueError("Range of histogram is 0!"))
    bin_size = get_bin_size(range, number_bins)
    bin_ranges = []
    bin_counts = []
    if anchor >= smallest_value and anchor <= largest_value:
        bin_lower = anchor
        while (bin_lower > smallest_value):
            bin_lower -= bin_size
    else:
        bin_lower = smallest_value - (smallest_value % bin_size)
    bin_index = 0
    while bin_index < number_bins:
        bin_upper = bin_lower + bin_size
        bin_ranges.append("[ " + str(bin_lower) + " , " + str(bin_upper) + " )")
        bin_counts.append(get_count_in_bin(bin_lower, bin_size, values))
        bin_lower += bin_size
        bin_index += 1
    histogram_bins = {'bin_ranges': bin_ranges, 'bin_counts' : bin_counts}
    return histogram_bins
    

def get_bin_size(range, number_bins):
    bin_size = range / (number_bins - 1)
    log10 = math.floor(math.log(bin_size, 10))
    bin_size = bin_size / pow(10, log10)
    if (bin_size < 1.5):
        bin_size = 1.5
    else:
        bin_size = math.ceil(bin_size)
    bin_size = bin_size * pow(10, log10)
    return bin_size

def get_count_in_bin(bin_lower, bin_size, values):
    return_sum = 0
    for value in values:
        if value >= bin_lower and value < bin_lower + bin_size:
            return_sum += 1
    return return_sum
    