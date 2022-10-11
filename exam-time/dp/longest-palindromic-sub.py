"""
Given a sequence, find the length of the longest palindromic subsequence in it.
"""


# Method 1
# res = dp[0][n-1]
# dp[i][i] = 1
# dp[i][j] = dp[i+1][j-1] + 2 if S[i] == S[j] else max(dp[i][j-1], dp[i+1][j])
def rec(S, dp, i, j):
    if j < i:
        return dp[j][i]

    if dp[i][j] != -1:
        return dp[i][j]

    if S[i] == S[j]:
        dp[i][j] = rec(S, dp, i + 1, j - 1) + 2
        return dp[i][j]

    dp[i][j] = max(rec(S, dp, i, j - 1), rec(S, dp, i + 1, j))
    return dp[i][j]


def longest_palindromic_sub(S):
    n = len(S)
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
    rec(S, dp, 0, n - 1)
    return dp[0][n - 1]


# Method 2
# lcs(S1, S2); S1 == our string, S2 == our string but reversed
def lps_with_lcs(S):
    n = len(S)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    Z = S[::-1]

    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                pass
            elif S[i - 1] == Z[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # print palindrom
    palindrom = ""
    i = j = n
    while i > 0 and j > 0:
        if S[i - 1] == Z[j - 1]:
            palindrom += S[i - 1]
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[n][n], palindrom


print(longest_palindromic_sub("GEEKSFORGEEKS"))
print()
print(lps_with_lcs("GEEKSFORGEEKS"))
