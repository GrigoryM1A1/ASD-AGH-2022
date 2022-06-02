'''
1) f(i) = długość najdłuższego rosnącego podciągu w tablicy A[0, ..., i] kończący się na i
2) f(i) = max{ f(j) + 1 | j < i and A[j] < A[i] }
   max{ None } = 1
   f(0) = 1
   wynik: max{ f(i) }, i c {0, 1, ... , n-1}
'''


def lis(A):
    n = len(A)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    max_ = 0

    for i in range(n):
        for j in range(i):
            if A[i] > A[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
        if F[i] > max_:
            max_ = i

    return max_, F, P


def print_sol(A, P, i):
    if P[i] != -1:
        print_sol(A, P, P[i])
    print(A[i], end=" ")


L = [2, 1, 4, 3, 4, 8, 5, 7, 2, 0]
ind, Res, Par = lis(L)
print(Res[ind])
print_sol(L, Par, ind)

