"""
Unbounded knapsakc - knapsack but with repetition of items
"""


def knap_rec(W, P, B, dp, ind):
    # there's only one type of item in our knapsack
    if ind == 0:
        return (B // W[0]) * P[0]

    if dp[ind][B] != -1:
        return dp[ind][B]

    exclude = 0 + knap_rec(W, P, B, dp, ind - 1)
    include = -float('inf')
    if B - W[ind] >= 0:
        include = P[ind] + knap_rec(W, P, B - W[ind], dp, ind)

    dp[ind][B] = max(include, exclude)
    return dp[ind][B]


def unbounded_knapsack(W, P, B):
    n = len(W)
    F = [[-1 for b in range(B+1)] for i in range(n)]
    knap_rec(W, P, B, F, n - 1)
    return F[n-1][B]


print(unbounded_knapsack([5, 10, 15], [10, 30, 20], 100))
