"""
Trzeba pokolorawac wszystko na 1 kolor
"""


def available_moves(i, j, n):
    jumps = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]
    moves = []
    for x, y in jumps:
        if 0 <= x < n and 0 <= y < n:
            moves.append((x, y))
    return moves


def dfs_visit(G, i, j, color_to_change, new_color):
    G[i][j] = new_color
    print(i, j)
    moves = available_moves(i, j, len(G))

    for x, y in moves:
        if G[x][y] != new_color and G[x][y] == color_to_change:
            dfs_visit(G, x, y, color_to_change, new_color)


def flood_fill(G, x, y, new_color):
    V = len(G)
    color_to_change = G[x][y]

    G[x][y] = new_color
    moves = available_moves(x, y, V)
    for i, j in moves:
        if G[i][j] != new_color and G[i][j] == color_to_change:
            dfs_visit(G, i, j, color_to_change, new_color)

    for row in G:
        print(row)


Table = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
flood_fill(Table, 1, 1, 2)
