'''
f(i) = na ile sposobów można dojść do pozycji i
'''


def amazon_stairs(A):
    n = len(A)
    F = [0 for _ in range(n+1)]
    F[0] = 1
    for i in range(n):
        for j in range(1, A[i] + 1):
            if i + j <= n:
                F[i+j] += F[i]
    print(F)
    return F


A = [2, 1, 3, 2, 2, 3]
amazon_stairs(A)
