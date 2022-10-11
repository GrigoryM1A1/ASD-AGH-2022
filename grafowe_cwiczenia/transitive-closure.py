"""
Floyd-Warshall ale na boolach
Zał: G[i][j] = True | False
"""


def transitive_closure(G):
    V = len(G)
    D = [[G[i][j] for j in range(V)] for i in range(V)]

    for k in range(V):
        for u in range(V):
            for v in range(V):
                D[u][v] = D[u][v] or (D[u][k] and D[k][v])
    return D
