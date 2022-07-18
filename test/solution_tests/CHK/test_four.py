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

])
def test_checkout(test_input, result):
    assert checkout(test_input) == result
