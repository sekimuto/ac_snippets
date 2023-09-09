class ZobristHash:
    """
        Zobrist Hash

        集合に登場する全要素にランダムな値を割り当てたあと、
        集合のハッシュ = 集合内の要素のXORとするこkとで、集合をハッシュ化できる
    """
    
    def __init__(self, all_factors: list):
        from random import randrange
        self.factor_rand_table = {}
        for factor in all_factors:
            self.factor_rand_table[factor] = randrange(1 << 61)
    
    def get_hash(self, set):
        # TODO
        pass


# TODO
# multisetに対応したZobrist Hash
class ZobristHashMultiSet:
    def __init__(self, all_factors: list):
        pass
