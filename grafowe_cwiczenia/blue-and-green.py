"""
Dany jest wazony graf nieskierowany reprezentowany przez macierz T o rozmiarach n x n.
T[i][j] == T[j][i], krawedz istnieje jesli T[i][j] > 0 i ma wage T[i][j].
Dana jest tez liczba rzeczywista d. Kazdy wierzcholek G ma jeden z kolorow:
zielony lub niebieski. Zaproponuj algorytm, ktory wyznacza najwieksza
liczbe naturalna l, taka ze istnieje l par wierzcholkow (p, q) nal. do V x V
spelniajacych warunki:

1) q - zielony, p - niebieski
2) odleglosc miedzy p i q (liczona jako suma wag najkrotszej sciezki) jest nie mniejsza niz d
3) kazdy wierzcholek wystepuje w co najwyzej jednej parze

Niech K[i] = 'blue' / 'green'
Pomysl:
1) Puszczamy Floyd-Warshalla, zeby znalezc wszystkie pary wierzcholkow, ktore
mozemy brac pod uwage (Dist[u][v] >= D)

2) Sprawdzamy czy kazda para ma rozne kolory

3) Tworzymy nowy graf skladajacy sie z krawedzi i wierzcholkow par (p, q) - dwudzielny

4) Zeby znalezc l wystarczy znalezc maksymalne skojarzenie tego grafu
"""
from collections import deque


def augmenting_path(G, s, t, parent):
    V = len(G)
    visited = [False for _ in range(V)]
    visited[s] = True
    Q = deque([])
    Q.append(s)

    while not len(Q) == 0:
        u = Q.popleft()
        for v in range(V):
            if not visited[v] and G[u][v] > 0:
                if v == t:
                    parent[v] = u
                    visited[v] = True
                    return
                visited[v] = True
                parent[v] = u
                Q.append(v)
    parent[t] = None
    return


def max_flow(G, s, t):
    V = len(G)
    inf = float('inf')
    flow = 0
    F = [G[i][:] for i in range(V)]
    parent = [None for _ in range(V)]

    augmenting_path(F, s, t, parent)
    while parent[t] is not None:
        u = t
        bottle_neck = inf
        while u != s:
            bottle_neck = min(bottle_neck, F[parent[u]][u])
            u = parent[u]

        flow += bottle_neck

        v = t
        while v != s:
            x = parent[v]
            F[x][v] -= bottle_neck
            F[v][x] += bottle_neck
            v = parent[v]

        augmenting_path(F, s, t, parent)
    return flow


def floyd_warshall(G):
    V = len(G)
    inf = float('inf')
    D = [G[i][:] for i in range(V)]

    for u in range(V):
        for v in range(u, V):
            if u != v and D[u][v] == 0:
                D[u][v] = D[v][u] =  inf

    for k in range(V):
        for u in range(V):
            for v in range(V):
                D[u][v] = min(D[u][v], D[u][k] + D[k][v])
    return D


def blue_and_green(T, K, D):
    # T - nasz graf
    # K - lista przedstawiajaca kolory wierzcholkow
    # D - odleglosc z warunku 2
    V = len(T)
    Dists = floyd_warshall(T)

    pq_pairs = []
    for p in range(V):
        for q in range(p, V):
            if p != q and float('inf') > Dists[p][q] >= D:
                if K[p] == 'blue' and K[q] == 'green':
                    pq_pairs.append((p, q))
                elif K[p] == 'green' and K[q] == 'blue':
                    pq_pairs.append((q, p))

    # skojarzenie w grafie dwudzielnym - dodajemy giga s i t z krawedziami z wagami 1
    # wszystkie wagi krawedzi w grafie ustawiamy na 1
    # puszczamy karpia na zer
    Max_matching = [[0 for v in range(V + 2)] for u in range(V + 2)]
    # s = V
    # t = V + 1
    for blue, green in pq_pairs:
        Max_matching[blue][green] = 1
        Max_matching[V][blue] = 1
        Max_matching[green][V + 1] = 1

    l = max_flow(Max_matching, V, V + 1)
    return l


Ta = [
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
]
Ka = ['blue', 'blue', 'green', 'green', 'blue']
Da = 2
print(blue_and_green(Ta, Ka, Da))
