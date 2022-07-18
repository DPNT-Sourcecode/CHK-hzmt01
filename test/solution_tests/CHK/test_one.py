import pytest

from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout():

    @pytest.mark.parametrize("input,result",[
        ("A", 50)
    ])
    def test_checkout(self):
        assert checkout(input) == result
