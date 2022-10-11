'''
BFS - lista sasiedztwa - O(V+E)
'''
from collections import deque


def bfs(G, s):
    Q = deque([])
    V = len(G)
    visited = [False for _ in range(V)]
    dist = [-1 for _ in range(V)]
    parent = [None for _ in range(V)]

    dist[s] = 0
    visited[s] = True
    Q.append(s)

    while not len(Q) == 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                parent[v] = u
                Q.append(v)
    print(dist)


Graph = [[3],
         [2, 3],
         [1, 3],
         [0, 1, 2, 4],
         [3, 5],
         [4, 6, 7],
         [5],
         [5]]
bfs(Graph, 0)

