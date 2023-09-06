def modpow(a: int, b: int, mod: int):
    """
        累乗のmod a^bをO(logb)で解く（二分累乗法）
    """
    l = b.bit_length()
    res = 1
    for i in range(l):
        if (b >> 1) & 1:
            res *= (a % mod)
            res %= mod
        a *= a
        a %= mod
