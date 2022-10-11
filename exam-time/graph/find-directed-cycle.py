"""
Given a directed graph, check whether the graph contains a cycle or not.
Your function should return true if the given graph contains at least one cycle, else return false.
"""


def dfs_visit(G, u, visited, tree_visited):
    visited[u] = True
    tree_visited[u] = True

    for v in G[u]:
        if not visited[v] and dfs_visit(G, v, visited, tree_visited):
            return True
        elif tree_visited[v]:
            return True
    tree_visited[u] = False
    return False


def detect_dir_cycle(G):
    V = len(G)
    visited = [False for _ in range(V)]
    tree_visited = [False for _ in range(V)]

    for u in range(V):
        if not visited[u] and dfs_visit(G, u, visited, tree_visited):
            return True
    return False


graph = [[2, 1],
         [2],
         [0, 3],
         []]
