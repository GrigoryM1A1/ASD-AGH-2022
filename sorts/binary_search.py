'''
O(logn) - algorytm podaje czy element znajduje sie w uporzadkowanej tablicy i na ktorej pozycji
'''


def binary_search(T, elem):
    left = 0
    right = len(T) - 1

    while left <= right:
        ind = (left + right) // 2
        if T[ind] < elem:
            left = ind + 1
        elif T[ind] > elem:
            right = ind - 1
        else:

            return ind

    print("Brak takiego elementu")
    return None

