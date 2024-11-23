# 101. program to create the linkedlist with creating node, deleting node, printing all node methods



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

    def printAllNodes(self):
        curr = self.head.next

        while curr != None:
            print (curr.val)
            curr = curr.next


linkedlist = LinkedList() 
# head -> 33 -> 22 -> 11 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 111 -> 222
linkedlist.insertNodeAtEnd(7)
linkedlist.insertNodeAtEnd(6)
linkedlist.insertNodeAtEnd(5)
linkedlist.insertNodeAtEnd(4)
linkedlist.insertNodeAtEnd(3)
linkedlist.insertNodeAtEnd(2)
linkedlist.insertNodeAtEnd(1)
linkedlist.insertNodeAtStart(11)
linkedlist.insertNodeAtEnd(111)
linkedlist.insertNodeAtStart(22)
linkedlist.insertNodeAtStart(33)
linkedlist.insertNodeAtEnd(222)
linkedlist.removeNode(7)
linkedlist.removeNode(33)
linkedlist.removeNode(222)

linkedlist.printAllNodes()
