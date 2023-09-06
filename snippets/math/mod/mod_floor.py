def mod_floor(n, m):
    """
        mの倍数のうち、n以下で最大の数xを返す
    """
    from math import floor
    return floor(n / m) * m
