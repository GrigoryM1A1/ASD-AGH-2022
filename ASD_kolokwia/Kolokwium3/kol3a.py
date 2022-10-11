"""
Grzegorz Piśkorski

Algorytm:
1) Na podstawie listy E - połączeń między planetami tworzymy sobie graf (lista sąsiedztwa)
2) Na podstawie listy S dodajemy wszystkie możliwe krawędzie między każdą parą planet z listy S do naszego
    grafu z punktu 1) z wagą 0
3) Wykonujemy algorytm Dijkstry na naszym stworzonym grafie i zwracamy długość najkrótszej trasy między planetami a i b

Złożoność obliczeniowa:
e == liczba wszystkich krawędzi między każdą parą wierzchołków z listy S
m == liczba krawędzi z listy E
n == liczba planet
O( m + e + (m+e)log(n) ) ===> O( (m+e)log(n) )
"""


from kol3atesty import runtests
import heapq


def spacetravel( n, E, S, a, b ):
    # tworze graf z w/w algorytmu
    Planets = [[] for _ in range(n)]

    # O( len(E) )
    for u, v, cost in E:
        Planets[u].append((v, cost))
        Planets[v].append((u, cost))

    # dodaje krawedzie miedzy planetami z S
    # O( len(S) * len(S) )
    for u in range(len(S)):
        for v in range(u + 1, len(S)):
            Planets[S[u]].append((S[v], 0))
            Planets[S[v]].append((S[u], 0))

    # Dijkstra
    # O( Elog(V) ) == dla tego grafu w najgorszym przypoadku chyba O( V^2 * log(V) )
    inf = float('inf')
    Dist = [inf for _ in range(n)]
    Dist[a] = 0
    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q, (Dist[a], a))
    while Q:
        weight, u = heapq.heappop(Q)
        for v, t in Planets[u]:
            new_dist = Dist[u] + t
            if new_dist < Dist[v]:
                Dist[v] = new_dist
                heapq.heappush(Q, (new_dist, v))

    if Dist[b] != inf:
        return Dist[b]

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
