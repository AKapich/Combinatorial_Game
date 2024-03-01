import pytest
from game import Token, check4arithmetic, choose_place

# SETUP
r = 3 # colours
k0, k1, k2 = 3, 4, 3 # number of colours in each row
series_lengths = {
    0: k0,
    1: k1,
    2: k2
}

def test_check4arithmetic():
    assert check4arithmetic(token_serie=[Token(0), Token(1), Token(2), Token(0), Token(2), Token(0)], col2check=0) == False
    assert check4arithmetic(token_serie=[Token(0), Token(1), Token(1), Token(0), Token(2), Token(1)], col2check=1) == False
    assert check4arithmetic(token_serie=[Token(2), Token(0), Token(2), Token(1), Token(2)], col2check=2) == True


# def test_choose_place():
#     r1 = [Token(1), Token(1), Token(None), Token(0), Token(2), Token(0)]
#     assert choose_place(token_serie=[Token(1), Token(1), Token(0), Token(2), Token(0)], current_token=Token(None)) == r1