class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def del_min(p):
    min_node = p
    while p != None:
        if p.val < min_node.val:
            min_node = p
        p = p.next




def sel_sort(head):
    first = head

    return first


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
