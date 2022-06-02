'''
Something's fucky
'''
from sys import maxsize as inf


def minimax(A, k):
    def rek(i, t):
        if F[i][t] is not None:
            return F[i][t]

        max_ = -inf
        for o in range(t, i):
            max_ = max(max_, min(rek(o, t-1), find_sum(o+1, i)))
        F[i][t] = max_
        return F[i][t]

    def find_sum(i, j):
        # indeksujemy jakby od 1
        nonlocal prefix_sum
        if i == 1:
            return prefix_sum[j-1]
        else:
            return prefix_sum[j-1] - prefix_sum[i-2]

    n = len(A)
    F = [[None for _ in range(k+1)] for _ in range(n+1)]
    prefix_sum = [A[i] for i in range(n)]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]

    for i in range(1, k+1):
        F[i][i] = min(A[:i])
    for i in range(1, n+1):
        F[i][1] = find_sum(1, i)
    for i in range(n+1):
        F[i][0] = inf
    for i in range(k+1):
        F[0][i] = inf

    F[n][k] = rek(n, k)
    print(F[n][k])
    return F[n][k]


A = [5, 6, 1, 3, 12, 1, 6, 5, 8, 2, 7]
k = 3
minimax(A, k)
