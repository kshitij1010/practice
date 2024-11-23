# Pairwise swap elements of a given linked list
#
# Given a singly linked list, write a function to swap elements pairwise.
# For example,
# if the linked list is 1->2->3->4->5
# then the function should change it to 2->1->4->3->5,
#
# and if the linked list is 1->2->3->4->5->6
# then the function should change it to 2->1->4->3->6->5.

class NodeType():
    def __init__(self, data):
        self.data = data
        self.next = None


def swap_pairwise(head):
    temp = head

    while temp is not None and temp.next is not None:
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next

    return

def print_linked_list(head):
    temp = head

    while temp is not None:
        print (temp.data, end=" ")
        temp = temp.next
    print ("\n")
    return

head = NodeType(1)
head.next = NodeType(2)
head.next.next = NodeType(3)
head.next.next.next = NodeType(4)
head.next.next.next.next = NodeType(5)
head.next.next.next.next.next = NodeType(6)

print_linked_list(head)
swap_pairwise(head)
print_linked_list(head)
