"""
Given a set of non-negative integers, and a value sum,
determine if there is a subset of the given set with sum equal to given sum.
"""


# albo bierzemy albo nie
# f(i, k) = f(i-1, k - A[i]) or f(i-1, k)
# f(i, k) = czy istnieje suma rowna k korzystajac z elementow 0 ... 1
def subset_sum(A, s):
    n = len(A)
    dp = [[False for _ in range(s+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True

    for i in range(n):
        for k in range(s+1):
            if k - A[i] >= 0:
                dp[i][k] = dp[i-1][k-A[i]] or dp[i-1][k]
            else:
                dp[i][k] = dp[i-1][k]

    for row in dp:
        print(row)
    return dp[n-1][s]


# print(subset_sum([3, 34, 4, 12, 5, 2], 9))
# print(subset_sum([3, 34, 4, 12, 5, 2], 30))
print(subset_sum([1, 6, 11, 5], 23))
