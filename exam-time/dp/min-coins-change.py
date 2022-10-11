"""
Given a value V, if we want to make a change for V cents, and we have an infinite supply of each of
C = { C1, C2, .., Cm} valued coins, what is the minimum number of coins to make the change?
If it’s not possible to make a change, print -1.

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required We can use one coin of 25 cents and one of 5 cents

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required We can use one coin of 6 cents and 1 coin of 5 cents
"""

'''
dp(i) = minimalna liczba monet potrzebna na wydanie wartosci i
dp(i) = min{ dp(i), dp(i - C[coin] } if i - C[coin] >= 0 and 0 <= coin < m
'''


def min_coins(V, C):
    m = len(C)
    dp = [float('inf') for _ in range(V + 1)]
    dp[0] = 0

    for i in range(1, V + 1):
        q = dp[i]
        for coin in range(m):
            if i - C[coin] >= 0:
                q = min(q, 1 + dp[i - C[coin]])
        dp[i] = q
    # print(dp)
    if dp[V] == float('inf'):
        return -1
    return dp[V]


print(min_coins(30, [25, 10, 5]))
print(min_coins(11, [9, 6, 5, 1]))
print(min_coins(7, [3, 6, 9]))
