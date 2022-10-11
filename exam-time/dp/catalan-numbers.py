"""
Find n'th catalan number
C0 = 1
Cn+1 = sum( Ci * Cn-i ) 0 <= i <= n

Cn = sum( Ci * Cn-i-1 ) 0 <= i < n
Cos jest zle ale nie wiem co
TODO
"""


def rec(n, dp):
    if dp[n] != 0:
        return dp[n]

    if n == 0 or n == 1:
        dp[n] = 1
        return dp[n]

    for i in range(n):
        dp[n] += rec(i, dp) * dp[n-i-1]

    return dp[n]


def catalan(n):
    F = [0 for _ in range(n+1)]
    # F[0] = F[1] = 1
    return rec(n, F)


print(catalan(4))
