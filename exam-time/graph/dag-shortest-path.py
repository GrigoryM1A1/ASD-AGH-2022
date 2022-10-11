"""Given a Weighted Directed Acyclic Graph and a source vertex in the graph,
find the shortest paths from given source to all other vertices."""


def dfs_visit(G, u, visited, res):
    visited[u] = True

    for v, w in G[u]:
        if not visited[v]:
            dfs_visit(G, v, visited, res)
    res.append(u)


def top_sort(G):
    V = len(G)
    res = []
    visited = [False for _ in range(V)]

    for u in range(V):
        if not visited[u]:
            dfs_visit(G, u, visited, res)

    return res


def dag_sh_paths(G, s):
    V = len(G)
    topological_order = top_sort(G)
    topological_order.reverse()

    dist = [float('inf') for _ in range(V)]
    dist[s] = 0

    for u in topological_order:
        for v, weight in G[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
    return dist


# (v, weight)
graph = [[(1, 5), (2, 3)],
         [(3, 6), (2, 2)],
         [(4, 4), (5, 2), (3, 7)],
         [(4, -1)],
         [(5, -2)],
         []]

print(dag_sh_paths(graph, 0))
