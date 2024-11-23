# A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset 
# and you don’t have a pre-shifted copy of it. 
# For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.
# 
# Given shiftArr and an integer num, 
# implement a function shiftedArrSearch that finds 
# and returns the index of num in shiftArr. 
# If num isn’t in shiftArr, return -1. 
# Assume that the offset can be any value between 0 and arr.length - 1.
# 
# Example.
# Input: shiftArr = [ 9, 12, 17, 2, 4, 5] num = 2
# Output: 3
# 
# Input   : [[9, 12, 17, 2, 4, 5], 9]
# Output  : 0

def shifted_arr_search(nums, target):
    if len(nums) == 0 or nums is None:
        return -1
    
    low = 0
    high = len(nums)-1
    
    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
            
    return -1

# [5, 0, 1,2,3,4] = 0

data = [
    {
        "input": [[ 9, 12, 17, 2, 4, 5 ], 2],
        "output": 3,
    },
    {
        "input": [[ 9, 12, 17, 2, 4, 5 ], 9],
        "output": 0,
    },
    {
        "input": [[ 9, 12, 17, 2, 4, 5 ], 5],
        "output": 5,
    },
    {
        "input": [[ 9, 12, 17, 2, 4, 5 ], 22],
        "output": -1,
    },
    {
        "input": [[ 9, 12, 17, 2, 4, 5 ], 17],
        "output": 2,
    },
    {
        "input": [[2], 2],
        "output": 0,
    },
    {
        "input": [[1, 2], 2],
        "output": 1,
    },
    {
        "input": [[0,1,2,3,4,5], 1],
        "output": 1,
    },
    {
        "input": [[1,2,3,4,5,0], 0],
        "output": 5,
    },
    {
        "input": [[9,12,17,2,4,5,6], 4],
        "output": 4,
    },
    {
        "input": [[5,0,1,2,3,4], 0],
        "output": 1,
    }
]


from helper import Test
test = Test()
test.check(shifted_arr_search, data)



































# def shifted_arr_search(arr, num):
  
#   start = 0
#   end = len(arr)-1

#   while start <= end:
#     mid = (end + start) // 2
    
#     if arr[mid] == num:
#       return mid
#     elif arr[mid] < arr[start]:
#       if arr[mid] <= num <= arr[end]:
#         start = mid + 1
#       else:
#         end = mid - 1
#     else:
#       if arr[start] <= num <= arr[mid]:
#         end = mid - 1
#       else:
#         start = mid + 1
    
      
#   return -1
