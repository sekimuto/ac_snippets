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

    def get_members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def get_roots(self):
        roots = list(set([self.find(i) for i in range(self.n)]))
        return roots
    
    def get_group_count(self):
        return len(self.get_roots())

    def get_all_members(self):
        from collections import defaultdict
        res = defaultdict(list)
        for i in range(self.n):
            root = self.find(i)
            res[root].append(i)
    
        return res

