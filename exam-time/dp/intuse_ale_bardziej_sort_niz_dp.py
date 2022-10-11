"""
Dany jest zbiór przedziałów domkniętych I, gdzie każdy przedział zaczyna się i kończy na liczbie
naturalnej (wliczając 0). Dane są także dwie liczby naturalne x i y.
Dwa przedziały mozna skleić (czyli zamienić na przedział będący ich suumą mnogościową) jeśli mają dokładnie
jeden punkt wspólny. Jeśli pewne przedziały można posklejać tak, że powstaje z nich przedział [x, y] to
mówimy, że są przydatne.

Proszę napisać funkcję, która zwraca listę numerów wszystkich przydatnych przedziałów.

Sortujemy tablicę I, następnie wyodrębniamy z niej spójny podciąg wszystkich przedziałów o początkach
z zakresu [x, y - 1]. Można ten fragment zapisać nawet w nowej tablicy dla wygody. Inicjalizujemy zwykłą kolejkę Q.
Dodajemy do kolejki wszystkie przedziały zaczynające się na x. Wyciągamy po kolei elementy z kolejki Q.
Wyciągając dany przedział [a, b], wyszukujemy binarnie pierwszy przedział w tablicy zaczynający się na b i oznaczamy
go jako odwiedzony (nowa tablica True/False, tak aby nie dublować elementów, a sprawdzenie czy przedziały zaczynające
się na b zostały dodane zredukować do O(1)), a następnie wszystkie przedziały zaczynające się na b dodajemy na koniec
kolejki. Jeżeli pierwszy przedział o początku b został odwiedzony, nie  dodajemy niczego i pobieramy z kolejki kolejny
przedział. Powtarzamy proces wypychania przedziałów z kolejki do momentu aż natrafimy na przedział kończący się na y.
Jeżeli na takowy nie natrafimy, to nie istnieje odpowiedni dobór przedziałów. Żeby zrekonstruować listę przydatnych
przedziałów wystarczy zrobić osobną tablicę parentów i zapisywać poprzedniki każdego z przedziałów
"""
from collections import deque


def binary_search(brackets, b):
    n = len(brackets)
    left = 0
    right = n - 1

    while left <= right:
        ind = (left + right) // 2
        if brackets[ind][0] < b:
            left = ind + 1
        elif brackets[ind][0] > b:
            right = ind - 1
        else:
            while ind >= 0 and brackets[ind][0] == b:
                ind -= 1
            ind += 1
            return ind
    return -1


def intuse(I, x, y):
    n = len(I)
    support_I = [(I[i][0], I[i][1], i) for i in range(n)]
    support_I.sort(key=lambda z: z[0])

    useful_brackets = []
    for a, b, i in support_I:
        if x <= a < y:
            useful_brackets.append((a, b, i))

    parent = [-1 for _ in range(len(useful_brackets))]
    visited = [False for _ in range(len(useful_brackets))]
    Q = deque([])
    l = 0
    while l < len(useful_brackets) and useful_brackets[l][0] == x:
        Q.append(useful_brackets[l])
        l += 1

    while Q:
        a, b, ind = Q.popleft()
        int_index = binary_search(useful_brackets, b)
        if int_index != -1:
            visited[int_index] = True

    return 0


print(intuse([(3, 4), (2, 5), (1, 3), (4, 6), (1, 4)], 1, 6))
