def ad_1(A, a, b):
    n = max(A, key=lambda x: x[1])[1] + 1
    F = [[None for _ in range(n)] for _ in range(n)]
    for x in A:
        F[x[0]][x[1]] = True

    def rek(i, j):
        nonlocal F
        if F[i][j] is not None:
            return F[i][j]
        for k in range(i + 1, j):
            if rek(i, k) and rek(k, j):
                F[i][j] = True
                return True
            else:
                F[i][j] = False
                return False

    print(rek(a, b))
    return F


def ad_2(A, a, b):
    n = max(A, key=lambda x: x[1])[1] + 1
    F = [[None for _ in range(n)] for _ in range(n)]
    for x in A:
        if F[x[0]][x[1]] is not None:
            F[x[0]][x[1]] = min(F[x[0]][x[1]], x[2])
        else:
            F[x[0]][x[1]] = x[2]

    def rek(i, j):
        nonlocal F
        if F[i][j] is not None:
            return F[i][j]
        cost = -1
        for k in range(i + 1, j):
            a = rek(i, k)
            b = rek(k, j)
            if a > 0 and b > 0:
                if cost > a + b or cost < 0:
                    cost = a + b
        F[i][j] = cost
        return cost

    res = rek(a, b)
    return F


def ad_3(A, k):
    return 0


def print_tab(A):
    for row in A:
        print(row)


A = [[2, 3, 2], [1, 5, 3], [3, 4, 5], [1, 2, 10], [1, 10, 1], [1, 3, 20], [3, 4, 1]]
print_tab(ad_2(A, 1, 4))
