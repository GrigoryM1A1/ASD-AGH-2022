"""
Longest increasing subsequence

f(i) = dl najdluzszego rosnacego podciagu w tablicy A[0 ... i] konczacy sie na A[i]
f(i) = max{ f(j) + 1 | j < i and A[j] < A[i] }
f(0) = 1

"""


def print_sol(A, P, i, res):
    if P[i] != -1:
        print_sol(A, P, P[i], res)
    res.append(A[i])


def lis(A):
    n = len(A)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    max_ = 0
    max_ind = 0
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
        if F[i] > max_:
            max_ind = i
            max_ = F[i]

    res = []
    print_sol(A, P, max_ind, res)
    print(res)
    print("Wynik:")
    return max_


print(lis([3, 10, 2, 1, 20]))
