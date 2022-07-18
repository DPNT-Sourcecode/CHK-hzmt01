
def offer(sku: str, char: str, price: int, offers=None):

    """
    computes optimal price in case of repeated offers
    NOTE: assumes for now that the optimal strategy is
    to repeatedly take the biggest offer. This holds true for
    the case given but might not always
    """

    count = 0
    for product in sku:
        if product == char:
            count += 1

    if not offers:
        return count * price

    ret = 0
    offers = sorted(offers, key = lambda x : x[0], reverse = True)

    #eliminate irrelevant offers
    offers = [o for o in offers where o[0] > count]

    for unit, offer_price in offers:
        modulo, remainder = divmod(count, unit)
        ret += modulo * offer_price
        count = remainder
        print(count)

    ret += remainder * offer_price
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
        "D" : 0
    }

    for char in skus:
        if char not in count.keys():
            return -1
        count[char] += 1

    #value counts
    ret = 15 * count["D"] + 20 * count["C"]

    modulo, remainder = divmod(count["A"], 3)
    ret += 130 * modulo + 50 * remainder

    modulo, remainder = divmod(count["B"], 2)
    ret += 45 * modulo + 30 * remainder

    return ret






