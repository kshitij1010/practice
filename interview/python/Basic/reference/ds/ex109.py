# 109. Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C


# Detect loop in a linked list
#
# Given a linked list, check if the the linked list has loop or not.
#
# Below diagram shows a linked list with a loop.
# 1 -> 2 -> 3 -> 4 -> 5
#           ^        |
#           |        |
#           ----------
# Reference:
# https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/

class NodeType:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def print_linkedlist(node):
    while node is not None:
        print (node.data)
        node = node.next


def if_loop_in_linkedlist(node):
    slow = node
    fast = node

    while slow is not None and fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True

    return False


############ Followup ################
# detect loop and remove the loop from linked list
# Reference:
# https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
def detect_loop_and_delete_from_linkedlist(node):
    slow = node
    fast = node

    while fast is not None:
        slow = slow.next
        fast = fast.next.next
        if fast.next is None or slow is None or fast == slow:
            break

    if slow == fast and fast is not None:
        slow = node
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = None

    return


# example nodes as mentioned above
node1 = NodeType(1)
node2 = NodeType(2)
node3 = NodeType(3)
node4 = NodeType(4)
node5 = NodeType(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3

# print_linkedlist(node1) # this would go in an infinite loop
print (if_loop_in_linkedlist(node1))
# Detecting and deleting loop from a linkedlist
detect_loop_and_delete_from_linkedlist(node1)
print (if_loop_in_linkedlist(node1))
print_linkedlist(node1)
