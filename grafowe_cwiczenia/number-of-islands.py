def count_islands(G):
    def dfs_visit(Grid, length, width, i, j):
        nonlocal visited
        visited[i][j] = True
        moves = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]

        for x, y in moves:
            if 0 <= x < length and 0 <= y < width and Grid[x][y] == 1 and not visited[x][y]:
                dfs_visit(Grid, length, width, x, y)

    n = len(G)
    m = len(G[0])
    visited = [[False for l in range(m)] for k in range(n)]
    islands = 0

    for u in range(n):
        for v in range(m):
            if not visited[u][v] and G[u][v] == 1:
                dfs_visit(G, n, m, u, v)
                islands += 1
    return islands


G1 = [[0, 1],
      [1, 0],
      [1, 1],
      [1, 0]]
print(count_islands(G1))
G2 = [[0, 1, 1, 1, 0, 0, 0],
      [0, 0, 1, 1, 0, 1, 0]]
print(count_islands(G2))
