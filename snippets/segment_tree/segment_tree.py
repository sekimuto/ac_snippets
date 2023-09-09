class SegTree:
    """
        Segment Tree

        値の更新と区間範囲についてのクエリ（区間の和や区間最小）を実行可能
    """
    def __init__(self, init_val: list, opr, ide_ele: int):
        n = len(init_val)
        self.opr = opr
        self.ide_ele = ide_ele
        self.num = 1 << (n-1).bit_length()
        self.tree = [ide_ele] * (2 * self.num - 1)

        # 配列の値をセット
        for i in range(n):
            self.tree[self.num + i - 1] = init_val[i]
        
        # segtreeを構築
        for i in range(self.num-2, -1, -1):
            self.tree[i] = self.opr(self.tree[2*i+1], self.tree[2*i+2])
    
    def update(self, k, x):
        """
            k番目(0-index)の値をxに更新する
        """
        k += (self.num - 1)
        self.tree[k] = x
        while k > 0:
            k -= 1
            k >>= 1
            self.tree[k] = self.opr(self.tree[2*k+1], self.tree[2*k+2])
    
    def add(self, k, x):
        """
            k番目(0-index)の値にxを加算する
        """
        k += (self.num - 1)
        self.tree[k] += x

        while k > 0:
            k -= 1
            k >> 1
            self.tree[k] = self.opr(self.tree[2*k+1], self.tree[2*k+2])
    
    def multiply(self, k, x):
        """
            k番目(0-index)の値にxを乗算する
        """
        k += (self.num - 1)
        self.tree[k] *= x
        while k > 0:
            k -= 1
            k >>= 1
            self.tree[k] = self.opr(self.tree[2*k+1], self.tree[2*k+2])
    
    def query(self, l, r):
        """
            区間[l, r)のoprの結果を返す
        """
        res = self.ide_ele

        l += (self.num - 1)
        r += (self.num - 1)

        while l < r:
            if l & 1 == 0:
                res = self.opr(res, self.tree[l])
            if r & 1 == 0:
                res = self.opr(res, self.tree[r-1])
                r -= 1
            l >>= 1
            r >>= 1
        
        return res
