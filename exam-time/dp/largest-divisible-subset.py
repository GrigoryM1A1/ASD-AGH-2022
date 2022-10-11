"""
Given an array of n distinct elements, find length of the largest subset such that every pair
in the subset is such that the larger element of the pair is divisible by smaller element.
"""


# f(i) = najwiekszy podciag z zadania, gdzie a[i] to najmniejszy element
def divisible_pairs(A):
    n = len(A)
    A.sort()

    dp = [0 for _ in range(n)]
    dp[n-1] = 1

    for i in range(n-2, -1, -1):
        max_len = 0
        for j in range(i+1, n):
            if A[j] % A[i] == 0 or A[i] % A[j] == 0:
                max_len = max(max_len, dp[j])
        dp[i] = max_len + 1
    return max(dp)


print(divisible_pairs([10, 5, 3, 15, 20]))
