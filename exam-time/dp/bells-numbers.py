"""
S(n, k) = S(n-1, k-1) + k*S(n-1, k), 0 < k < n
S(n, n) = 1, n >= 0
S(n, 0) = 0, n > 0

B(n) = sum( S(n, k) ), 0 <= k <= n
"""


def bell(n):
    S = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        S[i][i] = 1

    number = 0
    for i in range(n+1):
        for k in range(i):
            S[i][k] = (S[i-1][k-1] + k * S[i-1][k])

    for row in S:
        print(row)

    for k in range(n+1):
        number += S[n][k]
    return number


print(bell(3))

