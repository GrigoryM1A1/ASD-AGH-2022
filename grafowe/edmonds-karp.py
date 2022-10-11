from collections import deque


def bfs(G, s, t, parent):
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
                    return True
                visited[v] = True
                parent[v] = u
                Q.append(v)
    return False


def edmonds_karp_max_flow(G, s, t):
    V = len(G)
    parent = [None for _ in range(V)]
    inf = float('inf')
    flow = 0
    F = [[G[i][j] for j in range(V)] for i in range(V)]

    while bfs(F, s, t, parent):  # szukanie nowej sciezki powiekszajacej
        u = t
        bottle_neck = inf
        while u != s:  # szukanie bottle_necka
            bottle_neck = min(bottle_neck, F[parent[u]][u])
            u = parent[u]
        flow += bottle_neck

        v = t  # odpowiednie zmneijszanie sieci residualnej
        while v != s:
            x = parent[v]
            F[x][v] -= bottle_neck
            F[v][x] += bottle_neck
            v = parent[v]

    return flow


Graph = [[0, 4, 0, 3, 0, 0],
         [0, 0, 2, 2, 0, 0],
         [0, 0, 0, 0, 0, 4],
         [0, 0, 2, 0, 2, 0],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0]]
print(edmonds_karp_max_flow(Graph, 0, 5))
graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]
print(edmonds_karp_max_flow(graph, 0, 5))
