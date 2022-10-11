"""
There are a total of N tasks, labeled from 0 to N-1. Some tasks may have prerequisites, for example to do task 0 you
have to first complete task 1, which is expressed as a pair: [0, 1]
Given the total number of tasks N and a list of prerequisite pairs P, find if it is possible to finish all tasks.

Upraszcza sie do znalezienia cyklu w grafie skierowanym
"""


def dfs_visit(G, u, visited, curr_visited):
    visited[u] = True
    curr_visited[u] = True
    for v in G[u]:
        if not visited[v]:
            if dfs_visit(G, v, visited, curr_visited):
                return True
        elif curr_visited[v]:
            return True
    curr_visited[u] = False
    return False


def prerequisite_tasks(N, P, prerequisites):
    G = [[] for _ in range(N)]
    visited = [False for _ in range(N)]
    curr_visited = [False for _ in range(N)]
    for edge_to, edge_from in prerequisites:
        G[edge_from].append(edge_to)

    for u in range(N):
        if not visited[u]:
            if dfs_visit(G, u, visited, curr_visited):
                return False                            # ale to ocznacza, ze jest cykl
    return True     # ale to oznacza, ze nie ma cyklu


print(prerequisite_tasks(N=4, P=3, prerequisites=[[1, 0], [2, 1], [3, 2]]))     # YES
print(prerequisite_tasks(N=2, P=2, prerequisites=[[0, 1], [1, 0]]))             # NO
