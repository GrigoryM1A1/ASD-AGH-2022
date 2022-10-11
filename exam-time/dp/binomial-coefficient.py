"""
Symbol Newtona:
C(n, k) = C(n-1, k-1) + C(n-1, k)
C(n, 0) = C(n, n) = 1
"""


def rec(n, k, dp):
    if dp[n][k] != -1:
        return dp[n][k]

    if n == k or k == 0:
        dp[n][k] = 1
        return dp[n][k]

    dp[n][k] = rec(n-1, k-1, dp) + rec(n-1, k, dp)
    return dp[n][k]


def binomial_coefficient(n, k):
    dp = [[-1 for _ in range(k+1)] for _ in range(n+1)]
    return rec(n, k, dp)


print(binomial_coefficient(5, 2))
