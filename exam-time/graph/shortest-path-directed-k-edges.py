"""
Given a directed and two vertices ‘u’ and ‘v’ in it, find shortest path from ‘u’ to ‘v’
with exactly k edges on the path.
Matrix representation

Zał: k >= 2
"""


def shortest_path_exactly_k_edges(G, start, end, k):
    V = len(G)
    inf = float('inf')
    dp = [[[inf for _ in range(k + 1)] for _ in range(V)] for _ in range(V)]

    for e in range(k + 1):
        for i in range(V):
            for j in range(V):
                if e == 0 and i == j:
                    dp[i][j][e] = 0

                elif e == 1 and G[i][j] != 0:
                    dp[i][j][e] = G[i][j]

                elif e > 1:
                    for a in range(V):
                        if G[i][a] != 0 and i != a and j != a and dp[a][j][e - 1] != inf:
                            dp[i][j][e] = min(dp[i][j][e], G[i][a] + dp[a][j][e-1])

    # for row in dp:
    #     print(row)
    return dp[start][end][k]


graph = [[0, 10, 3, 2],
         [0, 0, 0, 7],
         [0, 0, 0, 6],
         [0, 0, 0, 0]]
print(shortest_path_exactly_k_edges(graph, 0, 3, 2))


graph = [[0, 1, 2, 0, 0, 0],
         [0, 0, 0, 6, 0, 0],
         [0, 2, 0, 4, 3, 0],
         [0, 0, 0, 0, 0, 3],
         [0, 0, 0, 1, 0, 5],
         [0, 0, 0, 0, 0, 0]]
print(shortest_path_exactly_k_edges(graph, 0, 3, 3))
