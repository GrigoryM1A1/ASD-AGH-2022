"""
Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that
cell, we need to find a path from top left cell to bottom right cell by which the total cost incurred is minimum.
From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j).

Note: It is assumed that negative cost cycles do not exist in the input matrix.
"""
import heapq


def available_moves(i, j, n):
    jumps = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
    moves = []
    for x, y in jumps:
        if 0 <= x < n and 0 <= y < n:
            moves.append((x, y))
    return moves


def min_path(G):
    V = len(G)
    inf = float('inf')
    Dist = [[inf for v in range(V)] for u in range(V)]
    Dist[0][0] = G[0][0]

    PQ = []
    heapq.heapify(PQ)
    heapq.heappush(PQ, (Dist[0][0], 0, 0))
    while PQ:
        cost, x, y = heapq.heappop(PQ)
        moves = available_moves(x, y, V)

        for i, j in moves:
            if Dist[i][j] > Dist[x][y] + G[i][j]:
                Dist[i][j] = Dist[x][y] + G[i][j]
                heapq.heappush(PQ, (Dist[i][j], i, j))
    return Dist[V-1][V-1]


G1 = [[9, 4, 9, 9],
      [6, 7, 6, 4],
      [8, 3, 3, 7],
      [7, 4, 9, 10]]
print(min_path(G1))

G2 = [[4, 4],
      [3, 7]]
print(min_path(G2))
