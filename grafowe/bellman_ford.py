"""
Bellman-Ford - lista sasiedztwa - O(VE)
Dziala na grafach skierowanych, ktore moga miec ujemne wagi
Dziala na grafach nieskierowanych ale wagi musza byc nieujemne
"""


def bellman_ford(G, s):
    V = len(G)
    inf = float('inf')

    Dist = [inf for _ in range(V)]
    Dist[s] = 0
    Parent = [None for _ in range(V)]

    for i in range(V-1):
        for u in range(V):
            for v in G[u]:
                if Dist[v[0]] > Dist[u] + v[1]:
                    Dist[v[0]] = Dist[u] + v[1]
                    Parent[v[0]] = u
    for i in range(V-1):
        for u in range(V):
            for v in G[u]:
                if Dist[u] + v[1] < Dist[v[0]]:
                    Dist[v[0]] = -inf
                    Parent[v[0]] = None
    print(Dist)


graph = [[(1, 5)],
         [(6, 60), (5, 30), (2, 20)],
         [(3, 10), (4, 75)],
         [(2, -15)],
         [(9, 100)],
         [(6, 5), (8, 50), (4, 25)],
         [(7, -50)],
         [(8, -10)],
         [],
         []]
# bellman_ford(graph, 0)
graph1 = [[(1, 1), (7, 2)],  # 0
          [(0, 1), (2, 2), (4, 3)],  # 1
          [(1, 2), (3, 5)],  # 2
          [(2, 5), (6, 1)],  # 3
          [(1, 3), (5, 3), (7, 1)],  # 4
          [(4, 3), (8, 1), (6, 8)],  # 5
          [(3, 1), (5, 8), (8, 4)],  # 6
          [(0, 2), (4, 1), (8, 7)],  # 7
          [(7, 7), (5, 1), (6, 4)]]  # 8
bellman_ford(graph1, 0)
