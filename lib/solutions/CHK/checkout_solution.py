
OFFERS = {
    "A" : [
        (1, 50),
        (3, 130),
        (5, 200)
    ],
    "B" : [
        (1, 30),
        (2, 45),
    ],
    "C" : [
        (1, 20),
    ],
    "D" : [
        (1, 15),
    ],
    "E" : [
        (1, 40),
    ],
    "F" : [
        (1, 10),
        (3, 20)
    ],
    "G" : [
        (1, 20),
    ],
    "H" : [
        (1, 10),
        (5, 45),
        (10, 80)
    ],
    "I" : [
        (1, 35),
    ],
    "J" : [
        (1, 60),
    ],
    "K" : [
        (1, 80),
        (2, 150)
    ],
    "L" : [
        (1, 90),
    ],
    "M" : [
        (1, 15),
    ],
    "N" : [
        (1, 40),
    ],
    "O" : [
        (1, 10),
    ],
    "P" : [
        (1, 50),
        (5, 200),
    ],
    "Q" : [
        (1, 30),
        (3, 80),
    ],
    "R" : [
        (1, 50),
    ],
    "S" : [
        (1, 30),
    ],
    "T" : [
        (1, 20),
    ],
    "U" : [
        (1, 40),
        (3, 80),
    ],
    "V" : [
        (1, 50),
        (2, 90),
        (3, 130)
    ],
    "W" : [
        (1, 20),
    ],
    "X" : [
        (1, 90),
    ],
    "Y" : [
        (1, 10),
    ],
    "Z" : [
        (1, 50),
    ]
}
def offer(count: int, offers: list):

    """
    computes optimal price in case of repeated offers
    NOTE: assumes for now that the optimal strategy is
    to repeatedly take the biggest offer. This holds true for
    the case given but might not always
    offers MUST have the price of 1 as a tuple (unchecked)
    """

    ret = 0
    offers = sorted(offers, key = lambda x : x[0], reverse = True)

    for unit, offer_price in offers:
        if unit > count:
            continue

        modulo, remainder = divmod(count, unit)
        ret += modulo * offer_price
        count = remainder

    return ret

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    
    count_dict = {
        "A" : 0,
        "B" : 0,
        "C" : 0,
        "D" : 0,
        "E" : 0,
        "F" : 0,
    }

    for char in skus:
        if char not in count_dict.keys():
            return -1
        count_dict[char] += 1

    #always can combine offer this way as it is cheaper
    count_dict["B"] -= count_dict["E"] // 2

    ret = (
        offer(count_dict["A"], [
            (1, 50),
            (3, 130),
            (5, 200)
        ]) +
        offer(count_dict["B"], [
            (1, 30),
            (2, 45),
        ]) +
        offer(count_dict["C"], [
            (1, 20)
        ]) +
        offer(count_dict["D"], [
            (1, 15),
            (3, 130),
            (5, 200)
        ]) + 
        offer(count_dict["E"], [
            (1, 40)
        ]) +
        offer(count_dict["F"], [
            (1, 10),
            (3, 20)
        ])
    )

    return ret






