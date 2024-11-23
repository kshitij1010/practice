
# 105. Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# Output:
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None
        

class LinkedList():
    def __init__(self, head=None):
        if head:
            self.head = head
        else:
            self.head = Node()

    def insertNodeAtEnd(self, val):
        new_node = Node(val)
        
        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = new_node

    def insertNodeAtStart(self, val):
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        

    def removeNode(self, val):
        curr = self.head.next
        prev = self.head
        while curr != None:
            if curr.val == val:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next

    def printAllNodes(self, start_node=None):
        curr = self.head.next
        if start_node:
            curr = start_node

        while curr != None:
            print (curr.val)
            curr = curr.next


def partitionMod(head, partiton=0):
    if partiton == 0:
        return head
    
    lower_start = Node()
    lower = lower_start

    higher_start = Node()
    higher = higher_start

    while head:
        if head.val >= partiton:
            higher.next = Node(head.val)
            higher = higher.next
        else:
            lower.next = Node(head.val)
            lower = lower.next

        head = head.next


    lower.next = higher_start.next

    return lower_start.next

        
        

        


linkedlist = LinkedList() 
# head -> 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
linkedlist.insertNodeAtEnd(3)
linkedlist.insertNodeAtEnd(5)
linkedlist.insertNodeAtEnd(8)
linkedlist.insertNodeAtEnd(5)
linkedlist.insertNodeAtEnd(10)
linkedlist.insertNodeAtEnd(2)
linkedlist.insertNodeAtEnd(1)
print ("Before:")
linkedlist.printAllNodes()


# head -> 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10
newLinkedList = partitionMod(linkedlist.head.next, 5)
print ("After:")
linkedlist.printAllNodes(newLinkedList)
