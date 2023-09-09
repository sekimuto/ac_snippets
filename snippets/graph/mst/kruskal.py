"""
    クラスカル法のテンプレート
    （最小全域木を求めるアルゴリズム）

    コスト昇順で辺を走査していき、すでにつながれていない頂点ならその辺を選択する
"""

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        
        size_x = self.size[x]
        size_y = self.size[y]

        if size_x > size_y:
            x, y = y, x
        
        size_union = size_x + size_y

        self.size[x] = size_union
        self.size[y] = size_union

        self.parents[y] = x
    
    def get_size(self, x):
        return self.size[x]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
def main():
    n = 1000
    cost = 0
    uf = UnionFind(n)

    # (cost, u, v)
    edges = [[100, 1, 2], [50, 1, 3]]
    edges.sort()

    for c, u, v in edges:
        if not uf.is_same(u, v):
            cost += c
            uf.union(u, v)
    
    print(cost)
