'''
Tablica m-elementowa i tablica n-elementowa, m << n
Algortym, ktory sprawdzi czy zbiory sa rozlaczne
'''
from random import randint


def bin_search(T, elem):
    left = 0
    right = len(T) - 1
    while left <= right:
        mid = (left + right) // 2
        if elem > T[mid]:
            left = mid + 1
        elif elem < T[mid]:
            right = mid - 1
        else:
            return True
    return False


def quick_sort(T):
    def partition(A, p, r):
        piv = randint(p, r)
        A[piv], A[r] = A[r], A[piv]
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        T[i + 1], T[r] = A[r], A[i + 1]
        return i + 1

    def qsort(A, p, r):
        while p < r:
            q = partition(A, p, r)
            if q - p < r - q:
                qsort(A, p, q - 1)
                p = q + 1
            else:
                qsort(A, q + 1, r)
                r = q - 1


def is_disjunctive(M, N):
    m = len(M)
    n = len(N)
    quick_sort(M)

    disjunctive = False
    for i in range(n):
        disjunctive = bin_search(M, N[i])
        if disjunctive:
            print("False")
            return False

    print("True")
    return True


tab_m = [7, 2, 3, 11, 4]
tab_n = [12, 10, 1, 0, 30, 21, 15, 8, 9, 14, 69, 22, 37, 420, 5]
is_disjunctive(tab_m, tab_n)
