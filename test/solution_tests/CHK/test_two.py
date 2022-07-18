import pytest

from lib.solutions.CHK.checkout_solution import checkout, offer


@pytest.mark.parametrize("test_input,result",[
    ("A", 50),
    ("AA", 100),
    ("AAA", 130),
    ("AAAA", 180),
    ("AAAAA", 200),
    ("AAAAAA", 250),
])
def test_offer(test_input, result):
    assert offer(
        test_input,
        "A",
        [
            (1, 50),
            (3, 130),
            (5, 200)
        ]) == result


