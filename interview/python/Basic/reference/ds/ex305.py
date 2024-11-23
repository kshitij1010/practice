# 305. Example of finding inorder successor

class Tree():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def inorder_successor(root, v):
    if not root:
        return None

    candidate = -1

    while root:
        if root.val == v:
            if root.right:
                candidate = root.right.val
                root = root.right
            else:
                return candidate
        elif root.val > v:
            candidate = root.val
            root = root.left
        else:
            root = root.right

    return candidate
            



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
# 1 3 5 7 8 9 10 12 15 17
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

print (inorder_successor(tree_root, 2))
