class RollingHash:
    """
        ローリングハッシュ

        数列や文字列のハッシュ化をする
    """

    def __init__(self, target: str):
        from random import randrange
        self.MOD = 1 << 61 - 1
        self.n = len(target)
        self.base = randrange(2, self.MOD-2)
        self.hash = []

        for i in range(self.n):
            # TODO
            pass

    def _calcmod(self, a, b):
        au = a >> 31
        ad = a & self.MOD
        bu = b >> 31
        bd = b & self.MOD
    
    def get_hash(self, l, r):
        return (self.hash[0:r] - self.hash[0:l-1]) % self.MOD
