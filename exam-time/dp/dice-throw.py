"""Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X.
X is the summation of values on each face when all the dice are thrown."""


# O(m*n*X)
def dice_throws(X, n, m):
    dp = [[0 for _ in range(X + 1)] for _ in range(n + 1)]

    for i in range(1, min(m + 1, X + 1)):
        dp[1][i] = 1

    for i in range(2, n + 1):
        for j in range(1, X + 1):
            for k in range(1, min(m + 1, j)):
                # sprawdzamy dla kazdej mozliwej scianki dla danej kostki
                dp[i][j] += dp[i-1][j-k]
    for row in dp:
        print(row)


dice_throws(8, 3, 6)




