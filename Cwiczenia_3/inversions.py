from sys import maxsize as inf


def inversions(A):
    def merge(L, p, q, r):
        n1 = q - p
        n2 = r - q
        left = [0] * (n1 + 1)
        right = [0] * (n2 + 1)

        for i in range(n1):
            left[i] = A[i + p]
        for i in range(n2):
            right[i] = A[i + q]
        left[n1] = inf
        right[n2] = inf

        i = j = 0
        invers_num = 0
        for k in range(p, r):
            if left[i] <= right[j]:
                i += 1
            else:
                j += 1


T = []
