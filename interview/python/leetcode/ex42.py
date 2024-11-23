# Description
# Given an array of integers representing heights in a bar graph, determine the volume of water that it can hold.

# Question Statement
# Input: An array of positive integers that represent the heights of bars in a bar chart. Heights are guaranteed to be >= 1.

# Output: The number of "units" of water that the bar chart can hold.

# Note that water "spills over" the sides if there's nothing to contain it. Formally, a cell can contain water if, and only if, it has a wall to its right and a wall to its left.

# Examples

# Example 1
# Input: [5, 3, 2, 1, 5]
# Output: 9

# Empty     Filled
# #   #     #...#
# #   #     #...#
# ##  #     ##..#
# ### #     ###.#
# #####     #####
# 53215

# Example 2
# Input: [2, 4, 1, 5, 3]
# Output: 3

# Empty     Filled

#    #         #
#  # #       #.#
#  # ##      #.##
# ## ##     ##.##
# #####     #####

# Example 3
# Input: [2, 1, 5, 1, 3]
# Output: 3

# Empty     Filled

#   #         #
#   #         #
#   # #       #.#
# # # #     #.#.#
# #####     #####

# Example 4
# Input: [1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1]
# Output: 7

# Empty        Filled

#    #   #        #...#
#  # # # # #    #.#.#.#.#
# ###########  ###########

def waterVolume(arr):
    
    if arr is None or len(arr) <= 1:
        return 0
    
    
    left_max = []
    maximum_left = float('-inf')
    for n in arr:
        maximum_left = max(maximum_left, n)
        left_max.append(maximum_left)
        
        
    right_max = []
    maximum_right = float('-inf')
    for n in arr[::-1]:
        maximum_right = max(maximum_right, n)
        right_max.append(maximum_right)
    
    right_max = right_max[::-1]
        
    helper_res = 0
    for i,n in enumerate(arr):
        diff = min(left_max[i]-n, right_max[i]-n)
        helper_res += diff
        
    return helper_res


print (waterVolume([1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1]))
