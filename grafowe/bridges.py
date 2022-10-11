def bridges(G):
    def DFS_visit(G, u, parent):
        nonlocal visit_time, time, low, res
        visit_time[u] = time
        low[u] = visit_time[u]
        time += 1

        temp = low_child = float('inf')

        for v in G[u]:
            if visit_time[v] == -1:
                child = DFS_visit(G, v, u)
                if child == visit_time[v]:
                    res.append((u, v))
                low_child = min(low_child, child)
            elif v != parent:
                temp = min(temp, low[v])

        low[u] = min(low[u], temp, low_child)

        return low[u]

    time = 0
    n = len(G)
    visit_time = [-1] * n
    low = [-1] * n
    res = []

    for i in range(n):
        if visit_time[i] == -1:
            DFS_visit(G, i, i)

    return res


G1 = [[3, 1],
      [0, 2],
      [5, 1, 3],
      [2, 0, 4],
      [3],
      [7, 6, 2],
      [7, 5],
      [5, 6]]
print(bridges(G1))
