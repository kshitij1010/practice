# Counting Unival Subtrees / Find Count of Single Valued Subtrees
#
# Given a binary tree, write a program to count the number of Single Valued Subtrees.
# A Single Valued Subtree is one in which all the nodes have same value.
# Expected time complexity is O(n).
#
# Reference:
# https://www.dailycodingproblem.com/blog/unival-trees/
# https://www.geeksforgeeks.org/find-count-of-singly-subtrees/


class Tree():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_unival(root):
    if root is None:
        return (True, 0)

    left_unival, left_val = is_unival(root.left)
    right_unival, right_val = is_unival(root.right)

    is_valid = True

    if root.left and (not left_unival or root.val != root.left.val):
        is_valid = False

    if root.right and (not right_unival or root.val != root.right.val):
        is_valid = False

    if not is_valid:
        return (False, left_val+right_val)

    return (True, left_val+right_val+1)


"""
            5
          /   \
        4       5
       /  \      \
      4    4      5
"""
root = Tree(5)
root.left = Tree(4)
root.right = Tree(5)
root.left.left = Tree(4)
root.left.right = Tree(4)
root.right.right = Tree(5)
print (is_unival(root)[1])
