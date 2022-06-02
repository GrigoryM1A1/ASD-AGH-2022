'''
Grzegorz Piśkorski

Niestety mój algorytm to najprostszy brute force. O(n^2 * k)
Dla każdego wyrazu sprawdzamy czy jakiś inny wyraz z listy różny od aktualnie rozpatrywanego
jest tym samym wyrazem lub wyrazem napisanym wspak.
Co do k nie jestem pewny ale zapewne y = x[::-1] ma złożoność O(k) gdzie k to długość wyraz.

Były inne pomysły, ale każdy kończył się fiaskiem :(
'''


from kol1atesty import runtests


def g(T):
    n = len(T)
    Maximums = [0] * n
    counter = 1
    for i in range(n):
        for j in range(n):
            if i != j:
                reverse = T[j][::-1]
                if T[i] == T[j] or T[i] == reverse:
                    counter += 1
        Maximums[i] = counter
        counter = 1

    maks = Maximums[0]
    for i in range(1, n):
        if Maximums[i] > maks:
            maks = Maximums[i]

    return maks


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
