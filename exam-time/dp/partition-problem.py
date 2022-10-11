"""
Partition problem is to determine whether a given set can be partitioned into two subsets such that
the sum of elements in both subsets is the same.
"""


def can_partition(A):
    elem_sum = sum(A)
    if elem_sum % 2 == 1:
        return False

    n = len(A)
    half_sum = elem_sum // 2
    # subset sum problem dla tablicy A i half_sum
    dp = [[False for _ in range(half_sum + 1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = True

    for i in range(n):
        for x in range(1, half_sum + 1):
            if x - A[i] >= 0:
                dp[i][x] = dp[i-1][x - A[i]] or dp[i-1][x]
            else:
                dp[i][x] = dp[i-1][x]

    return dp[n-1][half_sum]


print(can_partition([1, 5, 11, 5]))
