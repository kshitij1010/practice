# TREE example:
# 1. find the max height of the tree
# 2. find the min height of the tree
# 3. check if the given binary tree is binary search tree(BST) or not
# 4. print leaf node
# 5. print full node
# 6. print Pre-order, In-order, Post-order
# 7. print all the route from root node to leaf node
# 8. print all the node of the route with the max height of the tree


# Tree Node
class Tree():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# find the max height of the binary search tree
def find_max_height_of_tree(root):
    if root is None:
        return 0

    return max(find_max_height_of_tree(root.left), find_max_height_of_tree(root.right)) + 1

# find the min height of the binary search tree
def find_min_height_of_tree(root):
    if root is None:
        return 0

    return min(find_min_height_of_tree(root.left), find_min_height_of_tree(root.right)) + 1

# check if the given binary tree is binary search tree(BST) or not
def if_tree_BST_util(root, mini, maxi):
    if root is None:
        return True

    if root.data < mini or root.data > maxi:
        return False

    return if_tree_BST_util(root.left, mini, root.data-1) and if_tree_BST_util(root.right, root.data+1, maxi)

def if_tree_BST(root):
    mini, maxi = float('-inf'), float('inf')
    return if_tree_BST_util(root, mini, maxi)


# print leaf node
def print_leaf_node(root):
    if root.left is None and root.right is None:
        print (root.data, end=" ")
        return

    if root.left is not None:
        print_leaf_node(root.left)

    if root.right is not None:
        print_leaf_node(root.right)

    return

# print Full Nodes (Full Nodes are nodes which has both left and right children as non-empty.)
def print_full_node(root):
    if root is None:
        return

    if root.left is not None and root.right is not None:
        print (root.data, end=" ")
        print_full_node(root.left)
        print_full_node(root.right)

    return

# print Pre-order (root, left, right)
def print_pre_order(root):
    if root is None:
        return

    print (root.data, end=" ")
    print_pre_order(root.left)
    print_pre_order(root.right)

    return

# print In-order (left, root, right)
def print_in_order(root):
    if root is None:
        return

    print_in_order(root.left)
    print (root.data, end=" ")
    print_in_order(root.right)

    return

# print Post-order (left, right, root)
def print_post_order(root):
    if root is None:
        return

    print_post_order(root.left)
    print_post_order(root.right)
    print (root.data, end=" ")

    return

# print all the route from root to leaf
def print_route_root_to_leaf(stack, root):
    if root is None:
        return

    stack.append(root.data)
    if root.left is None and root.right is None:
        # means this is the leaf node
        print (stack)

    # otherwise try both the subtrees
    print_route_root_to_leaf(stack, root.left)
    print_route_root_to_leaf(stack, root.right)
    # since we already encountered/printed all the route which includes the current node
    stack.pop()

# print all the node of the route with the max height of the tree
def print_nodes_of_max_height_branch(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [root.data]

    left_side = print_nodes_of_max_height_branch(root.left)

    right_side = print_nodes_of_max_height_branch(root.right)

    if len(left_side) >= len(right_side):
        left_side.append(root.data)
        return left_side

    right_side.append(root.data)
    return right_side

"""
Example,
            7
        /        \
       3          10
     /  \       /     \
    1   5      8      15
                \    /    \
                9   12    17


print_pre_order(tree_root) => 7 3 1 5 10 8 9 15 12 17
print_in_order(tree_root) => 1 3 5 7 8 9 10 12 15 17
print_post_order(tree_root) => 1 5 3 9 8 12 17 15 10 7
print_leaf_node(tree_root) => 1 5 9 12 17
print_full_node(tree_root) => 7 3 10 15
find_min_height_of_tree(tree_root) => 3
find_max_height_of_tree(tree_root) => 4
if_tree_BST(tree_root) => yes

print_route_root_to_leaf =>
                        [7, 3, 1]
                        [7, 3, 5]
                        [7, 10, 8, 9]
                        [7, 10, 15, 12]
                        [7, 10, 15, 17]
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

# printing all nodes
print ("printing all nodes in Pre-Order: ") #
print_pre_order(tree_root)
print ("\nprinting all nodes in In-Order: ")
print_in_order(tree_root)
print ("\nprinting all nodes in Post-Order: ")
print_post_order(tree_root)

# printing leaf nodes
print ("\nprinting all leaf node: ")
print_leaf_node(tree_root)

# printing full nodes
print ("\nprinting all full nodes: ")
print_full_node(tree_root)

# printing min height of Tree
print ("\nMin height of tree:", find_min_height_of_tree(tree_root))

# printing max height of Tree
print ("Max height of tree:", find_max_height_of_tree(tree_root))

# if tree BST
print ("If given tree BST? => ", if_tree_BST(tree_root))

# print all the route from root to leaf
print ("All the routes from root to leaf node =>")
print_route_root_to_leaf([], tree_root)

# print all the node of the route with the max height of the tree
print ("Root to leaf max height branch: ", print_nodes_of_max_height_branch(tree_root))
