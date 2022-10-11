"""
https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/mr-president/
"""

"""
My idea:
Build MST and exchange most valuable edges to super roads until we fit in K
"""


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, rank, parent):
    x = find(x, parent)
    y = find(y, parent)

    if x == y:
        return

    if rank[x] > rank[y]:
        parent[y] = x

    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1
    return


def great_administrator(N, M, K, G):
    # N - number of cities
    # M - number of roads
    # K - desired cost of maintenance
    # G - [(Ai, Bi, Cost)] - all roads are bidirected
    # return minimal number of roads to transform into a super road
    G.sort(key=lambda edge: edge[2])
    Parent = [v for v in range(N)]
    Rank = [1 for _ in range(N)]
    MST_cost = 0
    MST_size = 0
    super_roads = 0
    for u, v, cost in G:
        u -= 1
        v -= 1
        u = find(u, Parent)
        v = find(v, Parent)
        if u != v:
            union(u, v, Rank, Parent)
            MST_cost += cost
            MST_size += 1

            new_cost = MST_cost + MST_size - 1
            if new_cost <= K:
                super_roads = MST_size

    return super_roads


Roads = [(1, 2, 10), (2, 3, 20), (3, 1, 30)]
print(great_administrator(3, 3, 25, Roads))
