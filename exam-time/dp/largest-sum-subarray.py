"""
Write an efficient program to find the sum of the contiguous subarray within
a one-dimensional array of numbers that has the largest sum.
"""


def max_sub_arr_cont_sum(A):
    n = len(A)
    max_so_far = -float('inf')
    max_end = 0
    start = 0
    end = 0
    s = 0

    for i in range(n):
        max_end += A[i]
        if max_so_far < max_end:
            max_so_far = max_end
            start = s
            end = i
        if max_end < 0:
            max_end = 0
            s = i + 1
    print(A[start:end + 1])
    return max_so_far


print(max_sub_arr_cont_sum([-2, -3, 4, -1, -2, 1, 5, -3]))
