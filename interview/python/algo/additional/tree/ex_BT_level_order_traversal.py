# # Binary Tree Level Order Traversal
#
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# Example,
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
class Tree():
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None


# using BFS
def level_order(root):
    # Edge case check
    if root is None:
        return []

    #  Edge case check
    if root.right is None and root.left is None:
        return [[root.val]]

    queue = []
    curr_level = []
    queue.append(root)

    res = []

    while queue:
        curr_level = queue
        temp = []
        for node in curr_level:
            temp.append(node.val)
        res.append(temp)

        queue = []
        for node in curr_level:
            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    return res


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

if __name__ == "__main__":
    print (level_order(tree_root))
