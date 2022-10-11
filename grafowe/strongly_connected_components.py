'''
Silnie spojne skladowe - lista sasiedztwa
'''


def reverse_edges(G):
    V = len(G)
    R_edges = [[] for _ in range(V)]

    for v in range(V):
        for u in G[v]:
            R_edges[u].append(v)

    return R_edges


def strongly_connected_components(G):
    def DFSVisit(G, u):
        nonlocal time, t, visited
        time += 1
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v)
        time += 1
        t[u] = time

    def second_DFS(G, u):
        nonlocal scc, visited, curr_component
        visited[u] = True
        scc[curr_component].append(u)
        for v in G[u]:
            if not visited[v]:
                second_DFS(G, v)

    V = len(G)
    visited = [False for _ in range(V)]
    t = [-1 for _ in range(V)]
    time = 0

    # pierwszy dfs
    for u in range(V):
        if not visited[u]:
            DFSVisit(G, u)
    # posortowanie po czasie przetworzenia
    for i in range(V):
        t[i] = (i, t[i])
    t.sort(key=lambda x: x[1], reverse=True)
    # odwrocenie krawedzi
    R = reverse_edges(G)
    # drugi dfs
    visited = [False for _ in range(V)]
    scc = []
    curr_component = 0
    for u in t:
        if not visited[u[0]]:
            scc.append([])
            second_DFS(R, u[0])
            curr_component += 1

    # zwracamy teblice ze spojnymi skladowymi
    return scc


Graph = [[2],
         [0, 6],
         [1, 7],
         [6],
         [3, 8],
         [4],
         [5],
         [10],
         [7, 9],
         [10],
         [8]]
print(strongly_connected_components(Graph))
