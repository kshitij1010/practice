# 108. Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
# node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.


class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None

def printAllNodes(head):
    curr = head

    s = ""
    while curr:
        s += " " + str(curr.val)
        curr = curr.next

    print (s)


def ifIntersect(l1, l2):
    a = l1
    b = l2
    
    while a != b:
        if not a:
            a = l2
        else:
            a = a.next
        
        if not b:
            b = l1
        else:
            b = b.next

    return True if a else False




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)


# 1st linked list ( 1 -> 2 -> 3 -> 4 -> 5 )
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print ("1st linked list")
printAllNodes(node1)

# 2nd linked list ( 7 -> 6 -> 3 -> 4 -> 5 )
node7.next = node6
node6.next = node3
print ("2nd linked list")
printAllNodes(node7)


# 2nd linked list ( 8 -> 7 -> 6 )
node10.next = node9
node9.next = node8
print ("2nd linked list")
printAllNodes(node10)

print (ifIntersect(node1, node7)) # true
print (ifIntersect(node1, node10)) # false
print (ifIntersect(node7, node10)) # false
