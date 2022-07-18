# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int):

    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError(f"received non-integer argument")
    elif x not in range(0, 101) or y not in range(0, 101):
        raise ValueError(f"argument not in range 0-100")

    return x + y

