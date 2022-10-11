'''Dodawanie noda do posortowanej listy, usuwanie maksymalnego noda (zwracamy wskaźnik na usuniety), selsort i insort'''


# None -> 3 -> 4 -> 12 -> 14 -> 17 -> None dodajemy 6

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert(L, elem):
    while L.next is not None and L.next.val < elem.val:
        L = L.next

    elem.next = L.next
    L.next = elem


def del_max(L):
    maks = L
    while L.next is not None:
        if L.next.val > maks.next.val:
            maks = L
        L = L.next

    res = maks.next
    maks.next = maks.next.next

    return res


def insort(L):
    A = Node(None)
    while L.next is not None:
        K = L.next
        L.next = L.next.next
        insert(A, K)
    L.next = A.next
    return L


def selsort(L):
    S = Node(None)
    while L.next is not None:
        x = del_max(L)
        x.next = S.next
        S.next = x
    L.next = S.next
    return L


def wypisz(L):
    L = L.next
    while L is not None:
        print(L.val, end="  ")
        L = L.next


el4 = Node(2)
el3 = Node(1)
el3.next = el4
el2 = Node(4)
el2.next = el3
el1 = Node(3)
el1.next = el2
wart = Node(None)
wart.next = el1


wypisz(wart)
print("")
a = selsort(wart)
wypisz(a)