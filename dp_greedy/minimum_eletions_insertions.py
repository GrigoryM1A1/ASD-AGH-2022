def lcs(A, B):
    m = len(A)
    n = len(B)
    F = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                F[i][j] = 0
            elif A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i][j-1], F[i-1][j])
    return F[m][n]


def num_of_del_and_ins(str1, str2):
    m = len(str1)
    n = len(str2)
    strings_lcs = lcs(str1, str2)
    min_ = m - strings_lcs + n - strings_lcs
    return min_


s1 = 'heap'
s2 = 'pea'
print(num_of_del_and_ins(s1, s2))
