# left-view, right-view, top-view, bottom-view


class Tree:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None


################## left_view
def left_view(root):
    if root is None:
        return
    level = [float('-inf')]
    left_view_print(root, 0, level)
    return

def left_view_print(root, cur_lev, mx_lev):
    if root is None:
        return

    if cur_lev > mx_lev[0]:
        mx_lev[0] = cur_lev
        print (root.val,  end=" ")

    left_view_print(root.left, cur_lev+1, mx_lev)
    left_view_print(root.right, cur_lev+1, mx_lev)
    return


################## right_view
def right_view(root):
    if root is None:
        return
    level = [float('-inf')]
    right_view_print(root, 0, level)
    return

def right_view_print(root, cur_lev, mx_lev):
    if root is None:
        return

    if cur_lev > mx_lev[0]:
        mx_lev[0] = cur_lev
        print (root.val,  end=" ")

    right_view_print(root.right, cur_lev+1, mx_lev)
    right_view_print(root.left, cur_lev+1, mx_lev)
    return

################## top_view
from collections import defaultdict
def top_view(root):
    if root is None:
        return
    level = defaultdict(list)
    top_view_print(root, 0, level)

    for key, val in sorted(level.items()):
        print (val[0], end=" ")

    return

def top_view_print(root, cur_lev, level):
    if root is None:
        return

    level[cur_lev].append(root.val)

    top_view_print(root.left, cur_lev-1, level)
    top_view_print(root.right, cur_lev+1, level)
    return


################## bottom_view
from collections import defaultdict
def bottom_view(root):
    if root is None:
        return
    level = defaultdict(list)
    bottom_view_print(root, 0, level)

    for key, val in sorted(level.items()):
        print (val[-1], end=" ")

    return

def bottom_view_print(root, cur_lev, level):
    if root is None:
        return

    level[cur_lev].append(root.val)

    bottom_view_print(root.left, cur_lev-1, level)
    bottom_view_print(root.right, cur_lev+1, level)
    return


tree_root = Tree(1)
tree_root.left = Tree(2)
tree_root.right = Tree(3)
tree_root.right.left = Tree(5)
tree_root.right.right = Tree(4)
print ("left view:")
left_view(tree_root)
print ("\nright view:")
right_view(tree_root)
print ("\ntop view:")
top_view(tree_root)
print ("\nbottom view:")
bottom_view(tree_root)




tree_root2 = Tree(12)
tree_root2.left = Tree(10)
tree_root2.right = Tree(30)
tree_root2.right.left = Tree(25)
tree_root2.right.right = Tree(40)
print ("\n\nleft view2:")
left_view(tree_root2)
print ("\nright view2:")
right_view(tree_root2)
print ("\ntop view2:")
top_view(tree_root2)
print ("\nbottom view2:")
bottom_view(tree_root2)
