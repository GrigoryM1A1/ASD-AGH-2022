def change(T):
    A = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    F = [0]*(T+1)   # F[i] - minimalna ilosc monet potrzebna do wydania kwoty i
    P = [0]*(T+1)
    for i in range(T+1):
        minimal = float('inf')
        for x in A:
            if x <= i and F[i-x] < minimal:
                minimal = F[i-x]
                F[i] = minimal + 1
                P[i] = i-x
    if F[T] == 0:
        return False
    else:
        res = []
        current = T
        while current != 0:
            res.append(current - P[current])
            current = P[current]
    return res
