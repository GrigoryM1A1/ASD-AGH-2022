"""
Given a gold mine of n*m dimensions.
Each field in this mine contains a positive integer which is the amount of gold in tons.
Initially the miner is at first column but can be at any row. He can move only (right->,right up /,right down\)
that is from a given cell, the miner can move to the cell diagonally up towards the right or right or diagonally down
towards the right. Find out maximum amount of gold he can collect.
"""


# f(i, j) = maksymalna liczba wykopanego zlota po dojsciu do pola i, j
def get_moves(i, j, n, m):
    jumps = [(i-1, j-1), (i, j-1), (i+1, j-1)]
    moves = []
    for x, y in jumps:
        if 0 <= x < n and 0 <= y < m:
            moves.append((x, y))
    return moves


def goooold(Mines):
    n = len(Mines)
    m = len(Mines[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = Mines[i][0]

    for j in range(1, m):
        for i in range(n):
            moves = get_moves(i, j, n, m)
            q = -1
            # bierzemy maxa z mozliwych wykonannych ruchow
            for x, y in moves:
                q = max(q, dp[x][y])
            dp[i][j] = q + Mines[i][j]

    max_ = -1
    for i in range(n):
        max_ = max(max_, dp[i][-1])
    for row in dp:
        print(row)
    return max_


grid = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]
print(goooold(grid))
