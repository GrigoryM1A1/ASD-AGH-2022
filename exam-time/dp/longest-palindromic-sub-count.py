"""
Find how many palindromic subsequences
(need not necessarily be distinct) can be formed in a given string. Note that the empty
string is not considered as a palindrome.
"""


'''
dp(i, j) = liczba istionie roznych palindormowych podlancuchow slowa zaczynajacego sie w "i" i konczacego w "j"
dp(i, i) = 1, bo kazdy pojedynczy znak to palindrom
dp(i, j) = dp(i, j - 1) + dp(i + 1, j) + 1 if S[i] == S[j] else dp(i, j - 1) + dp(i + 1, j) - dp(i + 1, j - 1)
'''


def dyn(S, dp, i, j):
    if j < i:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if S[i] == S[j]:
        dp[i][j] = dyn(S, dp, i, j - 1) + dyn(S, dp, i + 1, j) + 1
        return dp[i][j]

    dp[i][j] = dyn(S, dp, i + 1, j) + dyn(S, dp, i, j - 1) - dyn(S, dp, i + 1, j - 1)
    return dp[i][j]


def count_palindromic_sub(S):
    n = len(S)
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
    dyn(S, dp, 0, n - 1)
    return dp[0][n - 1]


strings = ["abcd", "aab", "aaaa"]
for word in strings:
    print(word, count_palindromic_sub(word))
