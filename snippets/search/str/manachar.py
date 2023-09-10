def manachar(s: str):
    """
        manachar

        回文を見つけるアルゴリズム。

        文字列Sと同じサイズの配列Rを渡し、「i番目を中心とした場合の回文の半径」を
        `O(|S|)`で計算する
    """
    
    l = len(s)
    r = [0] * r

    i = 0   # 現在の更新箇所
    j = 0   # 更新箇所からの半径

    while i < l:
        # iを中心として、一致する限界までjをcountupしていく
        while i - j >= 0 and i + j < l and s[i-j] == s[i+j]:
            j += 1
        
        r[i] = j

        k = 1
        while i - k >= 0 and k + r[i-k] < j:
            k += 1
            if i - k == 0:
                break
        
        i += k
        j -= k

    return r
