def bin_rightmost_search(A, elem):
    n = len(A)
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > elem:
            right = mid
        else:
            left = mid + 1

    return right - 1


def bin_left_most_search(A, elem):
    n = len(A)
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] < elem:
            left = mid + 1
        else:
            right = mid
    return left


Tab = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
print(bin_rightmost_search(Tab, 4))
print(bin_left_most_search(Tab, 4))
