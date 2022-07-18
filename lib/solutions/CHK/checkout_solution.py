
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
        (4, 120),
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
def compute_price(count: int, offers: list):

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

def grouping(count_dict: dict, group: list, group_size: int):
    """
    reduces counts in count_dict and returns saving
    ASSUMES group must contain separate members, i.e. 3Z is not a valid offer
    also ASSUMES it is rational to take the offer
    """
    new_count_dict = count_dict.copy()

    counts = [
        (g, new_count_dict[g])
        for g in group
    ]
    counts = sorted(counts, key = lambda x : x[1], reverse=True)
    counts = [count for count in counts if count[1] > 0]

    #loop to remove groups 1 by 1
    group_num = 0
    while len(counts) > group_size:
        new_counts = [(c[0], c[1] - counts[0][1]) for c in counts]
        group_num += counts[0][1]
        new_counts = [count for count in new_counts if count[1] > 0]
        counts = new_counts
        print(counts)


    for g in group:
        #RHS determines how many groupings it is possible to make
        new_count_dict[g] -= group_num

    return new_count_dict, group_num
    




# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    
    count_dict = {
        key: 0 for key in OFFERS.keys()
    }

    for char in skus:
        if char not in count_dict.keys():
            return -1
        count_dict[char] += 1

    #combine custom offers
    count_dict["B"] -= count_dict["E"] // 2
    count_dict["B"] = max(count_dict["B"], 0)
    count_dict["M"] -= count_dict["N"] // 3
    count_dict["M"] = max(count_dict["M"], 0)
    count_dict["Q"] -= count_dict["R"] // 3
    count_dict["R"] = max(count_dict["R"], 0)

    ret = sum(
        [
            compute_price(count_dict[key], OFFERS[key])
            for key in OFFERS
        ]
    )

    return ret








