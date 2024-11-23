# 107. Palindrome: Implement a function to check if a linked list is a palindrome.



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

def isPalindrome(head):
    slow, fast, curr = head, head, head
    helper = None

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next


    while slow:
        next = slow.next
        slow.next = helper
        helper = slow
        slow = next

    while helper and curr:
        if helper.val != curr.val:
            return False

        helper = helper.next
        curr = curr.next

    return True


linkedlist = LinkedList() 
# head -> 1 -> 2 -> 2 -> 1
linkedlist.insertNodeAtEnd(1)
linkedlist.insertNodeAtEnd(2)
linkedlist.insertNodeAtEnd(2)
linkedlist.insertNodeAtEnd(1)
# true
print (isPalindrome(linkedlist.head.next))



linkedlist2 = LinkedList() 
# head -> 1 -> 2 -> 3 -> 2 -> 1
linkedlist2.insertNodeAtEnd(1)
linkedlist2.insertNodeAtEnd(2)
linkedlist2.insertNodeAtEnd(3)
linkedlist2.insertNodeAtEnd(2)
linkedlist2.insertNodeAtEnd(1)
# true
print (isPalindrome(linkedlist2.head.next))


linkedlist3 = LinkedList() 
# head -> 1 -> 2 -> 3 -> 2 -> 5
linkedlist3.insertNodeAtEnd(1)
linkedlist3.insertNodeAtEnd(2)
linkedlist3.insertNodeAtEnd(3)
linkedlist3.insertNodeAtEnd(2)
linkedlist3.insertNodeAtEnd(1)
linkedlist3.insertNodeAtEnd(5)
# false
print (isPalindrome(linkedlist3.head.next))
