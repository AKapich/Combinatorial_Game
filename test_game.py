from text_game import __check4arithmetic, choose_place

# SETUP
r = 3  # colours
k0, k1, k2 = 3, 4, 3  # number of colours in each row
series_lengths = {0: k0, 1: k1, 2: k2}


def test_check4arithmetic():
    """
    The original function checks if the token series consists of an arithmetic subseries of the given colour
    """
    assert (
        __check4arithmetic(
            token_serie=[0, 1, 2, 0, 2, 0],
            col2check=0,
        )
        == False
    )
    assert (
        __check4arithmetic(
            token_serie=[0, 1, 1, 0, 2, 1],
            col2check=1,
        )
        == False
    )
    assert __check4arithmetic(token_serie=[2, 0, 2, 1, 2], col2check=2) == True


# def test_choose_place():
#     """
#     The original function chooses the minimal place index from set of place indices for places
#     where the amount of potential colours put will result in computer's victory
#     """
#     assert choose_place([1, 1, 0, 2, 0]) == 1
#     assert choose_place([0, 2, 2, 0]) == 2
#     assert choose_place([0, 1, 2, 0, 1, 2]) == 0
