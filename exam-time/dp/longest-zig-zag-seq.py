"""
The longest Zig-Zag subsequence problem is to find length of the longest subsequence of given sequence such that
all elements of this are alternating.
If a sequence {x1, x2, .. xn} is alternating sequence then its element satisfy one of the following relation :
  x1 < x2 > x3 < x4 > x5 < …. xn or
  x1 > x2 < x3 > x4 < x5 > …. xn
"""

'''
dp(i, j) = dl najdluzszego zyk zaka do elementu i typu j (j=0 xi < xi+1; j=1 xi > xi+1)
dp(0, 0) = 1
dp(0, 1) = 1

dp(i, 0) = max( dp(i, 0), dp(k, 1) ) k < i and A[k] < A[i]
dp(i, 1) = max( dp(i, 1), dp(k, 0) ) k < i and A[k] > A[i]
'''


def zig_zag(A):
    n = len(A)
    dp = [[1 for _ in range(2)] for _ in range(n)]

    for i in range(n):
        for k in range(i):
            if A[k] < A[i]:
                dp[i][0] = max(dp[i][0], dp[k][1] + 1)

            if A[k] > A[i]:
                dp[i][1] = max(dp[i][1], dp[k][0] + 1)

    return max(dp[n - 1][0], dp[n - 1][1])


print(zig_zag([10, 22, 9, 33, 49, 50, 31, 60]))
print(zig_zag([60, 31, 50, 49, 33, 9, 22, 10]))
