from .samplepmf import repeated_sample_sum, pmf
import random

points_for_soul = [
    [1, 2, 3, 6, 30, 70],
    [5, 6, 12, 30, 135, 300],
    [15, 20, 40, 100, 450, 1000]
]

mortal_rarity_probabilities = [0.66, 0.28, 0.06]
immortal_rarity_probabilities = [0.46, 0.42, 0.12]
eternal_rarity_probabilities = [0, 0.8, 0.2]

mortal_rank_probabilities = [0.48, 0.34, 0.12, 0.04, 0.015, 0.005]
immortal_rank_probabilities = [0, 0, 0.52, 0.32, 0.12, 0.04]
eternal_rank_probabilities = [0, 0, 0, 0, 0.8, 0.2]

def get_pmf(rarity_probabilities, rank_probabilities):
    probabilities = []
    values = []
    for rarity_index in range(len(rarity_probabilities)):
        for rank_index in range(len(rank_probabilities)):
            probabilities.append(rarity_probabilities[rarity_index] * rank_probabilities[rank_index])
            values.append(points_for_soul[rarity_index][rank_index])
    return pmf(probabilities = probabilities, values = values)

def get_mortal_pmf():
    return get_pmf(mortal_rarity_probabilities, mortal_rank_probabilities)

def get_immortal_pmf():
    return get_pmf(immortal_rarity_probabilities, immortal_rank_probabilities)

def get_eternal_pmf():
    return get_pmf(eternal_rarity_probabilities, eternal_rank_probabilities)

def get_points_for_n_trials(n, num_mortal, num_immortal, num_eternal):
    mortal_points = repeated_sample_sum(n, num_mortal, get_mortal_pmf())
    immortal_points = repeated_sample_sum(n, num_immortal, get_immortal_pmf())
    eternal_points = repeated_sample_sum(n, num_eternal, get_eternal_pmf())
    total_points = []
    for i in range(n):
        total_points.append(mortal_points[i] + immortal_points[i] + eternal_points[i])
    return total_points