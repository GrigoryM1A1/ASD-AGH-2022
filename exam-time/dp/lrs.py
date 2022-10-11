"""
Longest repeated subsequence
Given a string, print the longest repeating subsequence such that the two subsequence
don’t have same string character at same position, i.e., any i’th character in the two
subsequences shouldn’t have the same index in the original string.
"""


def lrs(A):
    n = len(A)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                pass
            elif A[i-1] == A[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    i = j = n
    sub = ""
    while i > 0 and j > 0:
        if A[i-1] == A[j-1] and i != j:
            sub += A[i-1]
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    sub = sub[::-1]
    print(sub)
    return dp[n][n]


print(lrs('AABEBCDD'))
