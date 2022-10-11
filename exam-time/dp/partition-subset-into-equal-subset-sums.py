"""
Given a set of integers, the task is to divide it into two sets S1 and S2
such that the absolute difference between their sums is minimum.
If there is a set S with n elements, then if we assume Subset1 has m elements,
Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.
"""


# albo bierzemy albo nie
# f(i, k) = f(i-1, k - A[i]) or f(i-1, k)
# f(i, k) = czy istnieje suma rowna k korzystajac z elementow 0 ... 1
# obliczmy subset sum dla n-1 sum(A)
# wszedzie gdzie mozemy stworzyc dana sume s, sprawdzamy roznice
def partition_equal_sum(A):
    n = len(A)
    S = sum(A)
    dp = [[False for _ in range(S + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True

    for i in range(n):
        for s in range(S + 1):
            if s - A[i] >= 0:
                dp[i][s] = dp[i - 1][s - A[i]] or dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]

    min_diff = float('inf')
    for s in range(S + 1):
        if dp[n - 1][s]:
            set1 = s
            set2 = S - s
            min_diff = min(min_diff, abs(set1 - set2))

    return min_diff


print(partition_equal_sum([1, 6, 11, 5]))
