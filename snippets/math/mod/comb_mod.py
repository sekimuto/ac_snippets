def modinv(a, mod):
    return pow(a, mod-2, mod)

def comb_mod(n, r, mod):
    """
        modでのnCrを算出する
    """
    # 例外
    if r < 0 or n < r:
        return 0
    
    r = min(r, n-r)

    res = 1

    # nCrの分子の部分
    for i in range(n, n-r, -1):
        res *= i
        res %= mod
    
    # nCrの分母の部分（逆元をかけていく）
    for i in range(r, 0, -1):
        res *= modinv(i, mod)
        res %= mod
    
    return res

def factorial_mod(n, mod):
    """
        1からnまでの階乗のmodのリスト（[1!%mod, 2!%mod, 3!%mod, ..., n!%mod]）を返す
    """
    res = [0] * (n + 1)
    res[0] = 1
    for i in range(1, n+1):
        res[i] = (res[i-1] * i) % mod
    
    return res
