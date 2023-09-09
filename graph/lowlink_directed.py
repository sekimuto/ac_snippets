class LowLink:
    def __init__(self, g, n):
        """
            有向グラフのLowLink

            グラフ上の橋(取り除いたら非連結になる辺)を調べる

            計算量は`O(V+E)`
        """
        self.g = g
        self.INF = 1 << 61
        self.ord = [-1] * n     # preorder
        self.low = [self.INF] * n   # lowlink
        self.child_count = [0] * n
        self.dfs_tree = []
        self.groups = []    # 強連結成分
        self.group_count = 0    # 強連結成分の数
        self.seen = []
        self.k = 0
        self.root = 0

        self.aps = []
        self.bridges = []

        self._dfs(self.root, -1)
        self.aps.sort()
        self.bridges.sort(key=lambda x: (x[0], x[1]))

    def _dfs(self, v, prev):
        self.k += 1
        self.ord[v] = self.k
        self.low[v] = self.k
        self.dfs_tree.append(v)

        for u in self.g[v]:
            if self.ord[u] == -1:
                self.child_count[v] += 1
                self._dfs(u, v)
                self.low[v] = min(self.low[v], self.low[u])
            else:
                self.low[v] = min(self.low[v], self.ord[u])
    
    def is_same_scc(self, u, v) -> bool:
        # TODO
        pass
