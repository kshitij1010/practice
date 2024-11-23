# 306. Minimal Tree
# 
# Given a sorted (increasing order) array with unique interger elements,
# write an algorithm to create a binary search tree with minimal height


class Tree():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def generate_binary_tree_helper(arr, start, end):
    if end < start:
        return None


    mid = (end+start)//2
    root = Tree(arr[mid])
    # print ("abcd")

    root.left = generate_binary_tree_helper(arr, start, mid-1)
    root.right = generate_binary_tree_helper(arr, mid+1, end)
    return root

def generate_binary_tree(arr):
    return generate_binary_tree_helper(arr, 0, len(arr)-1)

def print_in_order(root):
    if root is None:
        return

    print_in_order(root.left)
    print (root.val, end=" ")
    print_in_order(root.right)

    return


arr = [-1, 5, 9, 100, 888]
tree_root = generate_binary_tree(arr)

print ("printing all nodes in In-Order: ")
print_in_order(tree_root)
print ()
