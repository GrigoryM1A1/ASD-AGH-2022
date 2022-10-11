"""
Given a set of numbers, find the Length of the Longest Arithmetic Progression (LLAP) in it.
Works on sorted arrays.
"""


def find_3_arithmetic_elements(A):
    n = len(A)

    for j in range(n):
        i = j - 1
        k = j + 1
        while i > -1 and k < n:
            if A[i] + A[k] == 2 * A[j]:
                return True
            elif A[i] + A[k] < 2 * A[j]:
                i -= 1
            else:
                k += 1
    return False


# dp(i, j) = dlugosc llap, w ktorym A[i] - pierwszy elem, A[j] - drugi wyraz, i < j
# dp(0, n - 1) = 2
# j - fixed, szukamy takich i,k, że wyrazy i,j,k tworzą ciąg arytmetyczny i < j < k
def llap(A):
    n = len(A)
    if n <= 2:
        return n

    dp = [[0 for _ in range(n)] for _ in range(n)]
    longest_progression = 0
    for i in range(n):
        dp[i][n - 1] = 2

    # Consider every element as second
    # element of AP
    for j in range(n - 2, 0, -1):
        i = j - 1
        k = j + 1
        while i > -1 and k < n:
            if A[i] + A[k] < 2 * A[j]:
                k += 1
            elif A[i] + A[k] > 2 * A[j]:
                i -= 1
            else:
                dp[i][j] = dp[j][k] + 1
                longest_progression = max(longest_progression, dp[i][j])
                i -= 1
                k += 1
                # If the loop was stopped due to k
                # becoming more than n-1, set the
                # remaining entities in column j as 2
                while i >= 0:
                    dp[i][j] = 2
                    i -= 1

    return longest_progression


print(llap([1, 7, 10, 15, 27, 29]))
print(llap([5, 10, 15, 20, 25, 30]))
