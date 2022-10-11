"""
Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that maximizes product of
lengths of all parts. You must make at least one cut. Assume that the length of rope is more than 2 meters.
"""


"""
dp[i] = max product of cutting rod of the length n
dp[i] = max( k*(i-k), dp[i - k] * k ), 1 <= k <= i
dp[0] = 0
dp[1] = 0
"""


def rec(i, dp):
    if dp[i] != -1:
        return dp[i]

    max_ = 0
    for k in range(1, i + 1):
        max_ = max(max_, k * (i - k), rec(i - k, dp) * k)

    dp[i] = max_
    return dp[i]


def max_rod_product(n):
    dp = [-1 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 0
    rec(n, dp)
    print(dp)
    return dp[n]


print(max_rod_product(10))
