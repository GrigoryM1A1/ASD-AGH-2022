"""
There are ‘p’ balls of type P, ‘q’ balls of type Q and ‘r’ balls of type R.
Using the balls we want to create a straight line such that no two balls of same type are adjacent.

Input  : p = 1, q = 1, r = 0
Output : 2
There are only two arrangements PQ and QP

Input  : p = 1, q = 1, r = 1
Output : 6
There are only six arrangements PQR, QPR,
QRP, RQP, PRQ and RPQ

Input  : p = 2, q = 1, r = 1
Output : 6
There are only six arrangements PQRP, QPRP,
PRQP, RPQP, PRPQ and PQPR
"""


def count_ballz(p, q, r, last, dp):
    if p < 0 or q < 0 or r < 0:
        return 0

    if p == 1 and q == 0 and r == 0 and last == 'P':
        dp[p][q][r] = 1
        return dp[p][q][r]

    if p == 0 and q == 1 and r == 0 and last == 'Q':
        dp[p][q][r] = 1
        return dp[p][q][r]

    if p == 0 and q == 0 and r == 1 and last == 'R':
        dp[p][q][r] = 1
        return dp[p][q][r]

    if last == 'P':
        dp[p][q][r] = count_ballz(p - 1, q, r, 'Q', dp) + count_ballz(p - 1, q, r, 'R', dp)
        return dp[p][q][r]

    if last == 'Q':
        dp[p][q][r] = count_ballz(p, q - 1, r, 'P', dp) + count_ballz(p, q - 1, r, 'R', dp)
        return dp[p][q][r]

    if last == 'R':
        dp[p][q][r] = count_ballz(p, q, r - 1, 'P', dp) + count_ballz(p, q, r - 1, 'Q', dp)
        return dp[p][q][r]


def arranging_ballz(p, q, r):
    dp = [[[0 for _ in range(r + 1)] for _ in range(q + 1)] for _ in range(p + 1)]
    x = count_ballz(p, q, r, 'P', dp)
    y = count_ballz(p, q, r, 'Q', dp)
    z = count_ballz(p, q, r, 'R', dp)
    return x + y + z


print(arranging_ballz(2, 1, 1))
print(arranging_ballz(1, 1, 0))
print(arranging_ballz(1, 1, 1))
