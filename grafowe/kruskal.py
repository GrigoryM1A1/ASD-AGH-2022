'''
Algorytm Kruskala - reprezentacja macierzowa - O(V^2 + ElogE)
'''
from queue import PriorityQueue


# class Node:
#     def __init__(self, val):
#         self.parent = self
#         self.value = val
#         self.rank = 0
#
#
# def find(x):
#     if x.parent != x:
#         x.parent = find(x.parent)
#
#     return x.parent
#
#
# def union(x, y):
#     x = find(x)
#     y = find(y)
#
#     if x == y:
#         return
#     if x.rank > y.rank:
#         y.parent = x
#     else:
#         x.parent = y
#         if x.rank == y.rank:
#             y.rank += 1
#     return


def find(x, p):
    if p[x] != x:
        p[x] = find(p[x], p)
    return p[x]


def union(x, y, p, r):
    x = find(x, p)
    y = find(y, p)

    if r[x] == r[y]:
        r[x] += 1

    if r[x] > r[y]:
        p[y] = x

    else:
        p[x] = y

    return


def kruskal(G):
    V = len(G)
    Edges = PriorityQueue()     # w postacie (waga, z, do)
    MST = []

    Parent = [v for v in range(V)]
    Rank = [1 for _ in range(V)]
    for v in range(V):
        for u in range(v, V):
            if G[u][v] >= 0:     # tu rownie dobrze moze byc -1
                Edges.put((G[v][u], v, u))

    while not Edges.empty():
        weight, u, v = Edges.get()
        x = find(u, Parent)
        y = find(v, Parent)
        if x != y:
            MST.append((u, v))
            union(x, y, Parent, Rank)
    print(MST)
    return MST


graph = [[-1, 1, 6, -1, -1, -1, -1, -1, -1],
         [1, -1, -1, -1, 2, 10, -1, -1, -1],
         [6, -1, -1, 5, -1, -1, -1, -1, -1],
         [-1, -1, 5, -1, 3, -1, -1, 8, -1],
         [-1, 2, -1, 3, -1, -1, 4, -1, -1],
         [-1, 10, -1, -1, -1, -1, 9, -1, 11],
         [-1, -1, -1, -1, 4, 9, -1, 7, -1],
         [-1, -1, -1, 8, -1, -1, 7, -1, -1],
         [-1, -1, -1, -1, -1, 11, -1, -1, -1]]
kruskal(graph)
