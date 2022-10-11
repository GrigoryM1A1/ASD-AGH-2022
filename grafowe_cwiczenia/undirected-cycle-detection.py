"""
Szukamy czy istnieje cykl w grafie nieskierowanym
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 0


def find_set(x):
    if x.parent != x:
        x.parent = find_set(x.parent)
    return x.parent


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
    return


def is_cycle(G):
    V = len(G)
    Edges = []
    disjoint_set = [Node(v) for v in range(V)]

    for v in range(V):
        for u in G[v]:
            if not u < v:
                Edges.append((v, u))

    for u, v in Edges:
        x = find_set(disjoint_set[u])
        y = find_set(disjoint_set[v])
        if x != y:
            union(x, y)
        else:
            return True
    return False


G1 = [[1],
      [0, 4, 2],
      [3, 1],
      [2, 4],
      [3, 1]]
print(is_cycle(G1))

G2 = [[],
      [2],
      [3, 1],
      [2]]
print(is_cycle(G2))
