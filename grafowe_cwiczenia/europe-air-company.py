"""
The air company Europa serves various European cities.
The table below gives against the flight times between these cities.
1) How to determine the fastest route between two cities?
2) How to modify the previous method to take into account the duration of stopovers in different cities?
"""
# 1 - stworzyc graf i puscic dijkstre
# 2 - albo powielamy wierzcholki i dajemy krawedz z waga stopovera
#   - albo uwzgledniamy wage wierzcholka
# Zalozenie: Dostajemy tablice z dlugoscia przesiadki na starcie
import heapq


def dijkstra(G, Stopovers, s):
    V = len(G)
    inf = float('inf')
    Pq = []
    heapq.heapify(Pq)

    Dist = [inf for _ in range(V)]
    Dist[s] = 0
    heapq.heappush(Pq, (Dist[s], s))
    while Pq:
        weight, u = heapq.heappop(Pq)
        for v in range(V):
            if G[u][v] > 0:
                new_dist = Dist[u] + G[u][v] + Stopovers[u]
                if new_dist < Dist[v]:
                    Dist[v] = new_dist
                    heapq.heappush(Pq, (Dist[v], v))
    print(Dist)


Map = [[0, 90, 120, 0, 135],
       [100, 0, 0, 0, 180],
       [140, 0, 0, 175, 0],
       [0, 0, 200, 0, 65],
       [145, 190, 70, 0, 0]]
Breaks = [0, 10, 20, 30, 10]
dijkstra(Map, Breaks, 0)
