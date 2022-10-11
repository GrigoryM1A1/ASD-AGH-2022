'''
Znajdywanie cyklu eulera
Zal: Graf jest spojny
'''
from collections import deque


def even_degrees(G):
    V = len(G)

    for v in range(V):
        if len(G[v]) % 2 == 1:
            return False
    return True


def euler(G):
    # przychodzimy z u do v
    def DFSVisit(G, u, v):
        nonlocal visited_edges, res
        visited_edges[u][v] = True
        visited_edges[v][u] = True

        for i in G[v]:
            if not visited_edges[v][i]:
                DFSVisit(G, v, i)
        res.append(v)

    if not even_degrees(G):
        return None

    V = len(G)
    res = deque([])
    visited_edges = [[False for v in range(V)] for u in range(V)]

    for u in G[0]:
        if not visited_edges[0][u]:
            DFSVisit(G, 0, u)
    res.append(0)
    return res


Graph = [[1, 2],
         [0, 2, 3, 5],
         [0, 1, 3, 5],
         [1, 2, 4, 5],
         [5, 3],
         [2, 4, 1, 3]]
euler(Graph)
