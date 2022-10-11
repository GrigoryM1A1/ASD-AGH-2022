"""
1. Wykonaj DFS, dla kazdego wierzcholka v zapamietujac czas odwiedzenia d[v]
2. Dla kazdego v obliczamy:
    low[v] = min(d[v], min(d[u]), min(low[w]))
    u - istnieje krawedz wsteczna z u do v
    w - dzieckow w drzewie dfs

    krawedz wsteczna = krawedz z naszego aktualnego wierzcholka do jeszcze nie przetworzonego wierzcholka

3. Mosty to krawedzie {v, parent[v]}, gdzie d[v] == low[v]
"""


def dfs_visit(G, u, visited, parent, low, d, time):
    V = len(G)
    visited[u] = True

    d[u] = time
    low[u] = time
    time += 1

    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            dfs_visit(G, v, visited, parent, low, d, time)
            low[u] = min(low[u], low[v])

            # if low[v] > d[u]:
            #     print(u, v)
        elif v != parent[u]:
            low[u] = min(low[u], d[v])


def find_bridges(G):
    V = len(G)
    visited = [False for _ in range(V)]
    d = [float('inf') for _ in range(V)]
    low = [float('inf') for _ in range(V)]
    parent = [None for _ in range(V)]
    Bridges = []

    time = 0
    for u in range(V):
        if not visited[u]:
            dfs_visit(G, u, visited, parent, low, d, time)

    print("d: ", d)
    print("low: ", low)
    for v in range(V):
        if d[v] == low[v]:
            Bridges.append((v, parent[v]))
    print(Bridges)


G1 = [[3, 1],
      [0, 2],
      [5, 1, 3],
      [2, 0, 4],
      [3],
      [7, 6, 2],
      [7, 5],
      [5, 6]]
find_bridges(G1)
