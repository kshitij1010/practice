# Delete a given node in Linked List
#
# Full example of linked list class and methods

class NodeType:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def insert(self, val):
        temp = NodeType(val)
        if not self.head:
            self.head = temp
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = temp
        return

    def delete(self, val):
        curr = self.head
        if curr is None:
            print ("LinkedList is empty")
            return
        else:
            while curr.next is not None and curr.next == val:
                curr = curr.next

            if curr.next is not None:
                deleting_node = curr.next
                curr.next = deleting_node.next
                del deleting_node
            else:
                print ("Given valus is not in a LinkedList")
            return

    def get_len(self):
        return self.len

    def print_list(self):
        curr = self.head
        while curr is not None:
            print (curr.data, end=" ")
            curr = curr.next
        print ()
        return

l = LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.insert(6)
l.insert(7)
l.print_list()

l.delete(2)
l.print_list()
l.delete(3)
l.delete(6)
l.print_list()
