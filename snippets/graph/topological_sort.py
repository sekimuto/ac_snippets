def topological_sort(n, edges):
    """
        トポロジカルソート

        DAGの並び替えをする

        Args:
            n: 頂点数
            edges: (始点, 終点)のリスト

        Returns:
            list[int] | None: 並び替えた頂点のリスト。DAGではない場合はNoneを返す
    """

    from collections import Counter, deque

    inbound_c = Counter()

    # 流入計算 & グラフ作成
    g = [[] for _ in range(n)]
    for start, goal in edges:
        inbound_c[goal] += 1
        g[start].append(goal)
    
    starts = [i for i in range(n) if inbound_c[i] == 0]

    # 例外
    if len(starts) == 0:
        return None

    q = deque(starts)
    ans = []

    while q:
        v = q.popleft()
        ans.append(v)
        for u in g[v]:
            inbound_c[u] -= 1
            if inbound_c[u] == 0:
                q.append(u)
    
    # 全ての頂点が入らなければDAGではない
    if len(ans) == n:
        return ans
    else:
        return None
