class LowLink:
    def __init__(self, g, n):
        """
            LowLink

            グラフ上の橋(取り除いたら非連結になる辺)を調べる

            計算量は`O(V+E)`
        """
        from sys import setrecursionlimit

        self.INF = 1 << 61
        self.g = g
        self.ord = [self.INF] * n   # preorder
        self.low = [self.INF] * n   # lowlink
        self.child_count = [0] * n
        self.dfs_tree = []  # DFS木のスタック
        self.k = 0
        self.root = 0

        self.aps = []   # 関節点
        self.bridges = []   # 橋

        setrecursionlimit(1000000)

        self._dfs(self.root, -1)
        self.aps.sort()
        self.bridges.sort(key=lambda x: (x[0], x[1]))

    def get_aps(self):
        return self.aps
    
    def get_bridges(self):
        return self.bridges

    def _dfs(self, v, past):
        self.ord[v] = self.k
        self.low[v] = self.k

        self.k += 1
        self.dfs_tree.append(v)
        is_ap = False

        for u in self.g[v]:
            if self.ord[u] == self.INF:
                self.child_count[v] += 1
                self._dfs(u, v)
                self.low[v] = min(self.low[v], self.low[u])

                # 橋の判定
                if self.ord[v] < self.low[u]:
                    self.bridges.append((min(v, u), max(u, v)))
                
                if v != self.root and self.ord[v] <= self.low[u]:
                    is_ap = True
            
            elif u != past:
                self.low[v] = min(self.low[v], self.ord[u])
        
        # 根の関節点の判定
        if v == self.root and self.child_count[self.root] > 1:
            is_ap = True
        
        if is_ap:
            self.aps.append(v)

