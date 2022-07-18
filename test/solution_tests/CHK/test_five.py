import pytest

from lib.solutions.CHK.checkout_solution import checkout, get_group_count


@pytest.mark.parametrize(
    "count_dict, group_size, total_groups", [
        (
            {"S" : 0, "T" : 1, "X" : 3 ,"Y" : 5, "Z" : 5},
            3,
            4,
        ),
        (
            {"S" : 0, "T" : 1, "X" : 3 ,"Y" : 5, "Z" : 5},
            4,
            1
        ),
        (
            {"S" : 0, "T" : 1, "X" : 3 ,"Y" : 5, "Z" : 5},
            5,
            0
        ),
        (
            {"S" : 0, "T" : 1, "X" : 3 ,"Y" : 5, "Z" : 5},
            2,
            7
        ),
    ]
)
def test_grouping(count_dict, group_size, total_groups):
    assert get_group_count(
        count_dict,
        (("S", 20),("T",20),("X",17),("Y",20),("Z",21)),
        group_size
    ) == total_groups




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
    ("K", 70),
    ("KK", 120),
    ("NNNMM", 135),
    ("P", 50),
    ("PPPPP", 200),
    ("RRRQQ", 180),
    ("RRR", 150),
    ("U", 40),
    ("UUU", 120),
    ("UUUU", 120),
    ("STXYZ", 82)

])
def test_checkout(test_input, result):
    assert checkout(test_input) == result

