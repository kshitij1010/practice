# 303. Check Balanced: Implement a function to check if bianry tree is banalanced.
# A Balanced tree is defined to be a tree
# such that the height of the two subtrees of any node never differ by more than one.

class Tree():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def check_height(root):
    if root is None:
        return 0

    left = check_height(root.left)
    right = check_height(root.right)

    if left == -1 or right == -1 or abs(left-right) > 1:
        return -1

    return max(left, right) + 1


def ifBalanced(root):
    return check_height(root) != -1


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
tree_root.left.right.right = Tree(55)
tree_root.right.left = Tree(8)
tree_root.right.left.right = Tree(9)
tree_root.right.right = Tree(15)
tree_root.right.right.left = Tree(12)
tree_root.right.right.right = Tree(17)

print (ifBalanced(tree_root))
