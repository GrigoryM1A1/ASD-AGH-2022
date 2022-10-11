"""
We have to paint n boards of length {A1, A2…An}. There are k painters available and each takes 1 unit time
to paint 1 unit of board. The problem is to find the minimum time to get
this job done under the constraints that any painter will only paint continuous sections of boards, say board {2, 3, 4}
or only board {1} or nothing but not board {2, 4, 5}.

Examples:

Input : k = 2, A = {10, 10, 10, 10}
Output : 20.
Here we can divide the boards into 2
equal sized partitions, so each painter
gets 20 units of board and the total
time taken is 20.

Input : k = 2, A = {10, 20, 30, 40}
Output : 60.
Here we can divide first 3 boards for
one painter and the last board for
second painter.
"""


def efficient_painters(A, k):
    n = len(A)
    prefix_sum = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    # base cases
    for i in range(1, n + 1):
        dp[i][1] = prefix_sum[i] - prefix_sum[0]

    for j in range(1, k + 1):
        dp[1][j] = A[0]

    for i in range(2, n + 1):
        for j in range(2, k + 1):
            best = float('inf')
            for l in range(1, i + 1):
                best = min(best, max(dp[l][j - 1], prefix_sum[i] - prefix_sum[l]))
            dp[i][j] = best

    for row in dp:
        print(row)


efficient_painters([10, 20, 60, 50, 30, 40], 3)
