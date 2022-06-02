def count(S, n):
    m = len(S)
    F = [[0 for i in range(m)] for j in range(n+1)]

    for i in range(m):
        F[0][i] = 1

    for i in range(1, n+1):
        for j in range(m):
            # liczba rozwiazan jezeli bierzemy banknot S[j]
            if i - S[j] >= 0:
                x = F[i-S[j]][j]
            else:
                x = 0
            # liczba rozwiazane jezeli nie bierzemy banknotu S[j]
            if j >= 1:
                y = F[i][j-1]
            else:
                y = 0
            F[i][j] = x + y
    return F[n][m-1]


arr = [1, 2, 3]
print(count(arr, 4))
