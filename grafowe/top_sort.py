'''
Sortowanie topologiczne - lista sasiedztwa - O(V+E)
'''
import collections


def top_sort(G):
    def DFSVisit(G, u):
        nonlocal visited, res
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v)
        res.appendleft(u)

    V = len(G)
    visited = [False for _ in range(V)]
    res = collections.deque([])

    for u in range(V):
        if not visited[u]:
            DFSVisit(G, u)

    return res


Graph = [[1, 2, 6],
         [2, 3],
         [],
         [4, 5],
         [],
         [],
         [3]]
print(top_sort(Graph))
