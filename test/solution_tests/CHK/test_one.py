import pytest

from lib.solutions.CHK.checkout_solution import checkout


@pytest.mark.parametrize("test_input,result",[
    ("A", 50),
    ("AA", 100),
    ("AAA", 130),
    ("AAAA", 180),
    ("B", 30),
    ("BB", 45),
    ("BBB", 75)
    ("C", 20),
    ("CC", 40),
    ("D", 15),
    ("DD", 30),
])
def test_checkout(test_input, result):
    assert checkout(test_input) == result

