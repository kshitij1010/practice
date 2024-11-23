# Largest Smaller BST Key
#
# Given a root of a Binary Search Tree (BST) and a number num,
# implement an efficient function findLargestSmallerKey
# that finds the largest key in the tree that is smaller than num.
# If such a number doesn’t exist, return -1.
# Assume that all keys in the tree are nonnegative.
#
# Analyze the time and space complexities of your solution.
#
# For example:
# For num = 17 and the binary search tree below:
#             7
#         /        \
#       3          10
#     /  \       /     \
#    1   5      8      15
#                \    /    \
#                9   12    17
# Your function would return:
# 15 since it’s the largest key in the tree that is still smaller than 17.

# Tree Node
class Tree():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def find_largest_smaller_key(root, num):
    if root is None:
        return -1

    res = -1
    while root is not None:
        if root.data < num:
            res = root.data
            root = root.right
        else:
            root = root.left

    return res


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

print ("find_largest_smaller_key: ", find_largest_smaller_key(tree_root, 17))


# Follow up question:
# Write a function to find the 2nd largest element in a binary search tree.
def find_the_largest_num_in_tree(root):
    if root is None:
        raise Exception("Given root is None")

    largest = root.data

    while root is not None:
        if root.right is not None:
            largest = max(largest, root.right.data)
            root = root.right
        else:
            return largest
    return largest


def find_the_second_largedt_number_in_BST(root):
    if root is None:
        raise Exception("Given root is None")
    if root.left is None and root.right is None:
        raise Exception("Only one node in the Tree")

    num = find_the_largest_num_in_tree(root)

    res = find_largest_smaller_key(root, num)

    return res

print ("find_the_second_largedt_number_in_BST: ", find_the_second_largedt_number_in_BST(tree_root))
