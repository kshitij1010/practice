# Insert into a Binary Search Tree
# Difficulty:Medium
#
# Given the root node of a binary search tree (BST) and a value to be inserted into the tree,
# insert the value into the BST. Return the root node of the BST after the insertion.
# It is guaranteed that the new value does not exist in the original BST.
#
# Note that there may exist multiple valid ways for the insertion,
# as long as the tree remains a BST after insertion. You can return any of them.
#
# For example,
#
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# And the value to insert: 5
# You can return this binary search tree:
#
#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# This tree is also valid:
#
#          5
#        /   \
#       2     7
#      / \
#     1   3
#          \
#           4
#
# Reference:
# https://leetcode.com/problems/insert-into-a-binary-search-tree/

from ex_BT_level_order_traversal import level_order

class Tree():
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None

def insertion_helper(root, val, mn, mx):
        if root is None:
            root = Tree(val)
            return root

        if mn < val < root.val:
            # goes to left
            if root.left is None:
                root.left = Tree(val)
                return
            insertion_helper(root.left, val, mn, root.val)

        if root.val < val < mx:
            # goes to right
            if root.right is None:
                root.right = Tree(val)
                return
            insertion_helper(root.right, val, root.val, mx)

        return

def insert_into_BST(root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    mn = float('-inf')
    mx = float('inf')
    returned_root = insertion_helper(root, val, mn, mx)
    if returned_root:
        return returned_root
    return root



"""
Example,
            7
        /        \
       3          10
     /  \       /     \
    1   5      8      15
                \    /    \
                9   12    17
"""


tree_root = Tree(7)
tree_root.left = Tree(3)
tree_root.right = Tree(10)
tree_root.left.left = Tree(1)
tree_root.left.right = Tree(5)
tree_root.right.left = Tree(8)
tree_root.right.left.right = Tree(9)
tree_root.right.right = Tree(15)
tree_root.right.right.left = Tree(12)
tree_root.right.right.right = Tree(17)

print ("Example-1:")
print ("Orig tree:", level_order(tree_root))
tree_root = insert_into_BST(tree_root, 4)
print ("After inserting a node:", level_order(tree_root))

print ("\nExample-2:")
tree_root1 = None
print ("Orig tree:", level_order(tree_root1))
tree_root1 = insert_into_BST(tree_root1, 41)
print ("After insertinga node:", level_order(tree_root1))
