"""
Given a fence with n posts and k colors, find out the number of ways of painting the fence such that
at most 2 adjacent posts have the same color.
"""


def paint(n, k):
    f = [0 for _ in range(n+1)]
    f[1] = k
    f[2] = k * k

    if n <= 2:
        return f[n]

    for i in range(3, n+1):
        # f[i] = mozliwe kolory bez poprzedniego koloru slupka * (malujemy 1 slupek tym kolorem + malujemy 2 slupki)
        f[i] = (k - 1) * (f[i-1] + f[i-2])
    return f[n]


print(paint(2, 4))
