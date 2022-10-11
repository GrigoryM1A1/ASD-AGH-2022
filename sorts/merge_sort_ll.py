class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def rip(L):
    while L.next is not None and L.val <= L.next.val:
        L = L.next
    p = L.next
    L.next = None
    return p


def tail(L):
    while L.next is not None:
        L = L.next
    return L


def merge(A, B):
    C = Node(None)
    D = C
    while True:
        if A is None:
            D.next = B
            return C.next, tail(B)
        if B is None:
            D.next = A
            return C.next, tail(A)
        if A.val <= B.val:
            D.next = A
            A = A.next
            D = D.next
        else:
            D.next = B
            B = B.next
            D = D.next


def merge_sort(L):
    T = tail(L)

    while True:
        A = L
        L = rip(L)
        if L is None:
            return A

        B = L
        L = rip(L)
        C, D = merge(A, B)
        if L is None:
            return C
        T.next = C
        T = D


def print_ll(L):
    while L is not None:
        print(L.val, end="  ")
        L = L.next
    print("")


el6 = Node(5)
el5 = Node(6)
el5.next = el6
el4 = Node(4)
el4.next = el5
el3 = Node(2)
el3.next = el4
el2 = Node(3)
el2.next = el3
el1 = Node(0)
el1.next = el2
el0 = Node(1)
el0.next = el1

new_L = merge_sort(el0)
print_ll(new_L)
