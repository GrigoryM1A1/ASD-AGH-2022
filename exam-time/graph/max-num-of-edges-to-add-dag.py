"""
A DAG is given to us, we need to find maximum number of edges that can be added to this DAG, after which new graph
still remain a DAG that means the reformed graph should have maximal number of edges, adding even single edge will
create a cycle in graph.
"""


def dfs_visit(G, u, visited, res):
    visited[u] = True

    for v in G[u]:
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


def num_of_edges_to_add(G):
    V = len(G)
    top = top_sort(G)
    degrees = [0 for _ in range(V)]

    for v in range(V):
        degrees[v] = len(G[v])

    count_edges = 0
    i = 1
    for u in top:
        deg = degrees[u]
        add = V - i - deg
        count_edges += add
        i += 1
    print(count_edges)


dag = [[],
       [],
       [3],
       [1],
       [0, 1],
       [2, 0]]
num_of_edges_to_add(dag)