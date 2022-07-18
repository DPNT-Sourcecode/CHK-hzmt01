import pytest

from lib.solutions.CHK.checkout_solution import checkout, offer


@pytest.mark.parametrize("test_input,char,result",[
    ("A","A", 50),
    ("AA", "A",100),
    ("AAA", "A",130),
    ("AAAA", "A",180),
    ("AAAAA", "A",200),
    ("AAAAAA", "A",250),
    ("B","B",30),
    ("BB","B",45),
    ("AABB","B",45)
    
])
def test_offer(test_input, char, result):
    assert offer(
        test_input,
        char,
        [
            (1, 50),
            (3, 130),
            (5, 200)
        ]) == result



