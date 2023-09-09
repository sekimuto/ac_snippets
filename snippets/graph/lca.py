class LCA:
    def __init__(self, g, root):
        """
            LCA(最近共通祖先)を求める
        """
        from sys import setrecursionlimit
        setrecursionlimit(1000000)

        self.g = g
        self.root = root

        # n ≥ 2
        self.n = len(g)
        # 木の高さ以上の最初の2^k(n ≤ 1用に念の為1以上を保証しておく)
        self.k = max((self.n-1).bit_length(), 1)
        self.parent = [[-1] * self.n for _ in range(self.k)]
        self.dist = [0] * self.n

        # ダブリングする
        self._dfs(root, -1, 0)
        for i in range(self.k-1):
            for j in range(self.n):
                if self.parent[i][j] < 0:
                    self.parent[i+1][j] = -1
                else:
                    self.parent[i+1][j] = self.parent[i][self.parent[i][j]]
    
    def _dfs(self, v, past, dist):
        self.parent[0][v] = past
        self.dist[v] = dist

        for u in self.g[v]:
            if u != past:
                self._dfs(u, v, dist+1)
    
    def search(self, v, u):
        """
            頂点v, uのLCAを求める
        """

        # 深いほうをuにする
        if self.dist[v] > self.dist[u]:
            u, v = v, u
        
        # LCAまでの距離を同じにする
        for i in range(self.k):
            if (self.dist[u] - self.dist[v] >> i) & 1:
                u = self.parent[i][u]
        
        # 二分探索でLCAを求める
        if u == v:
            return u
        
        for i in range(self.k-1, -1, -1):
            if self.parent[i][u] != self.parent[i][v]:
                u = self.parent[i][u]
                v = self.parent[i][v]
        
        return self.parent[0][u]
