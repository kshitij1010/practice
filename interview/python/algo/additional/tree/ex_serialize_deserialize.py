# Serialize and Deserialize Binary Tree
#
# Serialization is to store tree in a file so that it can be later restored. The structure of tree must be maintained.
# Deserialization is reading tree back from file.
#
#
# References:
# https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


# Tree Node
class Tree():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


#################### Serialize
def serialize(root):
    res = []
    serialize_helper(root, res)
    return res

def serialize_helper(root, res):
        if root is None:
            res.append("|")
            return
        res.append(root.val)
        serialize_helper(root.left, res)
        serialize_helper(root.right, res)


#################### Deserialize
def deserialize(data):
    index = [0]
    root = deserialize_helper(data, index)
    return root

def deserialize_helper(data, index):
    if index[0] >= len(data) or data[index[0]] == "|":
        index[0] += 1
        return
    root = Tree(data[index[0]])
    index[0] += 1
    root.left = deserialize_helper(data, index)
    root.right = deserialize_helper(data, index)
    return root


#################### test

def print_in_order(root):
    if root is None:
        return

    print_in_order(root.left)
    print (root.val, end=" ")
    print_in_order(root.right)

    return


####################
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
print ("Original tree:")
print_in_order(tree_root)

serialized_data = serialize(tree_root)
print ("\n\nserialize data: ", serialized_data)
new_tree = deserialize(serialized_data)
print ("\n\nTree after deserialize:")
print_in_order(new_tree)
