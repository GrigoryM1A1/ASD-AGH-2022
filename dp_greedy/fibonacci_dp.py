def fibonacci_dp(n):
    F = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    print(F[n])
    return F[n]


fibonacci_dp(5)
