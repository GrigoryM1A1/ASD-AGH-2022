"""
lcs ale len(A) == len(B)
"""


def lcs(A, B):
    n = len(A)
    F = [[0 for i in range(n + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                F[i][j] = 0
            elif A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i][j - 1], F[i - 1][j])
    print(F[n][n])
    return F[n][n]


'''
lcs ale len(A) != len(B)
'''


def lcs_dif_lens(A, B):
    m = len(A)
    n = len(B)
    F = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                F[i][j] = 0
            elif A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[m][n]


X = "AGGTABSC"
Y = "GXTXAYBC"
lcs(X, Y)
print(lcs_dif_lens(X, Y))
