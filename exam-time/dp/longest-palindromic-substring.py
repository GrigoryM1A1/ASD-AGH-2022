"""
Given a string, find the longest substring which is palindrome.
"""


# chooooooy
# def longest_palindromic_substring(S):
#     n = len(S)
#     dp = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         dp[i][i] = 1
#     for i in range(n - 1):
#         dp[i][i + 1] = 2 if S[i] == S[i + 1] else 1
#
#     for j in range(2, n):
#         for i in range(n - j):
#             ind = i + j
#             if S[i] == S[ind]:
#                 dp[i][ind] = dp[i][ind - 1] + dp[i + 1][ind]
#             else:
#                 dp[i][ind] = max(dp[i][ind - 1], dp[i + 1][ind])
#
#     for row in dp:
#         print(row)
#
#     return dp[0][n - 1]
#
#
# print(longest_palindromic_substring("forgeeksskeegfor"))


# trzymamy se w tablicy True albo False w zaleznosci czy wyraz i ... j jest palindromem
# dp[i][j] = is_palindrome from i to j
# dp[i][j] = True if dp[i+1][j-1] == True and S[i] == S[j] else False
def longest_palindromic_substring(S):
    n = len(S)
    dp = [[False for _ in range(n)] for _ in range(n)]

    max_len = 1
    start = 0
    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if S[i] == S[i + 1]:
            dp[i][i + 1] = True
            max_len = 2
            start = i

    k = 3
    while k < n:
        i = 0
        while i < n - k + 1:
            j = i + k - 1

            if dp[i + 1][j - 1] and S[i] == S[j]:
                dp[i][j] = True

                if k > max_len:
                    start = i
                    max_len = k
            i += 1
        k += 1
    return max_len


print(longest_palindromic_substring("forgeeksskeegfor"))
