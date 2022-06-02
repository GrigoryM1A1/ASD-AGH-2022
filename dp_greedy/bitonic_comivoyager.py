def bitonic_comivoyager(C, Dist):
    def tspf(i, j, F, D):
        nonlocal inf
        if F[i][j] != inf:
            return F[i][j]

        if i == j - 1:
            best = inf
            for k in range(j-1):
                best = min(best, tspf(k, j-1, F, D) + D[k][j])
            F[j-1][j] = best
        else:
            F[i][j] = tspf(i, j-1, F, D) + D[j-1][j]
        return F[i][j]

    n = len(C)
    inf = float('inf')
    F = [[inf for j in range(n)] for i in range(n)]
    tspf(0, n-1, F, Dist)
    return F[0][n-1]
