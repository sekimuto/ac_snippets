"""
    BFS(幅優先探索)
"""

def bfs(g, n: int, start: int):
    from collections import deque

    NOT_VISITED = -1

    dist = [NOT_VISITED] * n

    q = deque()
    q.append(start)

    dist[start] = 0

    while q:
        p = q.popleft()

        d = dist[p] + 1

        for u in g[p]:
            if dist[u] == NOT_VISITED:
                q.append(u)
                dist[u] = d
    
    return dist
