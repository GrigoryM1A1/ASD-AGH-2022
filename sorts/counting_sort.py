'''
Counting sort - O(n + k),
n - rozmiar danych
k - zakres liczba jakie mamy do posortowania
'''


def count_sort(A, k):
    n = len(A)
    C = [0] * k
    B = [0] * n

    for x in A:
        C[x] += 1

    for i in range(1, k):
        C[i] += C[i-1]

    for i in range(n - 1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    for i in range(n):
        A[i] = B[i]


T = [1, 2, 0, 1, 4, 3, 3, 4, 0]
print(T)
count_sort(A=T, k=5)
print(T)
