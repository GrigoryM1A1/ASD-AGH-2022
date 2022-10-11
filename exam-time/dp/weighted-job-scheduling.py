"""
Given N jobs where every job is represented by following three elements of it.
    1.Start Time
    2.Finish Time
    3.Profit or Value Associated (>= 0)
Find the maximum profit subset of jobs such that no two jobs in the subset overlap.


Input: Number of Jobs n = 4
       Job Details {Start Time, Finish Time, Profit}
       Job 1:  {1, 2, 50}
       Job 2:  {3, 5, 20}
       Job 3:  {6, 19, 100}
       Job 4:  {2, 100, 200}
Output: The maximum profit is 250.
We can get the maximum profit by scheduling jobs 1 and 4.
Note that there is longer schedules possible Jobs 1, 2 and 3
but the profit with this schedule is 20+50+100 which is less than 250.
"""


# chyba ok, inaczej niz na geeksach
# dp(i) = maksymalny profit z wykonanych zadan spodrod 0 ... i zadan (posortowane po finish time)
# dp(0) = profit pierwszego w kolejnosci zadania
# dp(i) = max{ dp(i-1), dp(k) + task_profit[i] } 0 <= k < i and task i and k don't overlap
def max_profit(Schedule):
    n = len(Schedule)
    Schedule.sort(key=lambda Task: Task[1])

    dp = [-1 for _ in range(n)]
    dp[0] = Schedule[0][2]

    for i in range(1, n):
        q = dp[i - 1]
        for k in range(i):
            if not Schedule[i][0] < Schedule[k][1] < Schedule[i][1]:
                q = max(q, dp[k] + Schedule[i][2])
        dp[i] = q
    return dp


print(max_profit([(1, 2, 50), (3, 5, 20), (6, 19, 100), (2, 100, 200)]))
