"""
Given two integers m & n, find the number of possible sequences of length n such that each of the next element
is greater than or equal to twice of the previous element but less than or equal to m.

m = zakres liczb (1, 2, ... 10)
n = krotki rozmiaru n
"""

"""
If it is m, then the (n-1)th element is at most m/2. We recur for m/2 and n-1.
If it is not m, then it is at most is m-1. We recur for (m-1) and n.
"""


def sequences(m, n):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m + 1):
        dp[i][1] = i

    for i in range(1, m + 1):
        for j in range(2, n + 1):
            # bierzemy wartość j + nie bierzemy wartosci j ale rozpatrujemy i // 2
            dp[i][j] = dp[i-1][j] + dp[i // 2][j-1]

    return dp[m][n]


print(sequences(10, 4))
print()
print(sequences(5, 2))
