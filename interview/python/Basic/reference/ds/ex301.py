# 301. Basic TREE questions:
#         1. find the max height of the tree
#         2. find the min height of the tree
#         3. check if the given binary tree is binary search tree(BST) or not
#         4. print leaf node
#         5. print full node
#         6. print Pre-order, In-order, Post-order
#         7. print all the route from root node to leaf node
#         8. print all the node of the route with the max height of the tree


class Tree():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def find_max_height(root):
    if not root:
        return 0

    return max(find_max_height(root.left), find_max_height(root.right)) + 1

def find_min_height(root):
    if not root:
        return 0

    return min(find_min_height(root.left), find_min_height(root.right)) + 1

def ifBST(root):
    if not root:
        return True

    if root.left and root.val < root.left.val:
        return False

    if root.right and root.val > root.right.val:
        return False

    return ifBST(root.left) and ifBST(root.right)

def print_leaf_nodes(root):
    if not root:
        return

    if root.left == None and root.right == None:
        print (root.val)

    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)
    return

def print_full_nodes(root):
    if not root:
        return

    if root.right and root.left:
        print (root.val)

    print_full_nodes(root.left)
    print_full_nodes(root.right)
    return

def print_preorder(root):
    if not root:
        return

    print (root.val)
    print_preorder(root.left)
    print_preorder(root.right)

def print_inorder(root):
    if not root:
        return

    print_inorder(root.left)
    print (root.val)
    print_inorder(root.right)

def print_postorder(root):
    if not root:
        return

    print_postorder(root.left)
    print_postorder(root.right)
    print (root.val)


def print_all_routes_helper(root, stack):
    if not root:
        return
    
    temp = stack+[root.val]
    if not root.left and not root.right:
        print (temp)
        return

    print_all_routes_helper(root.left, temp)
    print_all_routes_helper(root.right, temp)
    
    return


def print_all_routes(root):
    if not root:
        return []

    stack = []
    return print_all_routes_helper(root, stack) 
    

def print_nodes_of_max_height_branch(root):
    if not root:
        return []

    if not root.left and not root.right:
        [root.val]

    left = print_nodes_of_max_height_branch(root.left)
    right = print_nodes_of_max_height_branch(root.right)

    if len(left) >= len(right):
        left.append(root.val)
        return left

    right.append(root.val)
    return right

def print_nodes_of_max_height_branch_helper(root, curr_stack, stack, max_height):
    if not root:
        return 
    
    temp = curr_stack+[root.val]
    if not root.left and not root.right:
        if len(temp) < max_height[0]:
            return

        if len(temp) > max_height[0]:
            stack.clear()
        max_height[0] = len(temp)
        stack += [temp]

    print_nodes_of_max_height_branch_helper(root.left, temp, stack, max_height) 
    print_nodes_of_max_height_branch_helper(root.right, temp, stack, max_height) 
    return


def print_nodes_of_max_height_branch2(root):
    curr_stack = []
    stack = []
    max_height = [0]
    print_nodes_of_max_height_branch_helper(root, curr_stack, stack, max_height)
    return stack

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


print ("max height of tree:", find_max_height(tree_root))
print ("min height of tree:", find_min_height(tree_root))
print ("if binary search tree:", ifBST(tree_root))
print ("leaf nodes")
print_leaf_nodes(tree_root)
print ("full nodes")
print_full_nodes(tree_root)
print ("pre-order")
print_preorder(tree_root)
print ("in-order")
print_inorder(tree_root)
print ("post-order")
print_postorder(tree_root)
print ("All routes")
print_all_routes(tree_root)
print ("Root to leaf max height branch: ", print_nodes_of_max_height_branch(tree_root))
print ("all root to leaf max height branch: ", print_nodes_of_max_height_branch2(tree_root))
