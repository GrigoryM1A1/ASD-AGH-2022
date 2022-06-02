def park(A, D):
    # F[i][D][D]
    n = len(A)
    F = [[[None for _ in range(D + 1)] for _ in range(D + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        F[i][0][0] = False
    for i in range(D + 1):
        for j in range(D + 1):
            F[0][i][j] = True
    for i in range(1, n + 1):
        for L in range(D + 1):
            for R in range(D + 1):
                F[i][L][R] = (L >= A[i - 1] and F[i - 1][L - A[i - 1]][R]) or (
                            R >= A[i - 1] and F[i - 1][L][R - A[i - 1]])
    k = n
    while not F[k][D][D] and k >= 1:
        k -= 1
    if k != 0:
        return k
    else:
        return False


A = [1, 3, 3, 1, 1, 1, 2, 5, 6]
D = 5
print(park(A, D))
