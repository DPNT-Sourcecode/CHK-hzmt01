

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




