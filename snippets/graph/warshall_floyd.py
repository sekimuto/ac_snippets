def warshall_floyd(costs):
    """
        ワーシャルフロイド法

        各頂点間の移動コストの最小値をまとめて算出する

        Args:
            costs: 2次元配列。iからjに移動するのにかかるコスト
    """

    n = len(costs)
    # 到達不可能
    NOT_ACCESSIBLE = 1 << 61
    STOPPED = -1

    # 経路復元用配列
    # i -> jの最短経路を考えた時、jに到達する直前に訪れる必要がある点を保持
    prev = [[STOPPED] * n for _ in range(n)]

    # 経由点
    for k in range(n):
        # 始点
        for i in range(n):
            # 終点
            for j in range(n):
                if costs[i][k] != NOT_ACCESSIBLE and costs[k][j] != NOT_ACCESSIBLE:
                    if costs[i][k] + costs[k][j] < costs[i][j]:
                        costs[i][j] = costs[i][k] + costs[k][j]
                        prev[i][j] = prev[k][j]
        
    return costs, prev
    
# 最短経路復元
def get_path(prev, start: int, goal: int):
    n = len(prev)

    # 例外
    if start < 0 or start >= n or goal < 0 or goal >= n:
        return None
    
    path = []

    cur = goal
    while cur != start:
        path.append(cur)
        cur = prev[start][cur]

    path.append(start)

    path.reverse()

    return path

# 負の閉路を検出
def is_negative(costs):
    n = len(costs)
    for i in range(n):
        if costs[i][i] < 0:
            return True
    
    return False
