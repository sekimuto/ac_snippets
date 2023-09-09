def bellman_ford(edges, n: int, start: int):
    """
        ベルマンフォード法

        負の重みを持つグラフの最短距離コストを求める。

        計算量は`O(EV)`

        Args:
            edges: (start, end, cost)の順で保持されたリスト
            n: 頂点数
            start: 開始点
    """

    # 頂点未探索判定
    NOT_VISITED = 1 << 61

    # 負の閉路判定
    IN_NEGATIVE_CYCLE = -1 << 61

    costs = [NOT_VISITED for _ in range(n)]
    costs[start] = 0

    # 更新継続フラグ
    f = True

    for i in range(n):
        f = False

        for s, g, c in edges:
            if costs[s] + c < costs[g]:
                costs[g] = costs[s] + c
                f = True

                if i == n-1:
                    costs[g] = IN_NEGATIVE_CYCLE
        
        if not f:
            break

    else:
        while f:
            f = False
            for s, g, c in edges:
                if costs[g] != IN_NEGATIVE_CYCLE and costs[s] == IN_NEGATIVE_CYCLE:
                    costs[g] == IN_NEGATIVE_CYCLE
                    f = True
    
    return costs
