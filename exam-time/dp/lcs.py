"""
Longest common subsequence
"""


def lcs(A, B):
    m = len(A)
    n = len(B)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                pass
            elif A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # printing lcs
    subs = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            subs += A[i-1]
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    subs = subs[::-1]
    print(subs)

    return dp[m][n]


X = "AGGTAB"
Y = "GXTXAYB"
print(lcs(X, Y))
