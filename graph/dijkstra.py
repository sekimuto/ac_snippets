def dijkstra(g, n: int, start: int):
    """
        ダイクストラ法

        正のコストの場合の探索コストの最小値を求める

        計算量は`O(ElogV)`

        Args:
            g: (cost, v)の形で保持されたリスト
            n: 頂点数
            start: 開始頂点
    """
    
    from heapq import heapify, heappop, heappush

    NOT_VISITED = -1

    hq = [(0, start)]
    heapify(hq)
    cost = [NOT_VISITED] * n
    cost[start] = 0

    while hq:
        c, v = heappop(hq)
        if c != NOT_VISITED and c > cost[v]:
            continue

        for d, u in g[v]:
            tmp_cost = d + cost[v]
            if cost[u] == NOT_VISITED or tmp_cost < cost[u]:
                cost[u] = tmp_cost
                heappush(hq, (tmp_cost, u))
    
    return cost
