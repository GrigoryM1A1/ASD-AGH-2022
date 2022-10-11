'''bubble_sort  selection_sort  insertion_sort'''


def bubble_sort(tab):
    n = len(tab)

    for i in range(n-1):
        for j in range(n-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    print(tab)
    return tab


def selection_sort(tab):
    n = len(tab)

    for i in range(n):
        pos = i
        print("i=", i)
        for j in range(i+1, n):
            print("j=", j)
            if tab[j] < tab[pos]:
                pos = j
        tab[i], tab[pos] = tab[pos], tab[i]
        print("=======")
    print(tab)


def insertion_sort(tab):
    n = len(tab)

    for j in range(1, n):
        key = tab[j]
        i = j-1

        while i >= 0 and tab[i] > key:
            tab[i+1] = tab[i]
            i -= 1
        tab[i+1] = key

    print(tab)


T = [3, 4, 2, 1, 7, 5, 3, 2, 2, 11, 10, 6, 9]
# bubble_sort(T)
# print(T)
# selection_sort(T)
insertion_sort(T)
print(T)
