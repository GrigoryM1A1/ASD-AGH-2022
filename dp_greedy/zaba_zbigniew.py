'''
f(i, y) = minimalna liczba skoków potrzebna by dotrzeć do pola i posiadając w zapasie dokładnie y energii
f(0, {0-k}) = 0
f(i, j) = 1 + min(f(i-k, j+k))
'''


def it_is_wednesday_my_dudes(A):
    n = len(A)
    m = sum(A)
    m = max(m, m - n)
    inf = float('inf')
    F = [[inf for i in range(m)] for j in range(n)]
    F[0][A[0]] = 0

    for i in range(1, n):
        for j in range(m):
            for k in range(i):
                if m - (i - k) > j - A[i] >= 0:
                    F[i][j] = min(F[i][j], F[k][j + (i - k) - A[i]] + 1)

    min_ = inf
    for i in range(m):
        if F[n-1][i] < min_:
            min_ = F[n-1][i]
    if min_ == inf:
        return -1

    return min_


test = [1, 1, 1, 1, 1]
T = [2, 0, 3, 0, 0, 0]
B = [1, 0, 2, 3, 4, 1]
P = [2, 4, 3, 1]
print(it_is_wednesday_my_dudes(B))
