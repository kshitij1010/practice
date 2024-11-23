# 104. Delete Middle Node: Implement an algorithm to delete a node in the middle 
# (i.e., any node but the first and last node, not necessarily the exact middle) 
# of a singly linked list, given only access to
# that node.
# EXAMPLE
# lnput:the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

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


    def removeOnlyMiddleNode(self, val):
        curr = self.head.next.next
        prev = self.head.next

        while curr:
            if curr.val == val and curr.next != None:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next

    def printAllNodes(self):
        curr = self.head.next

        while curr != None:
            print (curr.val)
            curr = curr.next


linkedlist = LinkedList() 
# head -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 
linkedlist.insertNodeAtEnd(7)
linkedlist.insertNodeAtEnd(6)
linkedlist.insertNodeAtEnd(5)
linkedlist.insertNodeAtEnd(4)
linkedlist.insertNodeAtEnd(3)
linkedlist.insertNodeAtEnd(2)
linkedlist.insertNodeAtEnd(1)
print ("Before:")
linkedlist.printAllNodes()
linkedlist.removeOnlyMiddleNode(1)
linkedlist.removeOnlyMiddleNode(4)
linkedlist.removeOnlyMiddleNode(3)
print ("After:")
# head -> 7 -> 6 -> 5 -> 2 -> 1 
linkedlist.printAllNodes()
