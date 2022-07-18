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




