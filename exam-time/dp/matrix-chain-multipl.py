"""
C(i, j) = minimalny koszt wymnożenia macierzy od indeksu i do indeksu j
C(i, j) = min{ C(i, k) + C(k+1, j) + d(i-1) * d(k) * d(j) | i <= k < j}
C(i, i) = 0
wynik: C(0, n-1)
"""


def solution(S, n):
    def rek(i):
        nonlocal S, Res
        pass

    Res = []


def matrix_chain_multiplication(M):
    n = len(M)
    inf = float('inf')
    # Tablica kosztow
    C = [[inf for j in range(n + 1)] for i in range(n + 1)]
    # Tablica do rozwiazania
    S = [[None for j in range(n + 1)] for i in range(n + 1)]
    # Tablica wymiarow
    D = [M[0][0], M[0][1]]
    for i in range(1, n):
        D.append(M[i][1])

    # Tablica rozmiaru n ale indeksujemy tak macierze od 1 do n
    for i in range(n + 1):
        C[i][0] = 0
        C[0][i] = 0
        C[i][i] = 0

    def rec(i, j):
        nonlocal S, C, D, inf
        if C[i][j] != inf:
            return C[i][j]

        min_ = inf
        for k in range(i, j):
            q = rec(i, k) + rec(k + 1, j) + D[i - 1] * D[k] * D[j]
            if q < min_:
                min_ = q
                S[i][j] = k
        C[i][j] = min_
        return C[i][j]

    rec(1, n)
    print(C[1][n])
    return C[1][n]


A = [(2, 3), (3, 4), (4, 2)]  # min_cost = 36
B = [(3, 2), (2, 4), (4, 2), (2, 5)]  # min_cost = 58
C = [(5, 4), (4, 6), (6, 2), (2, 7)]
# print(matrix_chain_multiplication(A))
# print('\n')
# print(matrix_chain_multiplication(B))
# print('\n')
print(matrix_chain_multiplication(C))
