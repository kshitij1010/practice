# 304. Validate BST: Implement a function to check if a binary tree is a binary search tree.


class Tree():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def ifBST(root):
    if not root:
        return True

    if root.left and root.left.val >= root.val:
        return False

    if root.right and root.right.val <= root.val:
        return False

    return ifBST(root.left) and ifBST(root.right)


'''
Example,
            7
        /        \
       3          10
     /  \       /     \
    1   5      8      15
                \    /    \
                9   12    17
'''
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

print (ifBST(tree_root))
