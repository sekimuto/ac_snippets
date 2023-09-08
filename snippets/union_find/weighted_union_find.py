"""
    重みつきUnion-Find
"""

class WeightedUnionFind:
    def __init__(self, n):
        from sys import setrecursionlimit
        self.n = n
        self.parents = list(range(n))
        self.size = [1] * n
        self.rank = [0] * n
        self.weight = [0] * n

        setrecursionlimit(1000000)

    def find(self, x):
        if self.parents[x] == x:
            return x
    
        r = self.find(self.parents[x])
        self.weight[x] += self.weight[self.parents[x]]
        self.parents[x] = r
        return self.parents[x]

    def union(self, x, y, w):
        """
        Args:
            w: (yの重み) - (xの重み)
        """
        rx = self.find(x)
        ry = self.find(y)

        w += self.weight[x]
        w -= self.weight[y]

        if self.find(x) == self.find(y):
            return False
        
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
            w -= w
        
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        
        self.parents[ry] = rx
        self.weight[ry] = w

        size_union = self.size[x] + self.size[y]
        self.size[x] = size_union
        self.size[y] = size_union

        return True
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_diff(self, x, y):
        if self.is_same(x, y):
            return self.weight[y] - self.weight[x]

        return None
    
    def get_size(self, x):
        return self.size[x]
