"""Given a 3 x n board, find the number of ways to fill it with 2 x 1 dominoes."""


def possible_dominoes_tilings(n):
    A = [0 for _ in range(n+1)]
    B = [0 for _ in range(n+1)]
    A[0] = B[1] = 1
    A[1] = B[0] = 0

    for i in range(2, n+1):
        # na rysunku w miare ladnie widac
        A[i] = A[i - 2] + 2 * B[i - 1]
        B[i] = A[i-1] + B[i-2]
    return A[n]


print(possible_dominoes_tilings(8))

