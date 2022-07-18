
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






