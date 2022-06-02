from sys import maxsize as inf


def mergeSort(T):
    def merge(tab, p, q, r):
        n_1 = q - p
        n_2 = r - q
        left = [0] * (n_1 + 1)
        right = [0] * (n_2 + 1)

        for i in range(n_1):
            left[i] = tab[p + i]
        for i in range(n_2):
            right[i] = tab[q + i]

        left[n_1] = inf
        right[n_2] = inf

        i = 0
        j = 0
        for k in range(p, r):
            if left[i] <= right[j]:
                tab[k] = left[i]
                i += 1
            else:
                tab[k] = right[j]
                j += 1

    def merge_sort(tab, p, r):
        if p < r - 1:
            q = (p + r) // 2
            merge_sort(tab, p, q)
            merge_sort(tab, q, r)
            print("A[p:q]: ", tab[p:q])
            print("A[q:r]: ", tab[q:r])
            merge(tab, p, q, r)

    p = 0
    n = len(T)
    merge_sort(T, p, n)


T = [3, 4, 2, 1, 7, 5, 3, 2, 2, 11, 10, 6, 9]
mergeSort(T)
print(T)
