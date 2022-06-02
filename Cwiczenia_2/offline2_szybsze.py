'''
kurde, powiem Ci, że z drobnymi przerwami praktycznie cały czas myślę jak dostać te wyniki g(b) i f(a) w czasie liniowym i chyba ani trochę nie jestem bliżej rozwiązania xd


Robimy sobie 2 tablice:
- starts - trzymamy w niej przedziały posortowane rosnąco względem ich poczatkow oraz jako trzecia informacje
trzymamy ich wagi (liczbe identycznych przedzialow)
- end - trzymamy w niej posortowane rosnaco konce przedzialow oraz liczbe przedzialow konczacych sie na ta
pierwsza liczbe



f(x) - liczba przedziałów, które zaczynają się na pozycji wczesniejszej niz x

g(x) - liczba przedziałów kończących się na pozycji x lub wcześniej

I teraz tak
Jak mamy przedział [a;b]
To liczba takich przedziałów które zawierają się w [a,b] to g(b) - f(a) - 1

c = g(b) - f(a) - 1

Dowód i implementacja była do domu XD
Jedna tylko uwaga: ten wzór nie będzie zawsze podawał dobrych wyników, ale na pewno poda dobre rozwiązanie,
tzn jak będziemy mieli sytuacje ze jest przedział [1;8], [5;6] i inne, to dla przedziału [5;6] ta różnica nie okaże się
prawdziwą liczba przedziałów zawierających się
Ale dla [1;8] wynik będzie na 100% dobry i to nas interesuje
'''
from random import randint


def quick_sort(T, m):                        # <--- Randomizowany quick sort bez rekurencji korzystajacy z logn pamieci
    def partition(A, l, r, ind):
        piv = randint(l, r)
        A[piv], A[r] = A[r], A[piv]
        x = A[r][ind]
        i = l - 1
        for j in range(l, r):
            if A[j][ind] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i + 1

    def quicksort(A, l, r, ind):
        S = []
        S.append((l, r))
        while len(S) != 0:
            l, r = S.pop()
            if l < r:
                q = partition(A, l, r, ind)
                if q - l < r - q:
                    S.append((q + 1, r))
                    S.append((l, q - 1))
                else:
                    S.append((l, q - 1))
                    S.append((q + 1, r))
    quicksort(T, 0, len(T) - 1, m)


# g(b) - f(a) - 1 dizała w chuj
# dodac se pozycje do pierwszej tablicy, zrobic se nowa, i dodawac ilosc powtorzonych przedzialow


def depth(L):
    n = len(L)
    for i in range(n):  # dodanie indeksu dla kazdego przedizalu
        L[i].append(i)

    Starts = [[0, 0] for i in range(n)]     # <- tablica na liczbe mniejszych indeksow poczatkow przedzialow od indeksu i
    Ends = [[0, 0] for i in range(n)]      # <- tablica na liczbe mniejszych lub rownych indeksow konca przedzialow od indeksu i
    # trzeba liniowo policzyc liczby dla kazdego poczatku i konca

    quick_sort(L, 0)
    i = 0
    while i < n - 1:
        tmp = i
        while i < n - 1 and L[i][0] == L[i+1][0]:
            Starts[i][0] = tmp
            Starts[i][1] = L[i][2]
            i += 1
        Starts[i][0] = tmp
        Starts[i][1] = L[i][2]
        i += 1
    if L[n - 1][0] == L[n - 2][0]:
        Starts[n - 1][0] = Starts[n - 2][0]
        Starts[n - 1][1] = L[n - 1][2]
    else:
        Starts[n - 1][0] = n - 1
        Starts[n - 1][1] = L[n - 1][2]

    quick_sort(L, 1)
    i = n - 1
    while i > 0:
        tmp = i + 1
        while i > 0 and L[i][1] == L[i-1][1]:
            Ends[i][0] = tmp
            Ends[i][1] = L[i][2]
            i -= 1
        Ends[i][0] = tmp
        Ends[i][1] = L[i][2]
        i -= 1
    if L[0][1] == L[1][1]:
        Ends[0][0] = Ends[1][0]
        Ends[0][1] = L[0][2]
    else:
        Ends[0][0] = 1
        Ends[0][1] = L[0][2]

    c_tab = [[0, 0] for i in range(n)]
    for i in range(n):
        c_tab[Starts[i][1]][0] = Starts[i][0]
        c_tab[Ends[i][1]][1] = Ends[i][0]

    c = c_tab[0][1] - c_tab[0][0] - 1
    for i in range(1, n):
        curr_c = c_tab[i][1] - c_tab[i][0] - 1
        if curr_c > c:
            c = curr_c
    return c
    # # Robienie tablicy posortowanych poczatkow przedzialow wraz z liczba wystapien tych samych przedzialow O(n)
    # quick_sort(L, 0)   # Quick sort iterowany wykorzystujacy maksymalnie O(logn) pamieci - O(nlogn)
    # print("Posortowane poczatkami: ", L)
    # i = 1
    # # while i < n:
    # #     pass
    # print("")
    #
    #
    # # Robienie tablicy posortowanych koncow przedzialow wraz z liczba wystapien w innych przedzialach O(n)
    # quick_sort(L, 1)    # Quick sort iterowany wykorzystujacy maksymalnie O(logn) pamieci - O(nlogn)
    # print("Posortowane koncami: ", L)
    # i = 1
    # while i < n:
    #     tmp = 1
    #     while i < n and L[i-1][1] == L[i][1]:
    #         tmp += 1
    #         i += 1
    #     Ends.append((L[i-1][1], tmp))
    #     tmp = 0
    #     if i == n - 1 and L[i-1][1] != L[i][1]:
    #         Ends.append((L[i][1], 1))
    #     i += 1
    # print("Ends: ", Ends)
    #
    # # Wyliczanie z aktualnego przedzialu [a, b] najwiekszej liczby zawartych przedzialow
    # ze wzoru g(b) - f(a) + w(a) - 1


L1 = [[1, 6],
      [5, 6],
      [2, 5],
      [8, 9],
      [1, 6]]
print("Nieposortowane: ", L1)
print("")
print(depth(L1))

# L2 = [[1, 6],
#       [5, 6],
#       [4, 5],
#       [1, 4],
#       [2, 5],
#       [7, 8]]
# print("Nieposortowane: ", L2)
# depth(L2)
# L3 = [[2, 5],
#       [3, 4],
#       [1, 6]]
# depth(L3)
# L4 = [[1, 4],
#       [1, 6],
#       [1, 5],
#       [1, 4],
#       [1, 4],
#       [1, 5],
#       [1, 6],
#       [1, 5],
#       [4, 5],
#       [2, 8],
#       [0, 1]]
# print("Nieposortowane: ", L4)
# depth(L4)

