import pytest

from lib.solutions.CHK.checkout_solution import checkout, OFFERS


def test_config_length():

    assert len(OFFERS) == 26

def test_config_units():

    for offer in OFFERS.values():
        units = set([index[0] for index in offer])

        assert 1 in units




@pytest.mark.parametrize("test_input,result",[
    ("AAA", 130),
    ("B", 30),
    ("BB", 45),
    ("BBBE", 115),
    ("BBBEE", 125),
    ("BBBEe", -1),
    ("C", 20),
    ("D", 15),
    ("F", 10),
    ("FF", 20),
    ("FFF", 20),
    ("AAAFF", 150),
    ("AAAFFF", 150),
    ("H", 10),
    ("HHHHH", 45),
    ("HHHHHHHHHH", 80),
    ("K", 80),
    ("KK", 150),
    ("NNNMM", 135),
    ("P", 50),
    ("PPPPP", 200),
    ("RRRQQ", 180),
    ("RRR", 150),
    ("U", 40),
    ("UUU", 120),
    ("UUUU", 120)

])
def test_checkout(test_input, result):
    assert checkout(test_input) == result
