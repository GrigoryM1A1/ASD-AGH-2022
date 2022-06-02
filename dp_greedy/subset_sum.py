'''
Znalezc takie elementy, aby sumowaly sie do s
f(i, j) = czy istnieje pozdzbior elementow od 0 do i-1 taki, że sumuje się do j
f(i, j) = bierzemy albo nie bierzemy elementu
f(i, j) = f(i-1, j - L[i-1]) or f(i-1, j)

'''


def subset_sum(A, s):
    n = len(A)
    F = [[None for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        F[i][0] = True

    for i in range(1, n+1):
        for j in range(s + 1):
            if j < A[i-1]:  # element ktory bierzemy jest za duzy
                F[i][j] = F[i-1][j]
            else:
                F[i][j] = F[i-1][j - A[i-1]] or F[i-1][j]
    for row in F:
        print(row)


L = [3, 34, 4, 12, 5, 2]
S = 10
subset_sum(L, S)
