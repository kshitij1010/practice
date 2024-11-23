# Left View of a tree
#
# Given a Binary Tree, print left view of it.
# Left view of a Binary Tree is set of nodes visible when tree is visited from left side.

# https://www.geeksforgeeks.org/print-left-view-binary-tree/


class Tree():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def left_view_util(root, level, max_level):
    if root is None:
        return

    if level > max_level[0]:
        print (root.val, end=" ")
        max_level[0] = level

    left_view_util(root.left, level+1, max_level)
    left_view_util(root.right, level+1, max_level)


def print_left_view_of_tree(root):
    max_level = [0]
    left_view_util(root, 1, max_level)
    print ()


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
print_left_view_of_tree(tree_root)



tree_root2 = Tree(12)
tree_root2.left = Tree(10)
tree_root2.right = Tree(30)
tree_root2.right.left = Tree(25)
tree_root2.right.right = Tree(40)
print_left_view_of_tree(tree_root2)
