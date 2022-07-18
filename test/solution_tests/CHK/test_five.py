import pytest

from lib.solutions.CHK.checkout_solution import checkout, grouping


@pytest.mark.parametrize(
    "count_dict, group_size, group_price, new_dict, total_groups", [
        (
            {"S" : 0, "T" : 1, "X" : 3 ,"Y" : 5, "Z" : 5},
            3,
            45,
            {"S" : 0, "T" : 0, "X" : 0 ,"Y" : 2, "Z" : 2},
            3,
        ),
        (
            {"S" : 0, "T" : 1, "X" : 3 ,"Y" : 5, "Z" : 5},
            4,
            45,
            {"S" : 0, "T" : 0, "X" : 2 ,"Y" : 4, "Z" : 4},
            1,
        )
    ]
)
def test_grouping(count_dict, group_size, group_price, new_dict, total_groups):
    assert grouping(
        count_dict,
        ("S","T","X","Y","Z"),
        group_size
    ) == (new_dict, total_groups)



"""
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
"""



