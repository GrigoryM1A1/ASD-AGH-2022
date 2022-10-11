def binary_search(L, l, r, x, act_ind):
    left = l
    right = r
    while left <= right:
        ind = (left + right) // 2
        if L[ind] + L[act_ind] > x:
            right = ind - 1
        elif L[ind] + L[act_ind] < x:
            left = ind + 1
        else:
            return ind
    return l


def find_i_j(A, x):
    i = 0
    n = len(A)
    while i < n:
        j = binary_search(A, i, n - 1, x, i)
        if A[i] + A[j] == x:
            print(i, j)
            return i, j
        i += 1
    print("Brak takich elementow")
    return False


T = [-5, -3, 0, 2, 3, 5, 6, 7]
# A[i] + A[j] = x
# A[i] = x - A[j]
# O(nlogn)
find_i_j(T, 15)
