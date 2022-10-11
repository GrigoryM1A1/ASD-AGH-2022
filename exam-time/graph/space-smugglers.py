"""
Nathan Reynolds is a famous smuggler and captain of a spaceship "Serenade". He was offered a potentially dangerous job
on Ariel, one of the border planets of the star system. But to save all the "honest" earnings of
the previous adventures, he decided to store them on one of the planets on the way to the border.
Star system is represented by n planets and m space tunnels between them. Space tunnel is one-way wormhole
to travel from one planet to another, requiring an amount of gravitonium to perform the gravity jump.
There may be several space tunnels between two planets, but no space tunnel leads to the same planet it starts from.

Your task as a first officer is to find the minimum amount of gravitonium to travel from the base planet to Ariel,
visiting some other planet to store the earnings, and return back to base, picking up the earnings on the way back.
Note, that storing the earnings in a base planet or the planet, where the job is taking place, is not allowed.
But it's allowed to visit Ariel with the earnings as long as you are not doing a job on this planet.


Czyli tak naprawde trzeba znalezc co najmniej jeden wspolny wierzcholek na drogach s -> t oraz t -> s

s -> v + v -> t + t -> v + v -> s
"""
import heapq


def dijkstra(G, s):
    V = len(G)
    dist = [float('inf') for _ in range(V)]
    dist[s] = 0
    Parent = [None for v in range(V)]

    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q, (dist[s], s))
    while Q:
        w, u = heapq.heappop(Q)
        for v, cost in G[u]:
            new_dist = dist[u] + cost
            if new_dist < dist[v]:
                dist[v] = new_dist
                Parent[v] = u
                heapq.heappush(Q, (new_dist, v))
    return dist


def smugglers(n, m, s, t, solar_system):
    Graph = [[] for _ in range(n)]
    Reverse_Graph = [[] for _ in range(n)]

    for u, v, cost in solar_system:
        Graph[u].append((v, cost))
        Reverse_Graph[v].append((u, cost))

    dist_from_s_original = dijkstra(Graph, s)
    dist_from_t_original = dijkstra(Graph, t)
    dist_from_s_reversed = dijkstra(Reverse_Graph, s)
    dist_from_t_reversed = dijkstra(Reverse_Graph, t)

    min_cost = float('inf')
    for v in range(n):
        if v != s and v != t:
            new_min = dist_from_s_original[v] + dist_from_t_reversed[v] +\
                      dist_from_t_original[v] + dist_from_s_reversed[v]
            min_cost = min(min_cost, new_min)

    return min_cost


# (u, v, cost)
planets = [(0, 2, 1), (0, 4, 5), (1, 4, 1), (2, 0, 10), (2, 3, 5), (3, 1, 1), (4, 0, 5), (4, 2, 100), (4, 3, 5)]
print(smugglers(5, 9, 0, 1, planets))
