"""
Given two numbers n and k where n represents a number of elements in a set,
find a number of ways to partition the set into k subsets.
"""


def stirling_II(n, k):
    S = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        S[i][i] = 1

    # S(n, k) = S(n - 1, k - 1) + k * S(n - 1, k)
    for i in range(n + 1):
        for j in range(i):
            S[i][j] = S[i - 1][j - 1] + j * S[i - 1][j]
    return S[n][k]


print(stirling_II(5, 2))
