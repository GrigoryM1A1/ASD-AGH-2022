"""
You have infinite cards for each number between  and  (inclusive of them).
Your task is to select three integers such that after sorting them in ascending order,
the difference between the adjacent number is less than or equal to two.
Find the number of ways to choose three numbers and print them.
"""


def seq_tuples(N):
    if N > 4:
        F = [-1 for _ in range(N+1)]
        F[0] = 0
        F[1] = 1
        F[2] = 4
        F[3] = 10
        F[4] = 18
        for i in range(5, N+1):
            F[i] = F[i-1] + 9
        return F[N]

    elif N == 0:
        return None

    elif N == 1:
        return 1

    elif N == 2:
        return 4

    elif N == 3:

        return 10

    elif N == 4:
        return 18


print(seq_tuples(6))
