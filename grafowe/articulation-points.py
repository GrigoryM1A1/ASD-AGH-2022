"""
Znajdowanie punktow artykulacji - lista sasiedztwa
"""


def art_points(G):
    def dfs_visit(G, u):
        nonlocal visited, articulation_points, parent, low, disc, time

        children = 0
        visited[u] = True
        disc[u] = time
        low[u] = time
        time += 1
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                dfs_visit(G, v)

                low[u] = min(low[u], low[v])
                # u is root
                if parent[u] == -1 and children > 1:
                    articulation_points[u] = True

                if parent[u] != -1 and low[v] >= disc[u]:
                    articulation_points[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    V = len(G)
    inf = float('inf')
    visited = [False for _ in range(V)]
    disc = [inf for _ in range(V)]
    low = [inf for _ in range(V)]
    parent = [-1 for _ in range(V)]
    articulation_points = [False for _ in range(V)]
    time = 0

    for i in range(V):
        if not visited[i]:
            dfs_visit(G, i)
    return articulation_points


G1 = [[3, 1],
      [0, 2],
      [5, 1, 3],
      [2, 0, 4],
      [3],
      [7, 6, 2],
      [7, 5],
      [5, 6]]
print(art_points(G1))
