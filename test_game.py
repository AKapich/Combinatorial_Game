from text_game import Token, check4arithmetic, choose_place

# SETUP
r = 3  # colours
k0, k1, k2 = 3, 4, 3  # number of colours in each row
series_lengths = {0: k0, 1: k1, 2: k2}


def test_check4arithmetic():
    """
    The original function checks if the token series consists of an arithmetic subseries of the given colour
    """
    assert (
        check4arithmetic(
            token_serie=[Token(0), Token(1), Token(2), Token(0), Token(2), Token(0)],
            col2check=0,
        )
        == False
    )
    assert (
        check4arithmetic(
            token_serie=[Token(0), Token(1), Token(1), Token(0), Token(2), Token(1)],
            col2check=1,
        )
        == False
    )
    assert (
        check4arithmetic(
            token_serie=[Token(2), Token(0), Token(2), Token(1), Token(2)], col2check=2
        )
        == True
    )


def test_choose_place():
    """
    The original function chooses the minimal place index from set of place indices for places
    where the amount of potential colours put will result in computer's victory
    """
    assert choose_place([Token(1), Token(1), Token(0), Token(2), Token(0)]) == 1
    assert choose_place([Token(0), Token(2), Token(2), Token(0)]) == 2
    assert choose_place([Token(0), Token(1), Token(2), Token(0), Token(1), Token(2)]) == 0
