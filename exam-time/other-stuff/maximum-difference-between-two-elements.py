"""
Given an array arr[] of integers,
find out the maximum difference between any two elements such that larger element appears after the smaller number.
"""


def max_diff(A):
    # w tej samej petli szukamy minimum i minimalnej roznicy
    n = len(A)
    min_ = A[0]
    diff = A[1] - A[0] if A[1] >= A[0] else -1

    for i in range(1, n):
        if A[i] >= min_:
            curr_diff = A[i] - min_
            if curr_diff >= diff:
                diff = curr_diff
        else:
            min_ = A[i]

    return diff


print(max_diff([100, 2, 6, 80, 1]))
