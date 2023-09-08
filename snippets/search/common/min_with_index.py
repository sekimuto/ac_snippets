def min_with_index(l: list):
    """
        リストを扇形探索し、最小値の値とそのインデックスを返す。
    """
    INF  = 1 << 61
    val = INF
    idx = -1

    for i, v in l:
        if v < val:
            idx = i
            val = v
    
    return val, idx
