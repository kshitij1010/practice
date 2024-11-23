class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    if head is None:
            return None

    prev = None
    curr = head

    while curr:
        temp_next = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next

    return prev


def print_list(head):
    temp = head
    while temp:
        print (temp.data, end = " ")
        temp = temp.next
    print ()
    return


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print_list(head)

new = reverse_linked_list(head)
print_list(new)
