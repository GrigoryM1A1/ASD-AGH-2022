"""
Link to problem
https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/allsomenone-78013449/
"""


import heapq


def all_paths(vertex, Parent, All_tab):
    if len(Parent[vertex]) == 0:
        return

    for v in Parent[vertex]:
        All_tab[v] = 'all'
        all_paths(v, Parent, All_tab)


def ver_and_edges(n, m, Edges):
    Graph = [[] for _ in range(n)]
    Is_in_sh_path = ['none' for _ in range(n)]
    Is_in_sh_path[0] = Is_in_sh_path[n-1] = 'all'
    for u, v, w in Edges:
        Graph[u].append((v, w))
        Graph[v].append((u, w))
    Parent = [[] for _ in range(n)]
    Dist = [float('inf') for _ in range(n)]
    Dist[0] = 0

    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q, (Dist[0], 0))
    while Q:
        weight, u = heapq.heappop(Q)
        for v, w in Graph[u]:
            new_dist = Dist[u] + w
            if new_dist <= Dist[v]:
                Dist[v] = new_dist
                Parent[v].append(u)
                heapq.heappush(Q, (Dist[v], v))

    all_paths(n-1, Parent, Is_in_sh_path)
    for x in Is_in_sh_path:
        print(x)


G = [(0, 4, 5), (0, 3, 20), (1, 4, 5), (1, 3, 8), (1, 2, 7),
     (3, 4, 7), (5, 4, 18), (5, 2, 10)]
ver_and_edges(6, len(G), G)

# G = [(0, 1, 2), (0, 3, 3), (0, 7, 6), (0, 4, 1), (1, 2, 2), (7, 2, 2),
#      (7, 6, 4), (7, 3, 3), (5, 6, 1), (4, 5, 1)]
# ver_and_edges(8, len(G), G)
