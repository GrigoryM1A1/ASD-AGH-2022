'''
Zaczynamy w dowolnej kolumnie 0 weirsza i chcemy znalezc najwartosciowsza siezke do n-1 wiersza
'''


def max_path(A):
    def moves(i, j):
        nonlocal n
        pot_moves = [(i-1, j-1), (i-1, j), (i-1, j+1)]
        res = []
        for move in pot_moves:
            if 0 <= move[0] < n and 0 <= move[1] < n:
                res.append(move)
        return res

    n = len(A)
    F = [[-1 for i in range(n)] for j in range(n)]
    S = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        F[0][i] = A[0][i]

    for i in range(1, n):
        for j in range(n):
            ruchy = moves(i, j)
            best = -1
            r = None
            c = None
            for k in ruchy:
                # best = max(best, F[k[0]][k[1]] + A[i][j])
                q = F[k[0]][k[1]] + A[i][j]
                if q > best:
                    best = q
                    r = k[0]
                    c = k[1]
            F[i][j] = best
            S[i][j] = r, c

    r = c = None
    max_ = 0
    for i in range(n):
        if F[n-1][i] > max_:
            max_ = F[n-1][i]
            r = n-1
            c = i

    res = []
    while S[r][c] is not None:
        res.append((r, c))
        r, c = S[r][c]
    res.append((r, c))

    return max_, res


T = [[1, 2, 1, 3, 4],
     [1, 5, 1, 1, 1],
     [7, 1, 1, 1, 1],
     [1, 8, 1, 1, 1],
     [1, 1, 9, 1, 1]]
max_path(T)
