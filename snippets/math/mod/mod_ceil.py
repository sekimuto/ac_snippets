def mod_ceil(n, m):
    """
        mの倍数のうち、ある数n以上で最小の数xを返す
    """
    from math import ceil
    return ceil(n / m) * m
