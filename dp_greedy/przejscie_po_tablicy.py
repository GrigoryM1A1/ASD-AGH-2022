def path(A):
    def moves(i, j):
        nonlocal n, m
        r = [(i, j-1), (i-1, j)]
        go_to = []
        for x in r:
            if 0 <= x[0] < m and 0 <= x[1] < n:
                go_to.append(x)
        return go_to

    def rec(i, j):
        nonlocal m, n, inf, F

        if F[i][j] is not None:
            return F[i][j]

        M = moves(i, j)
        best = inf
        for x in M:
            q = rec(x[0], x[1]) + A[i][j]
            if q < best:
                best = q
        F[i][j] = best
        return F[i][j]

    m = len(A)
    n = len(A[0])
    inf = float('inf')
    F = [[None for i in range(n)] for j in range(m)]
    F[0][0] = A[0][0]
    for i in range(1, n):
        F[0][i] = F[0][i-1] + A[0][i]
    for i in range(1, m):
        F[i][0] = F[i-1][0] + A[i][0]

    F[m-1][n-1] = rec(m-1, n-1)
    print(F[m-1][n-1])
    return F[m-1][n-1]


T = [
        [1, 4, 5],
        [1, 3, 6],
        [8, 1, 1],
        [4, 5, 4],
    ]

path(T)
