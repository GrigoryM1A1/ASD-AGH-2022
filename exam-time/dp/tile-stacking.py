"""
A stable tower of height n is a tower consisting of exactly n tiles of unit height stacked vertically in such a way,
that no bigger tile is placed on a smaller tile.
We have an infinite number of tiles of sizes 1, 2, …, m. The task is to calculate the number of the different stable
towers of height n that can be built from these tiles, with a restriction
that you can use at most k tiles of each size in the tower.
Note: Two towers of height n are different if and only if there exists a height h (1 <= h <= n),
such that the towers have tiles of different sizes at height h.
"""


# mamy nieskonczenie wiele klockow rozmiarow 1 ... m
# mamy ulozyc jak najwiecej wiez (kazda wysokosci n)
# w kazdej wiezy mozemy uzyc maks k klockow tego samego rodzaju
# O(n*m*k)
def tiles_rec(i, j, k, dp):
    if dp[i][j] != -1:
        return dp[i][j]

    if i == 0:
        dp[i][j] = 1
        return dp[i][j]

    if j == 0:
        dp[i][j] = 0
        return dp[i][j]

    q = 0
    for x in range(k):
        q += tiles_rec(i - x, j - 1, k, dp)
    dp[i][j] = q
    return dp[i][j]


def tile_stacking(m, n, k):
    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    tiles_rec(n, m, k, dp)
    return dp[n][m]

