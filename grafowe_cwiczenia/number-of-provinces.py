"""
Znalezc wszystkie spojne skladowe grafu
"""


def num_provinces(G):
    def dfs_visit(Adj, u):
        nonlocal visited
        visited[u] = True

        for v in Adj[u]:
            if not visited[v]:
                dfs_visit(Adj, v)

    V = len(G)
    visited = [False for _ in range(V)]
    provinces = 0
    for vertex in range(V):
        if not visited[vertex]:
            dfs_visit(G, vertex)
            provinces += 1

    return provinces


Graph = [[1, 2],
         [0, 2],
         [1, 0],
         [4],
         [5, 3],
         [4, 6],
         [5],
         [8],
         [7]]

Graph2 = [[1],
          [0]]
print(num_provinces(Graph2))
