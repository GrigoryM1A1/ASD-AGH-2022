"""
Check if graph is bipartite
"""
from collections import deque


def is_bipartite(G):
    V = len(G)
    color = [0 for _ in range(V)]
    Q = deque([])
    Q.append(0)
    color[0] = 1

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if color[v] == 0:
                color[v] = -color[u]
                Q.append(v)
            else:
                if color[v] == color[u]:
                    return False
    return True


G1 = [[1],
      [0, 2],
      [1]]
print(is_bipartite(G1))

G2 = [[3, 2],
      [3],
      [0, 3],
      [1, 2, 0]]
print(is_bipartite(G2))
