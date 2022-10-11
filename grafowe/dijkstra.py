# shift + F6 - mozna zmienic nazwe zmiennej w kazdym miejscu w danej funkcji #kozak
"""
Dijkstra - lista sasiedztwa - O(E*logV)
"""
import heapq
from collections import deque


def get_path(Parent, start, finish):
    Res = deque([])
    Res.appendleft(finish)

    curr = finish
    while curr is not None:
        if Parent[curr] is not None:
            Res.appendleft(Parent[curr])
        curr = Parent[curr]

    return list(Res)


def dijkstra(G, s):
    V = len(G)
    inf = float('inf')
    PQ = []
    heapq.heapify(PQ)

    Dist = [inf for v in range(V)]
    Dist[s] = 0
    Parent = [None for v in range(V)]

    heapq.heappush(PQ, (Dist[s], s))
    # for v in G[s]:
    #     heapq.heappush(PQ, (v[1], v[0]))

    while len(PQ) > 0:
        weight, u = heapq.heappop(PQ)
        for v in G[u]:
            if Dist[v[0]] > Dist[u] + v[1]:
                Dist[v[0]] = Dist[u] + v[1]
                Parent[v[0]] = u
                heapq.heappush(PQ, (Dist[v[0]], v[0]))

    # print(get_path(Parent, s, 8))
    print(Dist)


# (wierzcholek, waga)
graph1 = [[(1, 1), (7, 2)],  # 0
          [(0, 1), (2, 2), (4, 3)],  # 1
          [(1, 2), (3, 5)],  # 2
          [(2, 5), (6, 1)],  # 3
          [(1, 3), (5, 3), (7, 1)],  # 4
          [(4, 3), (8, 1), (6, 8)],  # 5
          [(3, 1), (5, 8), (8, 4)],  # 6
          [(0, 2), (4, 1), (8, 7)],  # 7
          [(7, 7), (5, 1), (6, 4)]]  # 8
#
# graph2 = [[(1, 2), (2, 4)],
#           [(3, 7), (2, 1)],
#           [(4, 3)],
#           [(5, 1)],
#           [(3, 2), (5, 5)],
#           []]
#
dijkstra(graph1, 0)
# dijkstra(graph2, 0)
# Gr = [[(1, 16), (2, 15), (3, 37)],
#       [(0, 16), (2, 8), (3, 22)],
#       [(0, 15), (1, 8), (3, 23)],
#       [(1, 22), (0, 37), (2, 23)]]
# dijkstra(Gr, 0)
