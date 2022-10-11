'''
Mamy dane n punktow (x, y) w okregu o promieniu k (liczba N), tnx. 0 <= x^2 + y^2 <= k,
które są w nim równomiernie rozłożone, tzn. pdb. znalezeinia punktu na danym obszarze jest
proporcjonalne do pola tego obszaru. Napisz algorytm sortujacy punktu po ich odleglosci do punktu (0, 0) tzn.
d = sqrt(x^2+y^2)
'''
from math import sqrt


def sort_points(T, k):
    def insertion_sort(A):
        n = len(A)
        for j in range(1, n):
            key = A[j][0]
            i = j - 1
            while i >= 0 and T[i][0] > key:
                A[i + 1] = A[i]
                i -= 1
            A[i + 1] = A[i]

    n = len(T)
    # Robie tablice pomocnicza z odleglosciami d i indeksem kazdego punktu
    D = [[0, 0] for _ in range(n)]
    for i in range(n):
        D[i][1] = i
        x = T[i][0]
        y = T[i][1]
        D[i][0] = sqrt(x*x + y*y)

    # kazdy bucket ma rozmiar [r(i-1), r(i)), czyli np pierwszy bucket to [0, r1)
    Buckets = [[] for _ in range(n + 1)]
    r1 = k / sqrt(n)
    print(r1)
    # for i in range(n):
    #     bucket_ind = 0
    #     Buckets[bucket_ind].append(D[i])


T = [(-3, 2), (-1, 3), (-1, -1), (-2, -3), (1, 1), (3, -1), (1, -2)]
k = 4
sort_points(T, k)