'''
DFS - lista sasiedztwa - O(V+E)
'''


def dfs(G):
    def DFSVisit(G, u):
        nonlocal time, visited, parent
        time += 1
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(G, v)
        time += 1

    V = len(G)
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]

    time = 0
    for u in range(V):
        if not visited[u]:
            DFSVisit(G, u)
    print(parent)
    print(visited)


def dfs_matrix(G):
    def DFSVisit(G, u):
        nonlocal visited, vertices
        visited[u] = True

        for v in range(V):
            if G[u][v] > -1 and not visited[v]:
                vertices.append(v)
                DFSVisit(G, v)

    V = len(G)
    visited = [False for _ in range(V)]
    vertices = [0]

    for u in range(V):
        if not visited[u]:
            DFSVisit(G, u)
    print(vertices)
    return visited


Graph = [[3],
         [2, 3],
         [1, 3],
         [0, 1, 2, 4],
         [3, 5],
         [4, 6, 7],
         [5],
         [5]]

Graph_matrix = [[-1, -1, -1, 10, -1, -1, -1, -1],
                [-1, -1, 10, 10, -1, -1, -1, -1],
                [-1, 10, -1, 10, -1, -1, -1, -1],
                [10, 10, 10, -1, 10, -1, -1, -1],
                [-1, -1, -1, 10, -1, 10, -1, -1],
                [-1, -1, -1, -1, 10, -1, 10, 10],
                [-1, -1, -1, -1, -1, 10, -1, -1],
                [-1, -1, -1, -1, -1, 10, -1, -1]]

print(dfs_matrix(Graph_matrix))
