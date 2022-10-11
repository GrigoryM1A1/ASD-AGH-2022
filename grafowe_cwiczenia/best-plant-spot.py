"""
We want to build a new plant in the following network,
nodes are places and links represent costs to send energy from one place to another.
"""
# Idea: Puszczamy Floyda-Warshalla i szukamy wirzchołka, gdzie sumy udkległości są najmniejsze do reszty


def find_best_spot(G):
    V = len(G)
    inf = float('inf')
    D = [G[i][:] for i in range(V)]

    for u in range(V):
        for v in range(V):
            if u != v and D[u][v] == 0:
                D[u][v] = inf

    for k in range(V):
        for u in range(V):
            for v in range(V):
                D[u][v] = min(D[u][v], D[u][k] + D[k][v])

    best_spot = -1
    min_sum = inf
    for i, row in enumerate(D):
        curr = sum(row)
        if curr < min_sum:
            min_sum = curr
            best_spot = i

    return best_spot


Plant = [[0, 3, 5, 9, 0, 0],
         [3, 0, 3, 4, 7, 0],
         [5, 3, 0, 2, 6, 8],
         [9, 4, 2, 0, 2, 2],
         [0, 7, 6, 2, 0, 5],
         [0, 0, 8, 2, 5, 0]]
print(find_best_spot(Plant))
