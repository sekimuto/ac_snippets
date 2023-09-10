def z_algorithm(s: str):
    """
        z-アルゴリズム

        文字列Sの先頭とS[i]からの部分文字列を比較したとき、何文字目まで一致するか

        計算量: `O(|S|)`
    """

    l = len(s)
    a = [0] * l
    a[0] = l
    i = 1
    j = 0

    while i < l:
        while i + j < l and s[j] == s[i+j]:
            j += 1
        
        a[i] = j

        if j == 0:
            i += 1
            continue

        k = 1
        while i + k < l and k + [k] < j:
            a[i+k] = a[k]
            k += 1


            i += k
            j -= k
    
    return a
