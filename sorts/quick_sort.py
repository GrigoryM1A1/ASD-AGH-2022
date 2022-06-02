# Quick_sort z wykladu z ifem i dwoma wywoalniami
def quick_sort_wyklad_ASD(T):
    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def quicksort(A, p, r):
        if p < r:
            q = partition(A, p, r)
            quicksort(A, p, q - 1)
            quicksort(A, q + 1, r)

    quicksort(T, 0, len(T) - 1)


# Quick_sort z wykladu z wilem z jednym wywolaniem
def quick_sort_wyklad_ASD_mod(T):
    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def quicksort(A, p, r):
        while p < r:
            q = partition(A, p, r)
            quicksort(A, p, q - 1)
            p = q + 1

    quicksort(T, 0, len(T) - 1)


# Quick_sort ze strony mattomatti
def quick_sort_by_mattomatti(T):
    def qsort(A, p, r):
        i = p
        j = r
        x = A[(p + r) // 2]
        while i <= j:
            while A[i] < x:
                i += 1
            while A[j] > x:
                j -= 1
            if i <= j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        if p < j:
            qsort(A, p, j)
        if i < r:
            qsort(A, i, r)

    qsort(T, 0, len(T) - 1)


# Quick_sort z uzyciem maksymalnie logn pamieci
def quick_sort_space_nlogn(T):
    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[j], A[i] = A[i], A[j]
        A[i + 1], A[r] = A[r], A[i + 1]
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

    qsort(T, 0, len(T) - 1)


# Quick_sort bez rekurencji z uzyciem stosu
def quick_sort_iter(T):
    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def quicksort(A, p, r):
        S = []
        S.append((p, r))
        while len(S) != 0:
            p, r = S.pop()
            if p < r:
                x = partition(T, p, r)
                S.append((p, x - 1))
                S.append((x + 1, r))

    quicksort(T, 0, len(T) - 1)


# Quick_sort bez rekurencji z uzyciem makysmalnie logn pamieci
def quick_sort_iter_space_logn(T):
    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def quicksort(A, p, r):
        S = []
        S.append((p, r))
        while len(S) != 0:
            p, r = S.pop()
            if p < r:
                x = partition(A, p, r)
                if x - p < r - x:
                    S.append((x + 1, r))
                    S.append((p, x - 1))
                else:
                    S.append((p, x - 1))
                    S.append((x + 1, r))

    quicksort(T, 0, len(T) - 1)


T1 = [85, 58, 31, 28, 47, 98, 9, 35, 8, 30, 36, 41, 10, 61, 6, 81, 53, 76, 67, 58, 81, 84, 3, 88, 27]
quick_sort_space_nlogn(T1)
# print(T1)
# quick_sort_by_mattomatti(T1)
# print(T1)
# quick_sort_wyklad_ASD_mod(T1)
# print(T1)
# quick_sort_iter(T1)
# print(T1)
#quick_sort_iter_space_logn(T1)
print(T1)
