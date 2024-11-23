# Binary search for the sorted array (Implement iterative Binary Search.)
#
# time complexity : O(log n) where n is the size of given array
# space complexity: O(1) in case of iterative implementation
# In case of recursive implementation, O(Logn) recursion call stack space.

def binary_search_algo(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (end + start)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


arr = [ 2, 3, 4, 10, 40 ]
x = 2

print (arr, x)
print (binary_search_algo(arr, x))
