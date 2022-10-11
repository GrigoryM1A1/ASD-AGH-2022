"""
Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B. C is said to be
interleaving A and B, if it contains all and only characters of A and B and order of all characters in individual
strings is preserved.
"""


"""
1. Create a DP array (matrix) of size M*N, where m is the size of the first string
   and n is the size of the second string. Initialize the matrix to false.
2. If the sum of sizes of smaller strings is not equal to the size of the larger string then return false
   and break the array as they cant be the interleaved to form the larger string.
3. Run a nested loop the outer loop from 0 to m and the inner loop from 0 to n. Loop counters are i and j.
4. If the values of i and j are both zeroes then mark dp[i][j] as true. If the value of i is zero and j is non zero
   and the j-1 character of B is equal to j-1 character of C the assign dp[i][j] as dp[i][j-1] and similarly if j is 0
   then match i-1 th character of C and A and if it matches then assign dp[i][j] as dp[i-1][j].
5. Take three characters x, y, z as (i-1)th character of A and (j-1)th character of B and (i + j – 1)th character of C.
6. if x matches with z and y does not match with z then assign dp[i][j] as dp[i-1][j] similarly if x is not equal to z
   and y is equal to z then assign dp[i][j] as dp[i][j-1]
7. if x is equal to y and y is equal to z then assign dp[i][j] as bitwise OR of dp[i][j-1] and dp[i-1][j].
8. return value of dp[m][n].
"""


def interleave(A, B, C):
    m = len(A)
    n = len(B)

    if m + n != len(C):
        return False

    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                dp[i][j] = True

            # A is empty
            elif i == 0:
                if B[j - 1] == C[j - 1]:
                    dp[i][j] = dp[i][j - 1]

            # B is empty
            elif j == 0:
                if A[i - 1] == C[i - 1]:
                    dp[i][j] = dp[i - 1][j]

            # Current character of C matches with
            # current character of A, but doesn't match
            # with current character of B
            elif A[i - 1] == C[i + j - 1] and B[j - 1] != C[i + j - 1]:
                dp[i][j] = dp[i - 1][j]

            # Current character of C matches with
            # current character of B, but doesn't match
            # with current character of A
            elif A[i - 1] != C[i + j - 1] and B[j - 1] == C[i + j - 1]:
                dp[i][j] = dp[i][j - 1]

            # Current character of C matches with
            # that of both A and B
            elif A[i - 1] == C[i + j - 1] and B[j - 1] == C[i + j - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[m][n]


print(interleave('XXY', 'XXZ', 'XXXXZY'))
print(interleave('YX', 'X', 'XXY'))
