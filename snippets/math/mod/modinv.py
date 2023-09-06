def modinv(a, mod):
    """
        aの逆元を求める

        Args:
            a: 逆元を求めたい数
            mod: 法
    """
    return pow(a, mod-2, mod)
