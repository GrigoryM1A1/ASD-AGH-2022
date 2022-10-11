"""
Floyd-Warshall - O(V^3)
"""


def floyd_warshall(G):
    V = len(G)
    inf = float('inf')
    D = [[G[i][j] for j in range(V)] for i in range(V)]

    for u in range(V):
        for v in range(V):
            if u != v and D[u][v] == 0:
                D[u][v] = inf

    for k in range(V):
        for u in range(V):
            for v in range(V):
                D[u][v] = min(D[u][v], D[u][k] + D[k][v])

    for row in D:
        print(row)


# Graph = [[0, 5, 0, 10],
#          [0, 0, 3, 0],
#          [0, 0, 0, 1],
#          [0, 0, 0, 0]]
# floyd_warshall(Graph)
Ta = [
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
]
floyd_warshall(Ta)
