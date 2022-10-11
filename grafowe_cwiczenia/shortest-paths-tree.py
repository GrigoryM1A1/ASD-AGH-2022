"""
Dany jest graf wazony G, oraz dzrewo rozpinajace T zawierajace wierzcholek s. Podaj algorytm, ktory sprawdzi
czy T jest drzewem najkrotszych sciezek od wierzcholka s.
"""

'''
Moj pomysl:
Robimy dijkstre, tworzymy drzewo najkrotszych sciezek i porownoujemy z drzewem T - da sie szybciej

Pomysl z bitalgo:
Sprawdzamy czy dla ktoregokolwiek wierzcholka w drzewie mozna wykonac relaksacje
'''
import heapq


def shortest_paths_tree(G, T, s):
    V = len(G)
    # dijkstra dla drzewa ElogV, ale E = V-1, czyli mamy VlogV tak naprawde, łacznie O(VlogV + E)
    tree_dist = [float('inf') for _ in range(V)]
    tree_dist[s] = 0
    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q, (tree_dist[s], s))
    while Q:
        weight, u = heapq.heappop(Q)
        for v in range(V):
            if T[u][v] > 0:
                new_dist = tree_dist[u] + T[u][v]
                if new_dist < tree_dist[v]:
                    tree_dist[v] = new_dist
                    heapq.heappush(Q, (tree_dist[v], v))

    for u in range(V):
        for v in range(V):
            if G[u][v] > 0:
                new_dist = tree_dist[u] + G[u][v]
                if new_dist < tree_dist[v]:
                    return False

    return True


G1 = [[0, 2, 0, 0, 0, 3],
      [2, 0, 8, 0, 5, 0],
      [0, 8, 0, 1, 0, 0],
      [0, 0, 1, 0, 1, 0],
      [0, 5, 0, 1, 0, 1],
      [3, 0, 0, 0, 1, 0]]

T_ok = [[0, 2, 0, 0, 0, 3],
        [2, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [3, 0, 0, 0, 1, 0]]
print(shortest_paths_tree(G1, T_ok, 0))

T_nope = [[0, 2, 0, 0, 0, 3],
          [2, 0, 8, 0, 0, 0],
          [0, 8, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 1],
          [3, 0, 0, 0, 1, 0]]
print(shortest_paths_tree(G1, T_nope, 0))
