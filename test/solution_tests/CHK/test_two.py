import pytest

from lib.solutions.CHK.checkout_solution import checkout, offer


@pytest.mark.parametrize("test_input,result",[
    (1, 50),
    (2,100),
    (3,130),
    (4,180),
    (5,200),
    (6,250),
])
def test_offer(test_input, result):
    assert offer(
        test_input,
        [
            (1, 50),
            (3, 130),
            (5, 200)
        ]) == result


@pytest.mark.parametrize("test_input,result",[
    ("AAA", 130),
    ("B", 30),
    ("BB", 45),
    ("BBBE", 115),
    ("BBBEE", 125),
    ("BBBEe", -1),
    ("C", 20),
    ("D", 15),

])
def test_checkout(test_input, result):
    assert checkout(test_input) == result
