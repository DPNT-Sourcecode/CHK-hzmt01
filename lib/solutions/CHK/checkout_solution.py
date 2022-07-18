
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
    
    count = {
        "A" : 0,
        "B" : 0,
        "C" : 0,
        "D" : 0,
        "E" : 0
    }

    for char in skus:
        if char not in count.keys():
            return -1
        count[char] += 1

    

    ret = offer(
        skus, "A", 
        [
            (1, 50),
            (3, 130),
            (5, 200)
        ])

    return ret










