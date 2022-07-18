

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    
    for char in skus:
        if char not in ["A","B","C","D"]:
            return -1


