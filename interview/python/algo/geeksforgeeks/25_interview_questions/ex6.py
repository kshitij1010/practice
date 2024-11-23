# Find the middle of a given linked list

# Given a singly linked list, find middle of the linked list.
# For example, if given linked list is 1->2->3->4->5 then output should be 3.

# https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/


class NodeType():
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle_elem_of_linked_list(head):
    if head is None:
        return None

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    print (slow.data)

    return


head = NodeType(1)
head.next = NodeType(2)
head.next.next = NodeType(3)
head.next.next.next = NodeType(4)
head.next.next.next.next = NodeType(5)
head.next.next.next.next.next = NodeType(6)


find_middle_elem_of_linked_list(head)
