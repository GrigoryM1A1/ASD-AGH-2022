def select(T, k):
    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1

    def quick_select(A, pos, p, r):
        if p == r:
            return A[p]

        if p < r:
            q = partition(A, p, r)
            if q == pos:
                return A[q]
            elif q < k:
                return quick_select(A, pos, q + 1, r)
            else:
                return quick_select(A, pos, p, q - 1)

    z = quick_select(T, k, 0, len(T) - 1)
    return z


T1 = [85, 58, 31, 28, 47, 98, 9, 35, 8, 30, 36, 41, 10, 61, 6, 81, 53, 76, 67, 58, 81, 84, 3, 88, 27]
z = select(T1, 4)
print(z)
