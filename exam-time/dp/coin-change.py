"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm}
valued coins, how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
So the output should be 5.
"""


def num_of_changes(n, m, S):
    dp = [[0 for _ in range(m)] for _ in range(n+1)]
    for i in range(m):
        dp[0][i] = 1

    for i in range(1, n+1):
        for j in range(m):
            x = y = 0
            # bierzemy dany nominal
            if i - S[j] >= 0:
                x = dp[i-S[j]][j]

            # pomijamy dany nominal
            if j >= 1:
                y = dp[i][j-1]

            dp[i][j] = x + y
    return dp[n][m-1]


print(num_of_changes(10, 4, [2, 5, 3, 6]))
