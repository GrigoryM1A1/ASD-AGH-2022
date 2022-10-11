"""
Dany jest graf nieskierowany G = (V, E) oraz wierzcholki s, t.
Zaimplementowac funkcje paths(G, s, t) zwracajaca liczbe krawedzi e, takich ze e wystepuje
w jednej z najkrotszych sciezek z s do t.

Graf dany jest lista sasiedztwa (vertex, weight)

Algorytm:
1) Puszczamy dijkstre w celu znalezeinia wszystkich mozliwych najkrotszych sciezek z s do t - parent jest listą
list, w ktorej przetrzymywani są wszystkie wierzcholki z ktorych przychodzimy do aktualnego wierzcholka

2) Po wykonaniu dijkstry, Parent jest pewnym grafem skierowanym
"""
from zad3testy import runtests
import heapq


def dfs(G, s, t):
    def dfs_visit(Graph, u):
        nonlocal edges, visited
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                edges += 1
                dfs_visit(Graph, v)
            else:
                edges += 1

    V = len(G)
    visited = [False for _ in range(V)]
    edges = 0

    for ver in G[s]:
        if not visited[ver]:
            edges += 1
            dfs_visit(G, ver)
    if not visited[t]:
        return 0

    return edges


def dijkstra(G, s):
    V = len(G)
    Dist = [float('inf') for _ in range(V)]
    Dist[s] = 0

    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q, (Dist[s], s))
    while Q:
        weight, u = heapq.heappop(Q)
        for v, w in G[u]:
            new_dist = Dist[u] + w
            if new_dist < Dist[v]:
                Dist[v] = new_dist
                heapq.heappush(Q, (new_dist, v))

    return Dist


def paths(G, s, t):
    V = len(G)
    Dist = dijkstra(G, s)
    # if Dist[t] == float('inf'):
    #     return 0

    Shortest_paths = [[] for i in range(V)]
    for u in range(V):
        for v, w in G[u]:
            if Dist[u] + w == Dist[v]:
                Shortest_paths[v].append(u)

    edges = dfs(Shortest_paths, t, s)
    return edges


Graph1 = [[(1, 2), (2, 4)],
         [(0, 2), (3, 11), (4, 3)],
         [(0, 4), (3, 13)],
         [(1, 11), (2, 13), (5, 17), (6, 1), (7, 4)],
         [(1, 3), (5, 5)],
         [(3, 17), (4, 5), (7, 7)],
         [(3, 1), (7, 3)],
         [(5, 7), (6, 3), (3, 4)]]
#print(paths(Graph1, s=0, t=7))
#
# # na ten moment ten graf rozwala ten algorytm
# Graph2 = [[(1, 1), (2, 1)],
#           [(4, 1), (0, 1)],
#           [(4, 1), (0, 1)],
#           [(6, 1), (4, 1)],
#           [(3, 1), (5, 1), (1, 1), (2, 1)],
#           [(4, 1), (6, 1)],
#           [(8, 1), (7, 1), (3, 1), (5, 1)],
#           [(6, 1), (9, 1)],
#           [(9, 1), (6, 1)],
#           [(7, 1), (8, 1)]]
# print(paths(Graph2, s=0, t=9))
runtests( paths )

# test5 = [[(5, 8), (6, 1), (20, 1), (21, 9), (24, 8)],
#          [(2, 2), (5, 4), (14, 1), (25, 5)],
#          [(1, 2), (11, 1), (18, 4), (21, 3), (26, 9)],
#          [(6, 4), (7, 1), (8, 6), (9, 6), (12, 8), (14, 6), (17, 8), (18, 6), (19, 2), (23, 3), (24, 5)],
#          [(6, 4), (10, 4), (25, 4), (25, 7), (29, 5)],
#          [(0, 8), (1, 4), (7, 6), (14, 7), (18, 7), (22, 8), (26, 3), (27, 1), (28, 1)],
#          [(0, 1), (3, 4), (4, 4), (16, 7), (19, 6)],
#          [(3, 1), (5, 6), (10, 7), (20, 2), (29, 8)],
#          [(3, 6), (27, 3)],
#          [(3, 6), (14, 1), (15, 7), (16, 8), (20, 1), (21, 9), (22, 5), (23, 4), (26, 4), (28, 7)],
#          [(4, 4), (7, 7), (13, 4), (16, 7), (19, 6)],
#          [(2, 1), (13, 9), (19, 5), (21, 1), (28, 8)],
#          [(3, 8), (14, 6), (16, 8)],
#          [(10, 4), (11, 9), (15, 5), (18, 2), (29, 2)],
#          [(1, 1), (3, 6), (5, 7), (9, 1), (12, 6), (17, 6), (22, 1)],
#          [(9, 7), (13, 5), (23, 4), (27, 1)],
#          [(6, 7), (9, 8), (10, 7), (12, 8), (18, 6), (27, 9)],
#          [(3, 8), (14, 6), (23, 2)],
#          [(2, 4), (3, 6), (5, 7), (13, 2), (16, 6), (23, 5), (24, 6)],
#          [(3, 2), (6, 6), (10, 6), (11, 5), (27, 8)],
#          [(0, 1), (7, 2), (9, 1), (21, 6), (23, 4), (25, 3), (28, 4), (29, 8)],
#          [(0, 9), (2, 3), (9, 9), (11, 1), (20, 6), (24, 8), (27, 7), (28, 1)],
#          [(5, 8), (9, 5), (14, 1), (24, 1), (27, 8)],
#          [(3, 3), (9, 4), (15, 4), (17, 2), (18, 5), (20, 4), (24, 8)],
#          [(0, 8), (3, 5), (18, 6), (21, 8), (22, 1), (23, 8), (28, 3), (29, 9)],
#          [(1, 5), (4, 4), (20, 3), (26, 4)],
#          [(2, 9), (5, 3), (9, 4), (25, 4)],
#          [(5, 1), (8, 3), (15, 1), (16, 9), (19, 8), (21, 7), (22, 8), (29, 3)],
#          [(5, 1), (9, 7), (11, 8), (20, 4), (21, 1), (24, 3)],
#          [(4, 5), (7, 8), (13, 2), (20, 8), (24, 9), (27, 3)]]
# print(paths(test5, s=0, t=18))
