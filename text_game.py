from itertools import combinations
from copy import deepcopy

r = 3  # colours
k0, k1, k2 = 3, 4, 3  # number of colours in each row
global series_lengths, vizdict
series_lengths = {0: k0, 1: k1, 2: k2}
vizdict = {
    None: "TOKEN",
    0: 0,
    1: 1,
    2: 2,
}
n = 10  # cap for moves


class Token:
    def __init__(self, colour):
        self.colour = colour


def check4arithmetic(token_serie, col2check):
    """
    The function checks if the token series consists of an arithmetic subseries of the given colour
    """
    colour_indices = [
        index for index, token in enumerate(token_serie) if token.colour == col2check
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


def choose_place(token_serie):
    """
    The function chooses the minimal place index from set of place indices for places
    where the amount of potential colours put will result in computer's victory
    """
    current_token = Token(None)
    if len(token_serie) == 0:
        return 0

    combinations_dict = {}

    for place2insert in range(len(token_serie) + 1):
        new_serie = deepcopy(token_serie)
        new_serie.insert(place2insert, current_token)
        how_many_arithmetic = 0  # how many colours put in the chosen place will create an arithmetic serie

        for col2check in range(r):
            current_token.colour = col2check
            arithmetic_present = check4arithmetic(new_serie, col2check)
            if arithmetic_present:
                how_many_arithmetic += 1

        combinations_dict[place2insert] = how_many_arithmetic

    best_place = max(combinations_dict, key=combinations_dict.get)
    return best_place


# GAME
def main():
    token_serie = []
    moves_count = 0
    while moves_count < n:
        # computer chooses place
        best_place = choose_place(token_serie)
        current_token = Token(None)
        token_serie.insert(best_place, current_token)
        print([vizdict[token.colour] for token in token_serie])
        print("\n")

        # agent chooses colour
        while True:
            try:
                colour = int(input(f"Dawaj kolor. [Dostępne kolory 0-{r-1}] "))
            except ValueError:
                print("Dawaj liczbę ")
                continue
            if 0 <= colour <= r - 1:
                break
            else:
                print(f"Dawaj kolor z przedziału 0-{r-1}!  ")
        current_token.colour = colour

        # verify if there's arithmetic serie present
        for col2check in range(r):
            arithmetic_present = check4arithmetic(token_serie, col2check)
            if arithmetic_present:
                print("MMMMMM puuuu")
                exit()

        moves_count += 1
        print([vizdict[token.colour] for token in token_serie])
        print("\nMoves left: ", n - moves_count, "\n")

    print("Elegancko, koniec gry")


if __name__ == "__main__":
    main()
