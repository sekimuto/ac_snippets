"""
    01BFS
"""

def bfs01(n, g, start):
    from collections import deque

    INF = 1 << 61
    
    q = deque([start])

    dist = [INF for _ in range(n)]
    dist[start] = 0

    while q:
        v = q.popleft()
        for u, c in g[v]:
            d = dist[v] + c
            if d < dist[u]:
                dist[u] = d
                if c == 1:
                    q.append(u)
                else:
                    q.appendleft(u)
    
    return dist
