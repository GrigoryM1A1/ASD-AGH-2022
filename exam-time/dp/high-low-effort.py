"""
You are given n days and for each day (di) you could either perform a high effort tasks (hi) or a low effort tasks (li)
or no task with the constraint that you can choose a high-effort tasks only if you choose no task on the previous day.
Write a program to find the maximum amount of tasks you can perform within these n days.
"""


# f(i) = maksymalny zysk ze zrobienia zadan w dni 0 ... i
# wynik = f(i-1)
# f(0) = max(Low[0], High[0])
# f(1) = max(High[1], Low[1] + High[0], Low[1] + Low[0])
# f(i) = max(High[i] + f(i-2), Low[i] + f(i-1))
def max_tasks(High, Low):
    n = len(High)
    F = [-1 for _ in range(n)]
    F[0] = max(Low[0], High[0])
    F[1] = max(High[1], High[0] + Low[1], Low[0] + Low[1])

    for i in range(2, n):
        F[i] = max(High[i] + F[i - 2], Low[i] + F[i - 1])
    return F[n - 1]


print(max_tasks([3, 6, 8, 7, 6], [1, 5, 4, 5, 3]))

