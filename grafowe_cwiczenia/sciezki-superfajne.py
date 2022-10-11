"""
Dany jest graf wazony G. Sciezka superfajna to taka, ktora jest nie tylko najkrotsza wagowa
sciezka miedzy v i u. ale takze ma najmniejsza liczbe krawedzi (szukamy najkrotszych sciezek
w sensie liczby krawedzi wsrod wszystkich sciezek w sensie wagowym).
Podaj algorytm, ktory dla danego wierzcholka startowego s znajdzie superfajne sciezki
do pozostalych wierzcholkow.


Mozemy zmodyfikowac to jak dijkstra rozumie najtansza sciezke:
    Kazdy wierzcholek poza kosztem dotarcia do niego przechowuje liczbe krawedzi
"""
import heapq
from collections import deque


def bfs(G, s, t):
    V = len(G)
    Dist = [-1 for _ in range(V)]
    Parent = [-1 for _ in range(V)]
    Visited = [False for _ in range(V)]
    Dist[t] = 0
    Visited[t] = True

    Q = deque([])
    Q.append(t)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not Visited[v]:
                Visited[v] = True
                Dist[v] = Dist[u] + 1
                Parent[v] = u
                Q.append(v)

    return Dist[s], Parent


# it works... probably
def super_good_paths(G, s, t):
    V = len(G)
    inf = float('inf')
    Dist = [inf for _ in range(V)]
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

    All_shortest_paths_directed_graph = [[] for _ in range(V)]
    for u in range(V):
        for v, w in G[u]:
            if Dist[u] + w == Dist[v]:
                All_shortest_paths_directed_graph[v].append(u)

    min_edges, Path = bfs(All_shortest_paths_directed_graph, s, t)

    curr = t
    res = []
    while curr != -1:
        res.append(curr)
        curr = Path[curr]
    res.append(s)
    res.reverse()
    return min_edges, res


# (vertex, weight)
Graph = [[(1, 2), (3, 3), (4, 1), (7, 6)],
         [(2, 2), (0, 2)],
         [(1, 2), (7, 2)],
         [(7, 3), (0, 3)],
         [(5, 1), (0, 1)],
         [(4, 1), (6, 1)],
         [(5, 1), (7, 3)],
         [(2, 2), (3, 3), (6, 3), (0, 6)]]
print(super_good_paths(Graph, 0, 7))
