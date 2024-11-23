# Lowest Common Ancestor in a Binary Tree
#
# Given a binary tree (not a binary search tree) and two values say n1 and n2,
# write a program to find the least common ancestor.
#
# Reference:
# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/


class Tree():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

# If given tree is Binary tree
def findLCA(root, n1, n2):
    if root is None:
        return None


    if n1 == root.val or n2 == root.val:
        return root

    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    if left_lca is not None:
        return left_lca

    return right_lca

tree_root = Tree(7)
tree_root.left = Tree(5)
tree_root.right = Tree(12)
tree_root.left.left = Tree(1)
tree_root.left.right = Tree(3)
tree_root.right.left = Tree(8)
tree_root.right.left.right = Tree(9)
tree_root.right.right = Tree(15)
tree_root.right.right.left = Tree(10)
tree_root.right.right.right = Tree(17)

"""
Example,
            7
        /        \
       5          12
     /  \       /     \
    1    3     8      15
                \    /    \
                9   10    17
"""

print ("BT LCA:", findLCA(tree_root, 1, 17).val)





########### Follow up question #############
# If given tree is Binary search tree
def findLCA_BST(root, n1, n2):
    if root is None:
        return -1

    if n1 > n2:
        return findLCA_BST(root, n2, n1)

    while root is not None:
        if root.val > n1 and root.val < n2:
            return root.val

        if root.val == n1 or root.val == n2:
            return root.val
        elif root.val < n1:
            root = root.right
        else:
            root = root.left

    return -1

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
tree_root1 = Tree(7)
tree_root1.left = Tree(3)
tree_root1.right = Tree(10)
tree_root1.left.left = Tree(1)
tree_root1.left.right = Tree(5)
tree_root1.right.left = Tree(8)
tree_root1.right.left.right = Tree(9)
tree_root1.right.right = Tree(15)
tree_root1.right.right.left = Tree(12)
tree_root1.right.right.right = Tree(17)
print ("BST LCA:", findLCA_BST(tree_root1, 8, 17))
