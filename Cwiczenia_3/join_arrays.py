'''
Mamy k posortowanych tablic o łącznej długości n. Trzeba je złączyć w jedną posortowaną.
'''


# O(nk)
def merge_arrays_nk(A):
    def merge(Left, Right):
        m = len(Left) + len(Right)
        Merged = [0] * m
        i = 0
        j = 0
        for v in range(m):
            if i < len(Left) and (j >= len(Right) or Left[i] <= Right[j]):
                Merged[v] = Left[i]
                i += 1
            else:
                Merged[v] = Right[j]
                j += 1
        return Merged

    n = 0
    for i in A:
        n += len(i)
    k = len(A)
    R = merge(A[0], A[1])
    for i in range(2, k):
        R = merge(R, A[i])
    print(R)
    return R


def merge_arrays(T):
    def merge(Left, Right):
        m = len(Left) + len(Right)
        Merged = [0] * m
        i = 0
        j = 0
        for v in range(m):
            if i < len(Left) and (j >= len(Right) or Left[i] <= Right[j]):
                Merged[v] = Left[i]
                i += 1
            else:
                Merged[v] = Right[j]
                j += 1
        return Merged

    while len(T) > 1:
        new_ = []
        for i in range(0, len(T), 2):
            if i + 1 < len(T):
                merged = merge(T[i], T[i + 1])
            else:
                merged = T[i]
            new_.append(merged)
        T = new_
    return T



T = [[3, 4, 5],
     [1, 2, 12, 13],
     [3, 4, 5, 6, 7],
     [10, 11, 15, 17],
     [2, 7, 9]]
print(merge_arrays(T))
