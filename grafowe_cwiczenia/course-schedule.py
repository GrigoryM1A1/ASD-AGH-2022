"""
There are a total of n tasks you have to pick, labeled from 0 to n-1. Some tasks may have prerequisites tasks,
for example to pick task 0 you have to first finish tasks 1, which is expressed as a pair: [0, 1]
Given the total number of n tasks and a list of prerequisite pairs of size m.
Find a ordering of tasks you should pick to finish all tasks.
Note: There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all tasks, return an empty array. Returning any correct order will give the output as 1,
whereas any invalid order will give the output 0.
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


def directed_graph_cycle(G):
    N = len(G)
    visited = [False for _ in range(N)]
    curr_visited = [False for _ in range(N)]

    for u in range(N):
        if not visited[u]:
            if dfs_visit(G, u, visited, curr_visited):
                return True
    return False


def schedule(n, m, prerequisites):
    def top_sort(G, u):
        nonlocal visited, res
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                top_sort(G, v)
        res.append(u)

    G = [[] for _ in range(n)]
    res = []
    for edge_to, edge_from in prerequisites:
        G[edge_from].append(edge_to)

    if directed_graph_cycle(G):
        return res

    visited = [False for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            top_sort(G, u)

    res.reverse()
    return res


print(schedule(n=4, m=3, prerequisites=[[1, 0], [2, 1], [3, 2]]))     # YES
print(schedule(n=2, m=2, prerequisites=[[0, 1], [1, 0]]))             # NO
