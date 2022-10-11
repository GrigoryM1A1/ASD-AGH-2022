"""
Dany jest zbior przedzialow.
Chcemy znalezc k przedzialow trzymanych w tablicy A, ktorych czesc wspolna jest jak najdluzszym przedzialem.
1 <= k <= len(A)
Funkcja zwraca liste numerow przedzialow.

Przyklad
A = [(0, 4), (1, 10), (6, 7), (2, 8)]
dla k = 3 wynikiem powinno byc [0, 1, 3] (lub dowolna permutacja listy)
co daje przedzialy o przecieciu [2, 4] o dlugosci 4 - 2 = 2


dp(i, j) = maksymalne przecięcie j wybranych przedziałów spośród i pierwszych przedziałów
dp(0, 0) = 0
dp(0, j) = 0
dp(i, 0) = 0
dp(i, j) = 0 if j > i
dp(i, i) = przecięcie przedziałów A[0] i A[1] i ... i A[i-1]
dp(i, 1) = max( dl(A[i - 1], dp(i - 1, 1) )
dp(i, j) = max( dp(i - 1, j), przecięcie dp(i - 1, j - 1) i A[i - 1] )
wynik: dp(n, k)

Złożoność O(n*k)
I choooooooooy nie dziala
"""
from kintersect_testy import runtests


def intersect(A, B):
    # print(A, B)
    dl1, a, b = A
    x, y = B

    if a == b == -2:
        return [y - x, x, y]

    if a == b == -1:
        return [0, -1, -1]

    if y < a or b < x:
        return [0, -1, -1]

    new_start = max(a, x)
    new_end = min(b, y)
    return [new_end - new_start, new_start, new_end]


def kintersect(A, k):
    n = len(A)
    # dp[i][j] = [dlugosc, start, end]
    dp = [[[0, -2, -2] for _ in range(k + 1)] for _ in range(n + 1)]

    # S[i][j] = [ith taken, parent_i, parent_j]
    S = [[[-2, -2, -2] for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, k + 1):
        dp[i][i] = intersect(dp[i - 1][i - 1], A[i - 1])
        S[i][i] = [1, i - 1, i - 1]

    for i in range(2, n + 1):
        dp[i][1] = [A[i - 1][1] - A[i - 1][0], A[i - 1][0], A[i - 1][1]]
        S[i][1] = [1, -1, -1]

        if dp[i - 1][1][0] > A[i - 1][1] - A[i - 1][0]:
            dp[i][1] = dp[i - 1][1]
            S[i][1] = [0, i - 1, 1]

    for i in range(3, n + 1):
        for j in range(2, min(i, k + 1)):
            q, a, b = dp[i - 1][j]
            S[i][j] = [0, i - 1, j]

            overlap, start, end = intersect(dp[i - 1][j - 1], A[i - 1])
            if overlap > q:
                q = overlap
                a = start
                b = end
                S[i][j] = [1, i - 1, j - 1]

            dp[i][j] = [q, a, b]

    res = []
    curr = S[n][k]
    i = n - 1
    while i >= 0:
        if curr[0] == 1:
            res.append(i)
            curr = S[curr[1]][curr[2]]
            i -= 1
        else:
            curr = S[curr[1]][curr[2]]
            i -= 1

    print('res', dp[n][k][0], 'len(res)', len(res))
    res.sort()
    return res


# k1 = 3
# A1 = [(0, 4), (1, 10), (6, 7), (2, 8)]
# print(kintersect(A1, k1))
runtests(kintersect)
