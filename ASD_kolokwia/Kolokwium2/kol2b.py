from kol2btesty import runtests
'''
Grzegorz Piśkorski

f(i) = minimalny koszt dojechania do parkingu i korzystając z warunku podpunkt 2 lub nie
f(0) = A[0]
f(i) = min{ f(i-k) + C[i], f(i-l) + C[i] } k oraz l zawierają się w przedziale [0, i-1], parking jest brany tylko
wtedy gdy odleglosc miedzy i oraz k jest z przedzialu [0, T] lub gdy odleglosc miedzy i oraz l jest
z przedzialu [T+1, 2T]
'''


def min_cost( O, C, T, L ):
    def get_dist(a, b):
        nonlocal prefix_sum
        return prefix_sum[b] - prefix_sum[a]
    n = len(O)

    for i in range(n):
        tmp = O[i]
        O[i] = [tmp, C[i]]

    O.sort(key=lambda z: z[0])

    for i in range(n):
        park = O[i][0]
        cost = O[i][1]
        O[i] = park
        C[i] = cost

    prefix_sum = [0 for i in range(n)]
    prefix_sum[0] = O[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + O[i]

    inf = float('inf')
    F = [inf for i in range(n)]
    F[0] = C[0]
    for i in range(1, n):
        x = y = inf
        for k in range(i):
            print(get_dist(k, i))
            if 0 <= get_dist(k, i) <= T and F[i-k] + C[i] < x:
                x = F[i-k] + C[i]
        for l in range(i):
            if 0 <= get_dist(l, i) <= 2 * T and F[i-l] + C[i] < y:
                y = F[i-l] + C[i]
        if O[i] - T <= 0 or O[i] - 2 * T <= 0:
            pass

        F[i] = min(x, y)
    return F[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
