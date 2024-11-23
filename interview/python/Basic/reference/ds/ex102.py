# 102. Remove Dups: Write code to remove duplicates from an unsorted linked list. FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?



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

    def removeDuplicates(self):
        prev = self.head
        curr = self.head.next
        val_tracker = set()

        while curr != None:
            if curr.val in val_tracker:
                prev.next = curr.next
            else:
                val_tracker.add(curr.val)
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
linkedlist.insertNodeAtEnd(2)
linkedlist.insertNodeAtEnd(7)
linkedlist.insertNodeAtEnd(7)


print("1st example: ")
print("All nodes: ")
linkedlist.printAllNodes()

linkedlist.removeDuplicates()
print("All nodes(after deleting duplicate nodes): ")
linkedlist.printAllNodes()

######
print("\n\n2nd example: ")
example2_node = LinkedList()
print("All nodes: ")
example2_node.printAllNodes()

example2_node.removeDuplicates()
print("All nodes(after deleting duplicate nodes): ")
example2_node.printAllNodes()
