"""
    木のいろいろを統合したクラス
"""

class Tree:
    def __init__(self, n):
        self.tree = [[] for _ in range(n)]
        self.n = n

    def add_edge(self, u: int, v: int):
        self.tree[u].append(v)
        self.tree[v].append(u)
    
    def get_kth_parent(self, u):
        # TODO
        pass

    def get_lca(self, u: int, v: int):
        """2頂点の最近共通祖先を求める"""
        # TODO
        pass

    def get_depth(self, v, root):
        pass
