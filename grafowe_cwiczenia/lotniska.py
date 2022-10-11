"""
Dostajemy na wejsciu liste trojek (miastoA, miastoB, koszt). Kazda z nich oznacza,
ze mozemy zbudowac droge miedzy miastem A i B za podany koszt. Ponadto w dowolnym
miescie mozemy zbydowac lotnisko za koszt K, niezalezny od miasta. Na poczadtku w
zadnym miescie nie ma lotniska, podobnie miedzy zadnymi dwoma miastami nie ma wybudowanej
drogi. Naszym celem jest zbudowac lotniska i drogi za minimalny laczny koszt, tak aby
kazde miasto mialo dostep do lotniska.

Miasto ma dostep do lotniska jesli:
1) jest w nim lotnisko
lub
2) mozna do niego doejachc do innego miasta, w ktorym jest lotnisko

Jesli istnieje wiecej niz jedno rozwiazanie o min. koszcie to nalezy wybrac to z
najwieksza liczba lotnisk.
"""

'''
Moj pomysl:
1) Puszczamy kruskala
2) Jak bierzemy po kolei miasta to jak bardziej nam się opyla zbudowac lotnisko to budujemy lotnisko

Czyli tak jakby dzielimy graf na takie mniejsze minimalne drzewa rozpinajace i pozniej budujemy tyle lotnisk 
ile nam wyszlo tych mniejszych drzewek

Miasta numerowane od 0
'''

import heapq


class Node:
    def __init__(self):
        self.parent = self
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
    return


def airport(G, K):
    E = len(G)
    min_cost = 0
    V = -1
    PQ = []
    heapq.heapify(PQ)

    for u, v, cost in G:
        V = max(V, u, v)
        heapq.heappush(PQ, (cost, u, v))
    V += 1
    Disjoint_set = [Node() for _ in range(V)]
    while PQ:
        cost, u, v = heapq.heappop(PQ)
        x = find(Disjoint_set[u])
        y = find(Disjoint_set[v])
        if x != y:
            if cost < K:
                union(x, y)
                min_cost += cost
            else:
                union(x, y)
                min_cost += K
    return min_cost


# (u, v, koszt)
Roads = [(2, 4, 100), (4, 6, 1), (5, 4, 4), (6, 7, 1), (3, 4, 3), (2, 7, 150),
         (0, 1, 2), (1, 2, 2,), (2, 0, 5), (8, 9, 1), (9, 0, 99)]
# chyba działa
print(airport(Roads, 50))
