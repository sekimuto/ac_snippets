def digit10(n: int) -> int:
    """
        10進数表記における桁数を返す関数
    """
    from math import log10

    return int(log10(n)) + 1
