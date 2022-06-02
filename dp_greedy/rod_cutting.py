'''
f(i) = maksymalny zysk dla pręta o długości i
f(i) = max(f(k-i) + price[i]) | 0 <= i < k
f(0) = 0
wynik: f(n)

'''


def cut_rod(A):
    def get_price(ind):
        nonlocal A
        if ind == 0:
            return 0
        return A[ind-1]
    n = len(A)
    F = [0 for i in range(n+1)]
    R = [None for i in range(n+1)]
    inf = float('inf')
    for k in range(1, n+1):
        best = -inf
        for i in range(k+1):
            q = F[k-i] + get_price(i)
            if q > best:
                best = q
                R[k] = i
        F[k] = best

    res = []
    i = n
    while R[i] is not None:
        res.append(R[i])
        cut = R[i]
        i = i - cut
    print(res)
    return F[n]


Rod = [1, 5, 8, 9, 10, 17, 17, 20]  # wynik: 22
print(cut_rod(Rod))
