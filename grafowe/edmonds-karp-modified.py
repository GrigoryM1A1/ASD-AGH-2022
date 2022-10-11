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
    F = [[G[i][j] for j in range(V)] for i in range(V)]
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
    # for row in F:
    #     print(row)
    return flow


# Graph = [[0, 4, 0, 3, 0, 0],
#          [0, 0, 2, 2, 0, 0],
#          [0, 0, 0, 0, 0, 4],
#          [0, 0, 2, 0, 2, 0],
#          [0, 0, 0, 0, 0, 5],
#          [0, 0, 0, 0, 0, 0]]
# # print(max_flow(Graph, 0, 5))
# graph = [[0, 16, 13, 0, 0, 0],
#          [0, 0, 10, 12, 0, 0],
#          [0, 4, 0, 0, 14, 0],
#          [0, 0, 9, 0, 0, 20],
#          [0, 0, 0, 7, 0, 4],
#          [0, 0, 0, 0, 0, 0]]
# print(max_flow(graph, 0, 5))
