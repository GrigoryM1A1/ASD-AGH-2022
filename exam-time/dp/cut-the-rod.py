"""
f(i) = maksymalny zysk dla pręta o długości i
f(i) = max(f(k-i) + price[i]) | 0 <= i < k
f(0) = 0
wynik: f(n)
"""


def cut_rod(A):
    n = len(A)
    F = [0 for _ in range(n+1)]
    inf = float('inf')

    for k in range(1, n+1):
        best = -inf
        for i in range(k+1):
            # indeksujemy od 1, to musimy dostosowac indeks do tablicy od 0
            ind = i-1 if i > 0 else 0

            # sprawdzamy wszystkie mozliwe dlugosci preta
            q = F[k-i] + A[ind]
            if q > best:
                best = q
        F[k] = best

    return F[n]


Rod = [1, 5, 8, 9, 10, 17, 17, 20]
print(cut_rod(Rod))
