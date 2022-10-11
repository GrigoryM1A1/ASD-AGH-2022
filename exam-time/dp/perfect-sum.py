"""
Given an array of integers and a sum, the task is to print all subsets of the given
array with a sum equal to a given sum.
"""


def print_subsets(A, s, dp, p, i):
    # jestesmy na koncu i bierzemy aktualny element
    if i == 0 and s != 0 and dp[0][s]:
        p.append(A[i])
        print(p)
        p = []
        return

    # suma wynosi 0
    if i == 0 and s == 0:
        print(p)
        p = []
        return

    # ignorujemy aktualny element
    if dp[i-1][s]:
        b = []
        b.extend(p)
        print_subsets(A, s, dp, b, i-1)

    # beirzemy aktualny element
    if s >= A[i] and dp[i-1][s - A[i]]:
        p.append(A[i])
        print_subsets(A, s-A[i], dp, p, i-1)


def perfect_sum(A, s):
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

    if not dp[n-1][s]:
        print('No subset')
        return None

    subsets = []
    print_subsets(A, s, dp, subsets, n-1)


perfect_sum([1, 3, 2, 5, 4], 10)


