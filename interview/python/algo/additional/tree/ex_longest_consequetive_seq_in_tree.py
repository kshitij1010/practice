# Longest consecutive sequence in Binary tree
#
# Given a Binary Tree find the length of the longest path
# which comprises of nodes with consecutive values in increasing order.
# Every node is considered as a path of length 1.
#
# Reference:
# https://www.geeksforgeeks.org/longest-consecutive-sequence-binary-tree/

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_longest_lcs(root):
    if root is None:
        return []
    res = []
    find_lcs(root, [], res)
    return res


def find_lcs(root, seq, res):
    if root is None:
        if len(seq) > len(res):
            del res[:]
            res += seq
        return

    if root.left is None or root.left.val == root.val+1:
        find_lcs(root.left, seq+[root.val], res)
    else:
        if len(seq) > len(res):
            del res[:]
            res += seq
        find_lcs(root.left, [], res)

    if root.right is None or root.right.val == root.val+1:
        find_lcs(root.right, seq+[root.val], res)
    else:
        if len(seq) > len(res):
            del res[:]
            res += seq
        find_lcs(root.right, [], res)
    return


tree_root = Tree(1)
tree_root.left = Tree(2)
tree_root.right = Tree(5)
tree_root.left.left = Tree(4)
tree_root.left.right = Tree(3)
tree_root.left.left = Tree(4)
tree_root.right.right = Tree(6)
tree_root.right.right.left = Tree(7)
tree_root.right.right.left.left = Tree(8)
print (find_longest_lcs(tree_root)) # 5,6,7,8

root = Tree(6)
root.right = Tree(9)
root.right.left = Tree(7)
root.right.right = Tree(10)
root.right.right.right = Tree(11)
print (find_longest_lcs(root)) # 9,10,11
