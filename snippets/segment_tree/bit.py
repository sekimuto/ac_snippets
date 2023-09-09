class BIT:
    """
        BIT(Binary Indexed Tree)

        以下が可能なデータ構造

            - `ai`に`x`を加算(`O(logN)`)
            - `ai`から`ai`までの和を求める(`O(logN)`)

        セグメント木の機能を限定して、高速に動くようにしたもの
    """

    def __init__(self, n):
        self.n = n
        # 内部的には1-indexedで保存しておく
        self.data = [0] * (self.n + 1)
    
    def set_init_val(self, init_val: list):
        """
            初期値をセットする(計算量`O(NlogN)`)
        """
        if len(init_val) != self.n:
            return False
        
        for i in range(self.n):
            self.add(i, init_val[i])
    
    def add(self, i, x):
        """
            i番目にxを加算する

            Args:
                i: index(0-indexed)
                x: 加算する値
        """
        i += 1

        while i <= self.n:
            self.data[i] += x
            i += i & -i
    
    def sum(self, l, r):
        """
            区間[l, r]の区間和を取得

            Args:
                l: 区間の左端(0-indexed)
                r: 区間の右端(1-indexed)
        """
        return self._sum(r) - self._sum(l-1)
    
    def _sum(self, i):
        """
            [0, i]の区間和を取得

            Args:
                i: 区間の右端(0-indexed)
        """
        # 1-indexedにする
        i += 1
        if i > self.n:
            return False
        
        s = 0
        while i:
            s += self.data[i]
            i -= i & -i

        return s
    
    def lower_bound(sself, x):
        """
            累積和がx以上になる最小のindex(0-indexed)と、その直前までの累積和を返す
        """
        # TODO
        pass
