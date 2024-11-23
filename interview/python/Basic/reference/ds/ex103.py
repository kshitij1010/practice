# 103. Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

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

    def find_kth_elem(self, k):
        faster_pointer = self.head.next

        for i in range(k):
            if faster_pointer == None:
                return "Invalid k"
            faster_pointer = faster_pointer.next
            

        curr = self.head.next
        while faster_pointer:
            curr = curr.next
            faster_pointer = faster_pointer.next
        
        if curr:
            return curr.val

        return "Invalid k"

    def printAllNodes(self):
        curr = self.head.next

        while curr != None:
            print (curr.val)
            curr = curr.next


linkedlist = LinkedList() 
# head  7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1
linkedlist.insertNodeAtEnd(7)
linkedlist.insertNodeAtEnd(6)
linkedlist.insertNodeAtEnd(5)
linkedlist.insertNodeAtEnd(4)
linkedlist.insertNodeAtEnd(3)
linkedlist.insertNodeAtEnd(2)
linkedlist.insertNodeAtEnd(1)
linkedlist.printAllNodes()

print ("kth element:")
print (linkedlist.find_kth_elem(-9))
