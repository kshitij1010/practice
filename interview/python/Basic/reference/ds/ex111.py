# Deepcopy of linked list
#
# Given a linked list where each node has two pointers,
# one to the next node and one to a random node in the list, clone the linked list.
#
# Reference:
# https://www.byte-by-byte.com/randomlinkedlist/
# https://www.youtube.com/watch?v=xF9goDxk5nM

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.random = None


def deep_copy(head):
    if head is None:
            return

    # adding copy-node in between with the same value and random pointer being None
    curr = head
    while curr:
        temp_next = curr.next
        new_node = Node(curr.val, temp_next, None)
        curr.next = new_node
        curr = temp_next

    # adding random pointer of the node
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        else:
            curr.next.random = None
        curr = curr.next.next



    new_head = head.next
    curr = head
    while curr.next:
        temp_next = curr.next
        curr.next = curr.next.next
        curr = temp_next

    return new_head
