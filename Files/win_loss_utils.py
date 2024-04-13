from itertools import combinations
from copy import deepcopy
from game_config import SequenceConfig, game_colors
import random


def check4arithmetic(token_serie, config):
    series_lengths = [sequence.length for sequence in config]
    colors = [sequence.color for sequence in config]

    for col2check in range(len(colors)):
        arithmetic_present = __check4arithmetic(token_serie, series_lengths, col2check)
        if arithmetic_present:
            return True

    return False


def __check4arithmetic(token_serie, series_lengths, col2check):
    """
    The function checks if the token series consists of an arithmetic subseries of the given colour
    """
    colour_indices = [
        index for index, col in enumerate(token_serie) if col == col2check
    ]
    mlos = series_lengths[col2check]  # minimun length of series

    if len(colour_indices) < mlos:  # series must be at least of the given length
        return False

    combinations_list = list(
        combinations(colour_indices, mlos)
    )  # every combination of mlos length
    for comb in combinations_list:
        is_subseries_arithmetic = True
        for i in range(len(comb) - 2):
            if comb[i] + comb[i + 2] != 2 * comb[i + 1]:
                is_subseries_arithmetic = False
                break
        if is_subseries_arithmetic:
            return True

    return False


def choose_place(token_serie: list[int], config: list[SequenceConfig]):
    """
    The function chooses the minimal place index from set of place indices for places
    where the amount of potential colours put will result in computer's victory
    """
    if len(token_serie) == 0:
        return 0

    series_lengths = [sequence.length for sequence in config]
    colors = [sequence.color for sequence in config]

    combinations_dict = {}

    for place2insert in range(len(token_serie) + 1):
        new_serie = deepcopy(token_serie)
        new_serie.insert(place2insert, None)
        how_many_arithmetic = 0  # how many colours put in the chosen place will create an arithmetic serie

        for col2check in range(len(colors)):
            new_serie[place2insert] = col2check
            arithmetic_present = __check4arithmetic(
                new_serie, series_lengths, col2check
            )
            if arithmetic_present:
                how_many_arithmetic += 1

        combinations_dict[place2insert] = how_many_arithmetic

    max_value = max(combinations_dict.values())
    best_places = [
        place for place, value in combinations_dict.items() if value == max_value
    ]
    return random.choice(best_places)
