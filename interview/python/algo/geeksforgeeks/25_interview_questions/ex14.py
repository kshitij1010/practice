# Program for n’th node from the end of a singly Linked List

# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/


class NodeType:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_nth_from_last_elem(head, n):
    if n < 1:
        return None
    ref_node = head
    main = head

    for i in range(1, n):
        ref_node = ref_node.next

    if ref_node is None:
        # linked list length is smaller then given n
        return None

    while ref_node.next is not None:
        ref_node = ref_node.next
        main = main.next

    return main


head = NodeType(1)
head.next = NodeType(2)
head.next.next = NodeType(3)
head.next.next.next = NodeType(4)
head.next.next.next.next = NodeType(5)
head.next.next.next.next.next = NodeType(6)

print (find_nth_from_last_elem(head, 4).data) # returns 3
