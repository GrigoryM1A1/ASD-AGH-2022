def cut_forrest(A):
    n = len(A)
    F = [0] * n  # F[i] - max zysk ze sciecia drzew 0, ..., i
    P = [None] * n
    F[0] = A[0]
    P[0] = (None, True)
    if A[1] >= A[0]:
        F[1] = A[1]
        P[1] = (None, True)
    else:
        F[1] = A[0]
        P[1] = (0, False)
    for i in range(2, n):
        if F[i - 1] >= F[i - 2] + A[i]:
            F[i] = F[i - 1]
            P[i] = (i - 1, False)
        else:
            F[i] = F[i - 2] + A[i]
            P[i] = (i - 2, True)

    res = []
    curr = n - 1
    while P[curr][0] is not None:
        if P[curr][1]: res.append(curr)
        curr = P[curr][0]
    if P[curr][1]: res.append(curr)

    return res[::-1]


A = [3, 4, 2, 8, 2, 5]
print(cut_forrest(A))
