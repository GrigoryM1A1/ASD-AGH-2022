'''Posortowana tablica, trzeba znalezc i,j takie, że T[i] - T[j] = x'''


# O(n)
def gasiennica(T, x):
    i = j = 0
    n = len(T)

    while i < n and j < n:
        if T[j] - T[i] < x:
            j += 1
        elif T[j] - T[i] > x:
            i += 1
        else:
            print(i, j, T[i], T[j])
            return i, j

    print("Nie ma takich i, j")
    return False


T = [1, 5, 6, 10, 12, 15, 16]
X = 3
gasiennica(T, 5)
