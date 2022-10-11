"""
Given n friends, each one can remain single or can be paired up with some other friend.
Each friend can be paired only once.
Find out the total number of ways in which friends can remain single or can be paired up.


f(i) = f(i-1) + f(i-1) * f(i-2) - albo dana osoba zostaje sama albo wybieramy jej pare sposrod pozostalych
f(0) = 0
f(1) = 1
"""


def u_my_fren_now(n):
    if n <= 2:
        return n

    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(n+1):
        dp[i] = dp[i-1] + dp[i-1] * dp[i-2]

    return dp[n]

