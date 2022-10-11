"""
Prim - macierzowa
"""
from queue import PriorityQueue


def prim(G, s):
    V = len(G)
    PQ = PriorityQueue()
    inf = float('inf')
    Weights = [inf for _ in range(V)]
    Parent = [None for _ in range(V)]
    Weights[s] = 0
    PQ.put((Weights[s], s))

    while not PQ.empty():
        weight, t = PQ.get()
        for u in range(V):
            if -1 < G[t][u] <= Weights[u]:  # G[t][u] > -1 and Weights[u] >= G[t][u]
                Weights[u] = G[t][u]
                Parent[u] = t
                PQ.put((Weights[u], u))

    res = []
    for v in range(V):
        if Parent[v] is not None:
            res.append((v, Parent[v]))
    print(res)


graph = [[-1, 1, 6, -1, -1, -1, -1, -1, -1],
         [1, -1, -1, -1, 2, 10, -1, -1, -1],
         [6, -1, -1, 5, -1, -1, -1, -1, -1],
         [-1, -1, 5, -1, 3, -1, -1, 8, -1],
         [-1, 2, -1, 3, -1, -1, 4, -1, -1],
         [-1, 10, -1, -1, -1, -1, 9, -1, 11],
         [-1, -1, -1, -1, 4, 9, -1, 7, -1],
         [-1, -1, -1, 8, -1, -1, 7, -1, -1],
         [-1, -1, -1, -1, -1, 11, -1, -1, -1]]
prim(graph, 0)
