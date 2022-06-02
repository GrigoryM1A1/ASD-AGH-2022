class Node:
    def __init__(self, val, next_item):
        self.val = val
        self.next = next_item


def print_list(head):
    p = head
    while p is not None:
        print(p.val)
        p = p.next


def insertion_sort_ll(head):
    def insert(head, new_node):
        if head is None or head.val >= new_node.val:
            new_node.next = head
            return new_node
        else:
            first = head
            while head.next is not None and head.next.val < new_node.val:
                head = head.next
            new_node.next = head.next
            head.next = new_node
        return first

    first = None
    while head is not None:
        head_next = head.next
        first = insert(first, head)
        head = head_next
    return first


def selecton_sort_ll(head):
    first = head
    while head is not None:
        min_val = head
        tmp = head.next
        while tmp is not None:
            if min_val.val > tmp.val:
                min_val = tmp
            tmp = tmp.next
        head.val, min_val.val = min_val.val, head.val
        head = head.next
    return first


node6 = Node(4, None)
node5 = Node(5, node6)
node4 = Node(2, node5)
node3 = Node(10, node4)
node2 = Node(3, node3)
node1 = Node(7, node2)

# print_list(node1)
# print("==========")
# beans = insertion_sort_ll(node1)
# print_list(beans)

print_list(node1)
print("==========")
beeeansss = selecton_sort_ll(node1)
print_list(beeeansss)